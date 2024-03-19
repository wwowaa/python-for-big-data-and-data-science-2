import unittest
import pandas as pd

from app.io.input import read_from_file, read_with_pandas


class TestInput(unittest.TestCase):

    def test_read_from_file_with_python_existing_file(self):
        test_content = "Test content for read_from_file function."
        test_file = "test_file.txt"
        with open(test_file, 'w') as file:
            file.write(test_content)

        self.assertEqual(read_from_file(test_file), test_content)

    def test_read_from_file_with_python_nonexistent_file(self):
        non_existent_file = "non_existent_file.txt"
        self.assertIsNone(read_from_file(non_existent_file))

    def test_read_from_file_with_pandas_existing_file(self):
        test_data = {'A': [1, 2, 3], 'B': [4, 5, 6]}
        test_df = pd.DataFrame(test_data)
        test_csv_file = "test_data.csv"
        test_df.to_csv(test_csv_file, index=False)

        pd.testing.assert_frame_equal(read_with_pandas(test_csv_file), test_df)

    def test_read_from_file_with_pandas_nonexistent_file(self):
        non_existent_file = "non_existent_file.csv"
        self.assertIsNone(read_with_pandas(non_existent_file))


if __name__ == '__main__':
    unittest.main()
