import psutil
from Facade.utils import get_size


class RAM:
    def __init__(self, type='', vendor=''):
        self.type = type
        self.vendor = vendor
        self.svmem = psutil.virtual_memory()

    def get_user(self):
        print(f"Used Virtual Memory:%f: {get_size(self.svmem.used)}")

    def get_all(self):
        print(f"All Virtual Memory:%f: {get_size(self.svmem.total)}")

    def get_available(self):
        print(f"Available Virtual Memory:%f: {get_size(self.svmem.available)}")

    def get_percentage(self):
        print(f"Used Virtual Memory Percentage:%f: {self.svmem.percent}%")
