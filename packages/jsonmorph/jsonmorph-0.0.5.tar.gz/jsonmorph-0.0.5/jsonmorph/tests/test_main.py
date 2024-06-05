import unittest
from jsonmorph.main import process_json
# from  ..main import process_json

class TestProcessJson(unittest.TestCase):
    def test_process_json(self):
        input_file = 'jsonmorph/tests/files/input.json'
        settings_file = 'jsonmorph/tests/files/setting.json'
        output_file = 'jsonmorph/tests/files/output.json'
        process_json(input_file, settings_file, output_file)
        # Add assertions to validate the output

if __name__ == '__main__':
    unittest.main()