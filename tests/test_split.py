import os
import tempfile
import unittest
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from splitxfiles import split_by_lines, split_by_size


class TestSplitFiles(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.mkdtemp()
        self.test_file = os.path.join(self.temp_dir, 'test.txt')
        with open(self.test_file, 'w') as f:
            for i in range(25):
                f.write(f"Line {i+1}\n")

    def test_split_by_lines(self):
        output_dir = os.path.join(self.temp_dir, 'output')
        split_by_lines(self.test_file, output_dir, 10, verbose=False)
        files = os.listdir(output_dir)
        self.assertEqual(len(files), 3)

    def test_split_by_size(self):
        output_dir = os.path.join(self.temp_dir, 'output_size')
        split_by_size(self.test_file, output_dir, 50, verbose=False)
        files = os.listdir(output_dir)
        self.assertTrue(len(files) > 0)

    def test_invalid_input(self):
        result = split_by_lines('nonexistent.txt', 'output', 10, verbose=False)
        self.assertFalse(result)

    def test_invalid_lines(self):
        result = split_by_lines(self.test_file, 'output', 0, verbose=False)
        self.assertFalse(result)

    def tearDown(self):
        import shutil
        shutil.rmtree(self.temp_dir)


if __name__ == '__main__':
    unittest.main()
