import Facade.Devices.cpu as cpu

class Facade:
    def __init__(self, mode):
        if mode == "-cpufreq":
            self.check(mode)

    def check(self, argv):
        if argv == "-cpufreq":
            cpu.CPU.getHz()




if __name__ == "__main__":
    print("Test")