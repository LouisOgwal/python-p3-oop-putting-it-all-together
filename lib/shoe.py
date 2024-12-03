class Shoe:
    def __init__(self, brand, size, color="Unknown"):
        self.brand = brand
        self.size = size  # Calls the setter
        self.color = color
        self.condition = "New"

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        if isinstance(value, int):
            self._size = value
        else:
            raise ValueError("size must be an integer")
    
    def cobble(self):
        self.condition = "New"
        print("Your shoe is as good as new!")