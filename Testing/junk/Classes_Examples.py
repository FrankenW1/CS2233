
class House:
    # foundation
    # materials
    # employees
    # color
    def __init__(self, employees, color, length=100, width=100):
        self.employees = employees
        self.color = color
        self.length = length
        self.width = width

    def __repr__(self):
        return f"<House {self.color}>"
    def square_footage(self):
        return self.length * self.width


def square_footage(length, width):
    return length * width


if __name__ == '__main__':
    # i = int(input())
    h2 = House(['dayton'], 'white', length=20)
    h = House(['josh', 'henry', 'carlos', 'dylan'], "red")
    print(h, h2)

