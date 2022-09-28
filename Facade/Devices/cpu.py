import psutil
import platform
from datetime import datetime

class CPU:
    def getHz():
        cpufreq = psutil.cpu_freq()
        print(f"Current Frequency: {cpufreq.current:.2f}Mhz")

if __name__ == "__main__":
    CPU.getHz()