import platform
import Facade.Devices.Hardware as Hardware

from rich.console import Console

console = Console()

class OS(Hardware.Hardware):
    def __init__(self, output_type='static'):
        super().__init__(output_type)
        self.type = ''
        self.vendor_name = ''
        self.version = ''
        self.unanme = platform.uname()

    def get_system(self):
        console.print(f"System: {self.unanme.system}", style="bold plum4")

    def get_version(self):
        self.version = self.unanme.version
        console.print(f"Version: {self.unanme.version}", style="bold plum4")

    def get_release(self):
        console.print(f"Release: {self.unanme.release}", style="bold plum4")

    def get_machine(self):
        console.print(f"Machine: {self.unanme.machine}", style="bold plum4")

    def get_processor(self):
        console.print(f"Processor: {self.unanme.processor}", style="bold plum4")

    def get_static(self):
        self.get_system()
        self.get_version()
        self.get_release()
        self.get_machine()
        self.get_processor()

    def get__dynamic(self):
        return super().get_static()