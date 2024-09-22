class Horse:
    def __init__(self):
        self.x_distance = 0
        self.sound = 'Frrr'
    
    def run(self, dx):
        self.x_distance += dx


class Eagle:
    def __init__(self):
        self.y_distance = 0
        self.sound = 'I train, eat, sleep, and repeat'

    def fly(self, dy):
        self.y_distance += dy


class Pegasus(Horse, Eagle):
    def __init__(self):
        Horse.__init__(self)
        Eagle.__init__(self)

    def move(self, dx, dy):
        self.run(dx)
        self.fly(dy)

    def get_pos(self):
        return (self.x_distance, self.y_distance)

    def voice(self):
        print(self.sound)


# Создание объекта класса Pegasus и тестирование методов
p1 = Pegasus()

print(p1.get_pos())  # Вывод: (0, 0)
p1.move(10, 15)
print(p1.get_pos())  # Вывод: (10, 15)
p1.move(-5, 20)
print(p1.get_pos())  # Вывод: (5, 35)

p1.voice()  # Вывод: I train, eat, sleep, and repeat