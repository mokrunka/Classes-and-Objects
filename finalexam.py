class Box:
    def __init__(self):
        # these are attributes
        self.length = 5
        self.width = 10
        self.height = 10
        self.filled = False
    # these, plus __init__, are methods (4 total)
    def get_filled(self):
        return self.filled
    def set_filled(self, new_value):
        self.filled = new_value
    def get_volume(self):
        the_volume = self.length * self.width * self.height
        return the_volume

new_box_1 = Box(2, 4, 8)