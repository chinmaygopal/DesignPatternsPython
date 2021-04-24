from abc import ABCMeta, abstractmethod


class Installer(metaclass=ABCMeta):
    @abstractmethod
    def execute(self):
        pass


class PathSetter(Installer):

    def __init__(self, install_obj, file_path="Default Directory"):
        self.install_obj = install_obj
        self.__file_path = file_path

    def execute(self):
        self.install_obj.path_setter(self.__file_path)


class InstallSimulink(Installer):

    def __init__(self, install_obj):
        self.install_obj = install_obj

    def execute(self):
        self.install_obj.install_simulink()


class InstallUpdates(Installer):

    def __init__(self, install_obj):
        self.install_obj = install_obj

    def execute(self):
        self.install_obj.install_updates()


class MatlabInstallationWizard:

    def path_setter(self, file_path):
        print("Matlab will be installed in : ", file_path)

    def install_simulink(self):
        print("Simulink will be installed")

    def install_updates(self):
        print("Updates Will be installed")


class MatlabInstallerAgent:

    def __init__(self):
        self.__cmd_queue = []

    def collect_commands(self, cmd):
        self.__cmd_queue.append(cmd)

    def execute_commands(self):
        for each_cmd in self.__cmd_queue:
            each_cmd.execute()
        print("")


if __name__ == "__main__":
    matlab_install_obj = MatlabInstallationWizard()

    #
    path_setter_obj = PathSetter(matlab_install_obj, "D:/Matlab/")
    install_simulink_obj = InstallSimulink(matlab_install_obj)
    install_update_obj = InstallUpdates(matlab_install_obj)

    #Invoker
    installer_agent_1 = MatlabInstallerAgent()
    installer_agent_1.collect_commands(path_setter_obj)
    installer_agent_1.collect_commands(install_update_obj)
    installer_agent_1.execute_commands()

    installer_agent_2 = MatlabInstallerAgent()
    installer_agent_2.collect_commands(path_setter_obj)
    installer_agent_2.collect_commands(install_simulink_obj)
    installer_agent_2.execute_commands()

