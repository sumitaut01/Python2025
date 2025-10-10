class Singleton:
    _inst=None
    def __new__(cls):
        if not cls._inst: cls._inst=super().__new__(cls)
        return cls._inst
