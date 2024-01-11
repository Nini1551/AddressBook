class Option:
    def __init__(self, lib: str, func: function):
        if '\n' in lib:
            raise ValueError("Lib can't contain line break.")
        self.__lib = lib
        self.__func = func

    @property
    def lib(self) -> str:
        return self.__lib

    def __str__(self):
        return f'{self.lib}'

    def __repr__(self):
        return f'<Option: lib="{self.lib} func={self.__func}">'

    def execute(self, *args, **kwargs):
        self.__func(*args, **kwargs)