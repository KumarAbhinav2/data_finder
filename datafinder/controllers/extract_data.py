import re
from datafinder.settings import PATTERN

from datafinder import logger
log = logger.getLogger(__name__)


class DataExtractor:
    """
    Data Extractor

    Attributes:
    -----------
    data_reader:object
        data_reader service object
    extracted_urls: list
        container for extracted urls
    """

    def __init__(self, data_reader):
        self.data_reader = data_reader
        self.extracted_urls = set()

    @staticmethod
    def _extract_url(string):
        """
        a regex based simple function to get matching url from string
        :param string: input line
        :return: list of urls
        """
        #log.info("Extracting the urls from the data...")
        pattern = re.compile(PATTERN)
        url = pattern.findall(string)
        return [x[0] for x in url]

    def process_data(self, data, eof):
        """
        :param data: str: input line
        :param eof: boolean: flag to check the end of file
        :return: list: extrated list of urls
        """
        if not eof:
            url = self._extract_url(data)
            if url:
                self.extracted_urls.update(set(url))
        else:
            return self.extracted_urls

    def start_extraction(self, file_name):
        """
        Initiation point...
        :param file_name: str: full file name
        :return:
        """
        self.data_reader.callback = self.process_data
        self.data_reader.read_file(file_name)