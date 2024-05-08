from pathlib import Path
import unittest  # The test framework
from deployment.streaming import lambda_function
from deployment.streaming.inc_dec import increment, decrement


class TestIncrementDecrement(unittest.TestCase):
    def test_increment(self):
        self.assertEqual(increment(3), 4)

    # This test is designed to fail for demonstration purposes.
    def test_decrement(self):
        self.assertEqual(decrement(3), 2)

    def test_test(self):
        ride = {"PULocationID": 130, "DOLocationID": 205, "trip_distance": 3.66}
        expected_features = {"PU_DO": "130_205", "trip_distance": 3.66}

        self.assertEqual(lambda_function.test(ride), expected_features)

    def read_text(self, file):
        test_path = Path(__file__).parent
        with open(test_path / file, "rt", encoding="utf-8") as f:
            return f.read().strip()

    def test_base64_decode(self):
        encoded_data = self.read_text("data.b64")
        expected_encoded_data = {
            "ride": {
                "PULocationID": 130,
                "DOLocationID": 205,
                "trip_distance": 3.66,
            },
            "ride_id": 256,
        }
        self.assertEqual(
            lambda_function.base64_decode(encoded_data), expected_encoded_data
        )

    def test_predict(self):
        self.assertEqual(1, 1)


if __name__ == "__main__":
    unittest.main()
