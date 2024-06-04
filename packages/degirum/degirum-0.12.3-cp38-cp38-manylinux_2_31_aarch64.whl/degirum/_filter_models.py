#
# _filter_models.py - DeGirum Python SDK: common models filtering
# Copyright DeGirum Corp. 2022
#
# Contains DeGirum common models filtering implementation
#

import re
from pathlib import Path
from typing import Optional, List
from .exceptions import DegirumException
from .aiclient import ModelParams


def check_runtime_device_supported(
    runtime: Optional[str],
    device: Optional[str],
    mparams: ModelParams,
) -> bool:
    """Check if model supports given runtime agent type and device type combination.

    Args:
        runtime: runtime agent type or None to ignore
        device: device type or None to ignore
        mparams: model info

    Returns:
        True if model supports given runtime agent type and device type combination, False otherwise
    """

    # check against default runtime and device
    if (runtime is None or runtime == mparams.RuntimeAgent) and (
        device is None or device == mparams.DeviceType
    ):
        return True

    supported_types = mparams.SupportedDeviceTypes
    if not supported_types:
        return False

    # convert string to list of [runtime, device] pairs
    supported_list = [t.split("/") for t in re.split("[,; ]+", supported_types)]

    # check if given runtime/device combination is supported
    for t in supported_list:
        if len(t) != 2:
            raise DegirumException(
                f"Invalid format of supported device list '{supported_types}' for model '{mparams.ModelPath}'"
            )

        runtime_match = runtime is None or t[0] == "*" or runtime == t[0]
        device_match = device is None or t[1] == "*" or device == t[1]
        if runtime_match and device_match:
            return True

    return False


def _filter_models(
    model_family=None,
    *,
    models,
    system_supported_device_types: List[str],
    device=None,
    precision=None,
    pruned=None,
    runtime=None,
):
    """List all available model matching to specified filter values.

    - `models`: callback to acquire models info using model identifier
    - `system_supported_device_types`: list of available system devices in format "RUNTIME/DEVICE"
    - `model_family`: model family: a string to match any part of the model name; for example, "yolo", "mobilenet1"
    - `device`: target inference device(s): a string or a string list of device labels; possible labels: "orca", "orca1", "cpu", "gpu", "edgetpu", "dla", "dla_fallback", "myriad", "npu"
    - `precision`: model calculation precision: a string or a string list of precision labels; possible labels: "quant", "float"
    - `pruned`: model density: a string or a string list of density labels; possible labels: "dense", "pruned"
    - `runtime`: type of inference runtime(s): a string or a string list of runtime labels; possible labels: "n2x", "tflite", "tensorrt", "openvino"

    Returns list of matching model names
    """

    def _to_list(value):
        """Convert value to the list containing this value if it is not list already.
        Returns empty list if value is None
        """
        if not value:
            return []
        elif not isinstance(value, list):
            return [value]
        else:
            return value

    model_family = (
        [model_family]
        if isinstance(model_family, re.Pattern)
        else _to_list(model_family)
    )
    device = _to_list(device)
    precision = _to_list(precision)
    pruned = _to_list(pruned)
    runtime = _to_list(runtime)
    system_rt_dev_pairs = [d.split("/") for d in system_supported_device_types]

    for value, description, supported_values, check in [
        (
            model_family,
            "model_family",
            ["yolo", "mobilenet", "..."],
            lambda f, lst: not isinstance(f, str) and not isinstance(f, re.Pattern),
        ),
        (
            device,
            "device",
            [
                "ORCA",
                "ORCA1",
                "CPU",
                "GPU",
                "EDGETPU",
                "DLA",
                "DLA_FALLBACK",
                "MYRIAD",
                "NPU",
                "DUMMY",
            ],
            lambda f, lst: not isinstance(f, str) or f.upper() not in lst,
        ),
        (
            precision,
            "precision",
            ["QUANT", "FLOAT"],
            lambda f, lst: not isinstance(f, str) or f.upper() not in lst,
        ),
        (
            pruned,
            "pruned",
            ["PRUNED", "DENSE"],
            lambda f, lst: not isinstance(f, str) or f.upper() not in lst,
        ),
        (
            runtime,
            "runtime",
            ["N2X", "TFLITE", "ONNX", "OPENVINO", "TENSORRT", "DUMMY"],
            lambda f, lst: not isinstance(f, str) or f.upper() not in lst,
        ),
    ]:
        for f in value:
            if check(f, supported_values):
                raise DegirumException(
                    f"Filter '{description}' has unsupported value '{f}'. Possible values are: {supported_values}"
                )

    def re_filter(mparams, lst):
        return lst[0].match(Path(mparams.ModelPath).stem)

    def str_filter(mparams, lst):
        return any(n in Path(mparams.ModelPath).stem for n in lst)

    def density_filter(mparams):
        name = Path(mparams.ModelPath).stem
        p = name.split("--")[-1].split("_")[::-1]
        return "PRUNED" if len(p) >= 5 and p[4].upper() == "PRUNED" else "DENSE"

    def quant_filter(mparams):
        name = Path(mparams.ModelPath).stem
        p = name.split("--")[-1].split("_")[::-1]
        return "QUANT" if len(p) >= 4 and p[3].upper() == "QUANT" else "FLOAT"

    def is_device_supported(mparams, device_list):
        system_devices = [d[1] for d in system_rt_dev_pairs]
        return any(
            check_runtime_device_supported(None, dev, mparams)
            for dev in device_list
            if dev in system_devices
        )

    def is_runtime_supported(mparams, runtime_list):
        system_runtimes = [d[0] for d in system_rt_dev_pairs]
        return any(
            check_runtime_device_supported(rt, None, mparams)
            for rt in runtime_list
            if rt in system_runtimes
        )

    def is_in_system_devices(mparams, _):
        return any(
            check_runtime_device_supported(r, d, mparams)
            for r, d in system_rt_dev_pairs
        )

    filters_configuration = [
        (system_supported_device_types, is_in_system_devices),
        (
            model_family,
            (
                re_filter
                if model_family and isinstance(model_family[0], re.Pattern)
                else str_filter
            ),
        ),
        ([s.upper() for s in device], is_device_supported),
        ([s.upper() for s in runtime], is_runtime_supported),
        (
            [s.upper() for s in precision],
            lambda mparams, lst: quant_filter(mparams) in lst,
        ),
        (
            [s.upper() for s in pruned],
            lambda mparams, lst: density_filter(mparams) in lst,
        ),
    ]

    current = models()
    for filter_to_check, check_function in filters_configuration:
        if filter_to_check:
            current = [v for v in current if check_function(models(v), filter_to_check)]

    return current
