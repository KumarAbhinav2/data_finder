import abc

class FileReaderServiceInterface(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def read_file(self, file):
        pass

