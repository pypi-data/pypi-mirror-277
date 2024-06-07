import unittest
import os
from img2otxt.convert import convert_image_to_text


class TestImageToTextConversion(unittest.TestCase):

    def setUp(self):
        self.image_path = 'tests/New.png'  # Path relative to the root of the project
        self.output_dir = os.getcwd()

    def test_conversion(self):
        convert_image_to_text(self.image_path, self.output_dir)
        text_path = os.path.join(self.output_dir, 'output.txt')
        self.assertTrue(os.path.exists(text_path))
        with open(text_path, 'r') as file:
            content = file.read()
            self.assertNotEqual(content, '')


if __name__ == '__main__':
    unittest.main()
