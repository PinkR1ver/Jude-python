import string
from tempfile import tempdir
import psutil
import platform
from datetime import datetime
import Facade.Devices.Hardware as Hardware

class GPU(Hardware.Hardware):
    def __init__(self, output_type="dynamic"):
        super().__init__(output_type)
    
    def get_MHz_dynamic(self):
        cpufreq = psutil.cpu_freq()
        # print(f"dynamic Frequency: {cpufreq.dynamic:.2f}Mhz")
        # print(f"Max Frequency: {cpufreq.max:.2f}Mhz")
        # print(f"Min Frequency: {cpufreq.min:.2f}Mhz")
        return cpufreq.current

    def get_usage_dynamic(self): 
        # print("CPU Usage Per Core:")
        # for i, percentage in enumerate(psutil.cpu_percent(percpu=True, interval=1)):
        #     print(f"Core {i}: {percentage}%")
        # print(f"CPU Usage: {psutil.cpu_percent()}%")
        return psutil.cpu_percent()

    def get_cpu_temp(self):
        tempFile = open("/sys/class/thermal/thermal_zone0/temp")
        cpu_temp = tempFile.read()
        tempFile.close()
        # print(str(float(cpu_temp) / 1000) + '°C' )
        return float(cpu_temp) / 1000

    def get_MHz_static(self):
        return psutil.cpu_freq().max, psutil.cpu_freq().min

    def get_core(self):
        return psutil.cpu_count(logical=False), psutil.cpu_count(logical=True)

    def get_static(self):
        core = self.get_core()
        freq = self.get_MHz_static();
        print(f"Physical cores: {core[0]}")
        print(f"Total cores: {core[1]}")
        print(f"Max Frequency: {freq[0]:.2f}Mhz")
        print(f"Min Frequency: {freq[1]:.2f}Mhz")

    def get_dynamic(self):
        print(f"dynamic Frequency: {self.get_MHz_dynamic():.2f}Mhz")
        print(f"CPU Usage: {self.get_usage_dynamic()}%")
        print(f"dynamic CPU Temp: {self.get_cpu_temp()}°C")

if __name__ == "__main__":
    cpuinfo = CPU()
    cpuinfo.get_MHz_dynamic()
    cpuinfo.get_cpu_temp()