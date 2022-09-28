import Facade.Devices.cpu as cpu
import os
import time

class Facade:
    def __init__(self, mode):
        if mode[1] == "-cpud":
            self.cpu_monitor_dynamic()
        if mode[1] == "-cpus":
            self.cpu_monitor_static()      

    def cpu_monitor_dynamic(self):
        cpuinfo = cpu.CPU('dynamic')
        clear = lambda: os.system('clear')
        clear()
        while True:
            cpuinfo.get_info()
            time.sleep(0.5)
            clear()

    def cpu_monitor_static(self):
        cpuinfo = cpu.CPU('static')
        cpuinfo.get_info()



if __name__ == "__main__":
    print("Test")