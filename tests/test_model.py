# test_model.py
import os
import sys
import unittest

# Get the absolute path to the parent directory
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

class TestModel(unittest.TestCase):
    def test_model_file_exists(self):
        # Use the absolute path to the model file
        model_path = os.path.join(parent_dir, 'models', 'model.h5')
        self.assertTrue(os.path.exists(model_path))

if __name__ == '__main__':
    unittest.main()