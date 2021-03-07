import os
from datafinder.services.data_reader_interface import FileReaderServiceInterface
from datafinder import logger
log = logger.getLogger(__name__)


class TextFileReaderService(FileReaderServiceInterface):
    """
    Text File Reader Service

    Attributes:
    ----------
    chunk_size: int
        integer value to represent chunk size
    callback: object
        function object
    """

    def __init__(self, chunk_size):
        self.chunk_size = chunk_size
        self.callback = None

    def _read_chunks(self, f):
        """
        :param f: file or file like object
        :param chunk_size: size of chunk to be read
        :return:
        """
        while True:
            log.info("reading the chunks....")
            data = f.read(self.chunk_size)
            log.info("finished reading ")
            if not data:
                break
            yield data

    @staticmethod
    def _file_check(file_name):
        return os.path.isfile(file_name)

    def _read_file(self, file_name, callback):
        """
        simple line by line file read function
        :param file_name: str(file to be read)
        :param callback: callback method
        :return:
        """
        log.info(f'Started reading {file_name}....')
        f_handle = open(file_name)
        rem_data = None

        log.info(f'Reading through the chunks of size {self.chunk_size} bytes')
        no_chunks = 0
        for chunk in self._read_chunks(f_handle):
            if rem_data:
                current_chunk = rem_data + chunk
            else:
                current_chunk = chunk
            lines = current_chunk.splitlines()
            if current_chunk.endswith('\n'):
                rem_data = None
            else:
                rem_data = lines.pop()
            for line in lines:
                callback(data=line, eof=False)
            no_chunks+=1
            log.info(f"Current chunk count {no_chunks}")
        log.info(f"Total chunks read...{no_chunks}")

        if rem_data:
            current_chunk = rem_data
            if current_chunk:
                lines = current_chunk.splitlines()
                for line in lines:
                    callback(data=line, eof=False)
                    pass
        callback(data=None, eof=True)
        log.info("Done with file reading...")

    def read_file(self, file_name):
        """
        :param file_name: string
        :return:
        """
        log.info("Preparing to read the content.....")
        if not self._file_check(file_name):
            raise FileNotFoundError
        self._read_file(file_name, self.callback)

