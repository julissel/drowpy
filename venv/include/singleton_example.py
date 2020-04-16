class Singleton:
    isinstance = None

    def __new__(cls):
        if cls.isinstance is None:
            cls.isinstance = super().__new__(cls)

        return cls.isinstance


first_obj = Singleton()
second_obj = Singleton()

print(first_obj is second_obj)
