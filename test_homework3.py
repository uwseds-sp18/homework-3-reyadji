import numpy as np
import unittest
from homework3 import create_dataframe


class Homework3Tests(unittest.TestCase):
    """Unit tests class for homework3.py."""

    test_file = 'class.db'
    test_df = create_dataframe(test_file)
    col_length = test_df.shape[0]

    def test_column_names(self):
        """Testing the DataFrame column names are
        video_id, category_id, language columns
        """
        self.assertTrue(
            np.all(self.test_df.columns == ['category_id', 'video_id', 'language']))

    def test_number_rows(self):
        """Testing there are at least 10 rows in the DataFrame"""
        self.assertTrue(self.col_length >= 10)

    def test_category_id_key(self):
        """Testing category_id column whether it constitute a key"""
        self.assertEqual(
            self.col_length,
            len(self.test_df['category_id'].unique()),
            'category_id is not a key'
            )

    def test_video_id_key(self):
        """Testing video_id column whether it constitute a key"""
        self.assertEqual(
            self.col_length,
            len(self.test_df['video_id'].unique()),
            'video_id is not a key'
            )

    def test_language_key(self):
        """Testing language column whether it constitute a key"""
        self.assertEqual(
            self.col_length,
            len(self.test_df['language'].unique()),
            'language is not a key'
            )

    def test_path_exception(self):
        """Testing whether invalid path raise ValueError exception"""
        self.assertRaises(ValueError, create_dataframe, 'nonexistant_file.db')


if __name__ == '__main__':
    unittest.main()
