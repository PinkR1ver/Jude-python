import sys
from abc import ABC
import psutil
from Facade.utils import get_size
from Facade.Devices.Hardware import Hardware
import os
from rich.console import Console

console = Console()




class RAM(Hardware, ABC):
    def __init__(self, output_type='dynamic'):
        super().__init__(output_type)
        self.model = ''
        self.vendor = ''
        self.output_type = output_type
        self.svmem = psutil.virtual_memory()

    def get_user(self):
        console.print(f"Used Virtual Memory: {get_size(self.svmem.used)}", style="bold plum4")

    def get_all(self):
        console.print(f"All Virtual Memory: {get_size(self.svmem.total)}", style="bold plum4")

    def get_available(self):
        console.print(f"Available Virtual Memory: {get_size(self.svmem.available)}", style="bold plum4")

    def get_percentage(self):
        console.print(f"Used Virtual Memory Percentage: {self.svmem.percent}%", style="bold plum4")

    def check_ram_space(self):
        return self.svmem.total

    def get_dynamic(self):
        self.get_user()
        self.get_available()
        self.get_percentage()
        self.get_all()

    def get_static(self):
        return super().get_static()

    def kill_pids(self):
        print("-" * 40 + "PIDS" + "-" * 40)
        pids = psutil.pids()
        for pid in pids:
            p = psutil.Process(pid)
            print(p.name())
            # print('pid-%s,pname-%s' % (pid, p.name()))
            # if p.name() == 'dllhost.exe':
            #     cmd = 'taskkill /F /IM python.exe'
            #     os.system(cmd)
        print("Enter the .exe you want to kill:")
        exe_name = sys.stdin.readline().strip('\n')
        try:
            for pid in pids:
                p = psutil.Process(pid)
                # print('pid-%s,pname-%s' % (pid, p.name()))
                if p.name() == exe_name or exe_name + '.exe':
                    cmd = 'taskkill/pid ' + str(p.pid) + ' -t -f'
                    os.system(cmd)
        except ValueError as e:
            pass