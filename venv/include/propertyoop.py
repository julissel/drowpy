class Robot:

    def __init__(self, power):
        self._power = power

    power = property()

    @power.setter
    def power(self, value):
        if value < 0:
            self._power = 0
        else:
            self._power = value

    @power.getter
    def power(self):
        return self._power

    @power.deleter
    def power(self):
        print("make robot useless")
        del self._power


robo = Robot(100)
print('Power of this robot = ', robo.power, sep='\n')
robo.power = -20
print('Power of this robot = ', robo.power, sep='\n')

del robo.power
