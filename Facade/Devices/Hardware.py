from abc import abstractmethod


class Hardware:
    def __init__(self, output_type='dynamic'):
        self.output_type = output_type
    
    def get_info(self):
        if self.output_type == 'dynamic':
            self.get_dynamic()
        if self.output_type == 'static':
            self.get_static()

    @abstractmethod
    def get_static(self):
        pass

    @abstractmethod
    def get_dynamic(self):
        pass
