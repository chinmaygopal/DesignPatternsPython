import abc


class IDecryptFile:
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def decrypt_log_file(self, file_path):
        pass


class DecryptTimFile(IDecryptFile):
    def decrypt_log_file(self, file_path):
        print("Decrypted Tim File")


class DecryptXMLFile(IDecryptFile):
    def decrypt_log_file(self, file_path):
        print("Decrypted XML File")


class DecryptCSVFile(IDecryptFile):
    def decrypt_log_file(self, file_path):
        print("Decrypted CSV File")


class LogFile:
    def __init__(self, file_path, file_type):
        self.__file_path = file_path
        self.__file_type = file_type
        pass

    def decrypt_log_file(self):
        self.__file_type.decrypt_log_file(self.__file_path)


class AnalysisForTimFiles(LogFile):
    def __init__(self):
        decrypt_for_tim = DecryptTimFile()
        file_path = "string for path"
        super(AnalysisForTimFiles, self).__init__(file_path, decrypt_for_tim)


file_read = AnalysisForTimFiles()
file_read.decrypt_log_file()