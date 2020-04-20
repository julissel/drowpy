class NoDataDescr:
    # non-data descriptor
    def __set_name__(self, owner, name):
        self.__name = name

    def __get__(self, instance, owner):
        return  "NoDataDescr __get__"


class CoordValue:
    # data-descriptor
    def __set_name__(self, owner, name):
        print(name)
        self.__name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self.__name]

    def __set__(self, instance, value):
        instance.__dict__[self.__name] = value


class Point:
    noData = NoDataDescr()

    coordX = CoordValue()
    coordY = CoordValue()

    def __init__(self, x=0, y=0):
        self.coordX = x
        self.coordY = y


pt1 = Point(1, 2)
pt2 = Point(10, 20)
print(pt1.coordX, pt1.coordY)
print(pt2.coordX, pt2.coordY)

a = Point(5, 6)

# receive result of NoDataDescr._get__
b = a.noData

# new local property noData
a.noData = "new test"
c = a.noData

print(f"value of NoDataDescr = '{b}'.")
print(f"value of new local property noData = '{c}'")
