import os
from typing import Any


def get_model_config_var(var_name: str, default: str, **kwargs: Any) -> str:
    """Get the model config variable.

    Args:
        var_name (str): Variable name.
        model_config (dict): Model config.

    Returns:
        str: Model config variable value.

    """
    model_config = kwargs.get("deployment_config")
    config = (
        model_config[var_name]
        if model_config and model_config.get(var_name)
        else default
    )
    if not config:
        raise ValueError(f"Missing model config variable: {var_name}")
    return config


def add_rerank_model_to_request_state(
    model: str,
    **kwargs: Any,
) -> None:
    request = kwargs.get("request", None)
    if not request:
        return
    request.state.rerank_model = model
