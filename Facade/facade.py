from turtle import title
import Facade.Devices.cpu as cpu
import os
import time
import rich
import emoji
from Facade.Devices.RAM import RAM
from Facade.Devices.OS import OS
from rich.console import Console
from uniplot import plot

console = Console()

class Facade:
    def __init__(self, mode):
        if len(mode) > 2: 
            print(emoji.emojize('we only receive 1 args right now, sorry:pinching_hand:'))
        elif mode[1] == "-h":
            self.help()
        elif mode[1] == "-cpu":
            self.cpu_monitor()
        elif mode[1] == "-cpud":
            self.cpu_monitor_dynamic()
        elif mode[1] == "-cpus":
            self.cpu_monitor_static()      
        elif mode[1] == '-ram':
            self.check_RAM()
        elif mode[1] == "-os":
            self.check_OS()
        elif mode[1] == "-rts":
            self.check_rts()
        elif mode[1] == "-cpulive":
            self.check_cpu_live()


    def help(self):
        console.print("You can use following instructions to check your PC situation, command like this:", style="bold yellow")
        console.print("")
        console.print("Jude [-args], [args] can be like", style="bold yellow")
        console.print("")
        console.print("[-cpu] check CPU", style="bold plum4")
        console.print("[-cpus] check CPU static", style="bold plum4")
        console.print("[-cpud] check CPU dynamic", style="bold plum4")
        console.print("[-dl] deep learning", style="bold plum4")
        console.print("[-rts] check is your computer is suitable for RTS", style="bold plum4")
        console.print("[-ram] check ram", style="bold plum4")
        console.print("[-os] check OS", style="bold plum4")

    def cpu_monitor(self):
        cpuinfo = cpu.CPU('static')
        cpuinfo.get_info()
        cpuinfo = cpu.CPU('dynamic')
        cpuinfo.get_info()

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

    def check_RAM(self):
        clear = lambda: os.system('clear')
        clear()
        while True:
            ram = RAM()
            print("-"*40 + "RAM INFO" + "-"*40)
            ram.get_dynamic()
            time.sleep(0.5)
            clear()
    
    def check_OS(self):
        os_instance = OS()
        os_instance.get_static()

    def check_rts(self):
        cpuinfo = cpu.CPU()
        ram = RAM()
        advices = []
        flag = 1
        if cpuinfo.get_MHz_static()[0] < 3590:
            flag = 0
            advices.append("Your CPU Max Frequency is too low for this")
        
        if cpuinfo.get_core()[1] < 4:
            flag = 0
            advices.append("Maybe you should change a mulit-core cpu for today's era?")

        if ram.check_ram_space()/ (1024*1024*1024) < 15:
             flag = 0
             advices.append("Pls buy some RAM")

        if flag:
            console.print(":face_screaming_in_fear: What a power computer!", style="bold yellow")
        else:
            console.print("Though people say, 1 fps can play, 2 fps can be fluent, 3 fps is enough for e-sports, it would be a new world if you can change your computer :clown_face:", style="bold misty_rose1")
            print()
            console.print("The reason will be:", style="italic cornflower_blue")
            print()
            for advice in advices:
                console.print(advice, style="bold plum4")

    def check_cpu_live(self):
        clear = lambda: os.system('clear')
        clear()
        cpuinfo = cpu.CPU()
        freq_list = []
        flag = 1
        count = 0
        while True:
            if flag:
                freq_list.append(cpuinfo.get_MHz_dynamic())
            if len(freq_list) > 500:
                flag = 0
                freq_list[count] = cpuinfo.get_MHz_dynamic()
                count = count + 1
                if count == 500:
                    clear()
                    count = 0
                    plot(freq_list, title="CPU Freq", lines=True, y_max =3500, y_min=1000)
                    time.sleep(0.2)

            



if __name__ == "__main__":
    print("Test")