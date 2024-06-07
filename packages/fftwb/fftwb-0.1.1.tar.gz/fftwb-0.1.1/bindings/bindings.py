import sys

sys.path.append("../build")
sys.path.append("./generated")

import json

from src.serialize import *
from src.deserialize import *

from twb import run, indicator


print(
    deserialize_indicator_request(
        serialize_indicator_request(
            "EMA", {"default": [20, 30, 50, 40, 40, 30]}, {"i": "10"}
        )
    )
)

serialized_ind = indicator(
    serialize_indicator_request(
        "EMA", {"default": [20, 30, 50, 40, 40, 30]}, {"i": "10"}
    )
)

print(deserialize_arr(serialized_ind))
