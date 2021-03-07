import io
import unittest
from datafinder import logger
from unittest.mock import patch, Mock, mock_open
from datafinder.services.data_reader_service import TextFileReaderService


class TestServices(unittest.TestCase):

    def setUp(self) -> None:
        self.obj = TextFileReaderService(1024)
        self.testfile = '../URLS-200.txt'

    @patch.object(TextFileReaderService, '_read_file')
    def test_read_file(self, mocked):
        self.obj.read_file(self.testfile)
        mocked.assert_called_once()

    @patch('os.path.isfile')
    @patch('builtins.open', mock_open(read_data='test'))
    def test_read_file_protected(self, mock_isfile):
        mock_isfile.return_value = True
        self.obj.callback = Mock(return_value = 'test')
        self.obj.read_file('test.txt')
        self.assertEqual(self.obj.callback.call_count, 2)

    def test_read_chunks(self):
        fake_file = io.StringIO('test')
        self.obj._read_chunks(fake_file)
        self.assertLogs(logger.getLogger('test'), 'info')


if __name__ == '__main__':
        unittest.main()
