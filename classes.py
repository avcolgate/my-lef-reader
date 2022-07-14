class Macro:
    def __init__(self, name=''):
        self.name = name
        self.class_type = 'None'
        self.size = {0, 0}
        self.symmetry = 'None'
        self.pins = []


class Pin:
    def __init__(self, name=''):
        self.name = name
        self.direction = 'None'
        self.layers = []
