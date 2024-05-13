from pathlib import Path

from deployment.streaming import lambda_function
from deployment.streaming.inc_dec import decrement, increment  # The code to test


def test_increment():
    assert increment(3) == 4


# This test is designed to fail for demonstration purposes.
def test_decrement():
    assert decrement(3) == 2


def test_test():
    ride = {"PULocationID": 130, "DOLocationID": 205, "trip_distance": 3.66}
    expected_features = {"PU_DO": "130_205", "trip_distance": 3.66}

    assert lambda_function.test(ride) == expected_features


def read_text(file):
    test_path = Path(__file__).parent
    with open(test_path / file, "rt", encoding="utf-8") as f:
        return f.read().strip()


def test_base64_decode():
    encoded_data = read_text("data.b64")
    expected_encoded_data = {
        "ride": {"PULocationID": 130, "DOLocationID": 205, "trip_distance": 3.66},
        "ride_id": 256,
    }
    assert lambda_function.base64_decode(encoded_data) == expected_encoded_data
