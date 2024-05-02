import os

truthy_values = {
    "1": True,
    "true": True,
    True: True,
    1: True,
}


def get_env_param_str(param_name: str, default: str = None, required: bool = False):
    param_str = os.environ.get(param_name) or default
    if param_str is None and required:
        raise Exception("Incorrect env param: {}".format(param_name))
    return param_str


def get_env_param_bool(param_name, default=None, required=True):
    param_str = os.environ.get(param_name) or default
    if param_str is None and required:
        raise OSError(f"Incorrect env param: {param_name}")

    if isinstance(param_str, str):
        param_str = param_str.lower()

    return truthy_values.get(param_str, False)
