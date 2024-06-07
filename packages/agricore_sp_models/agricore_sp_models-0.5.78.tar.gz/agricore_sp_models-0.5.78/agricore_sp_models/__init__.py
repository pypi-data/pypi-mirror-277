from pydantic import BaseModel, root_validator
from typing import Any


class CaseInsensitiveModel(BaseModel):
    @root_validator(pre=True)
    def __preserve_input_keys__(cls, values: Any) -> Any:
        def __lower__(value: Any) -> Any:
            if isinstance(value, dict):
                return {k.lower(): __lower__(v) for k, v in value.items()}
            return value

        values = __lower__(values)
        model_keys = {key.lower(): key for key in cls.__fields__.keys()}

        for key in list(values.keys()):
            if key.lower() in model_keys:
                values[model_keys[key.lower()]] = values.pop(key)

        return values