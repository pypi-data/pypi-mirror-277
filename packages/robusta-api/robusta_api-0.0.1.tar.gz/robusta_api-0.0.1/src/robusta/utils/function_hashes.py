import hashlib
import inspect
import json

from pydantic import BaseModel

# this returns a hash that will change if the function's definition changes
# this is desirable because it lets you warn users if a playbook is called with parameters that
# were generated by a previous version of the playbook. in that case you can ask the user if you should
# call the playbook anyway even though the code that the callback refers to has changed


def get_function_hash(func):
    plaintext = str(inspect.getfullargspec(func)).encode() + func.__code__.co_code
    return hashlib.sha256(plaintext).hexdigest()


def action_hash(func, action_params: BaseModel, additional_data: dict) -> str:
    hash_input = (
        f"{get_function_hash(func)}"
        + ("None" if additional_data is None else json.dumps(additional_data))
        + ("None" if action_params is None else action_params.json())
    )
    return hashlib.md5(hash_input.encode()).hexdigest()
