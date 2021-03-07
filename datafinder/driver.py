"""
Data Finder:

Simple Set of Apis to extract data from source, current version does the following:
    - Read text file from the disk
    - Extract all the urls from the file
    - prints extracted urls
"""

from datafinder.settings import CHUNK_SIZE, file_name
from datafinder.services.data_reader_service import TextFileReaderService
from datafinder.controllers.extract_data import DataExtractor

from datafinder import logger
log = logger.getLogger(__name__)


def writedata(data):
    with open('output/output.txt', 'w') as f:
        for item in data:
            f.write("%s\n" % item)


def main():
    try:
        text_reader = TextFileReaderService(chunk_size=CHUNK_SIZE)
        extractor_obj = DataExtractor(text_reader)
        extractor_obj.start_extraction(file_name)
        writedata(extractor_obj.extracted_urls)
    except Exception as e:
        log.error(e)
        return "Something went wrong....", 500
    else:
        log.info("Done extracting....")



if __name__ == '__main__':
    log.info("Initialising.....")
    main()