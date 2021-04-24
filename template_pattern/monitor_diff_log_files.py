from abc import ABCMeta, abstractmethod


class BiometricIdentifier(metaclass=ABCMeta):
    @abstractmethod
    def capture_biometric(self):
        pass

    @abstractmethod
    def process_biometric(self):
        pass

    @abstractmethod
    def save_biometric_db(self):
        pass

    @abstractmethod
    def display_report(self):
        pass

    def biometric_identification(self):
        self.capture_biometric()
        self.process_biometric()
        self.save_biometric_db()
        self.display_report()


class IrisBasedBiometry(BiometricIdentifier):

    def __init__(self):
        self.__biometric_data = 0

    def capture_biometric(self):
        print("Iris image captured")

    def process_biometric(self):
        print("Segmentation Done")
        print("Normalization Done")
        print("Feature Encoding Done\n")
        self.__biometric_data = 123

    def save_biometric_db(self):
        print("Saved Iris data\n")

    def display_report(self):
        print("Your Iris Scan has been successfully registered\n")


iris_scan_obj = IrisBasedBiometry()
iris_scan_obj.biometric_identification()
