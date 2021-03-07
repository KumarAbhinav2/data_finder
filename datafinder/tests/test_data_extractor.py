
import unittest
from unittest.mock import patch, Mock, mock_open
from datafinder.services.data_reader_service import TextFileReaderService
from datafinder.controllers.extract_data import DataExtractor


class TestServices(unittest.TestCase):

    def setUp(self) -> None:
        self.reader_obj = TextFileReaderService(1024)
        self.obj = DataExtractor(self.reader_obj)
        self.input_data = 'test http://www.google.com sdkndajsdl;ds\n'
        self.expected = {'http://www.google.com'}

    def test_extract_url(self):
        ret = self.obj._extract_url(self.input_data)
        self.assertEqual(ret, ['http://www.google.com'])
        self.assertIsInstance(ret, list)

    @patch('os.path.isfile')
    @patch('builtins.open', mock_open(read_data='test http://www.google.com sdkndajsdl;ds\n'))
    def test_process_data(self, mocked_isfile):
        mocked_isfile.return_value = True
        self.reader_obj.callback = self.obj.process_data
        self.reader_obj.read_file('test.txt')
        self.assertEqual(self.obj.extracted_urls, self.expected)


if __name__ == '__main__':
        unittest.main()
