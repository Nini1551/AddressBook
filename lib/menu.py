class Menu:
    def __init__(self):
        self.options = {}

    def get_menu_options(self, title: None|str = None):
        menu = f'{title}\n\n' if title else ''
        for key, option in self.options.items():
            menu += f'{key}. {option}\n'
        return menu[:-1]

    def add_option(self, key: str, lib: str, func: function):
        if key in self.options:
            raise IndexError("The key already exists in the menu.")

        self.options[key] = Option(lib, func)

    def execute_option(self, key):
        if not key in self.options:
            raise IndexError("The key doesn't exist in the menu.")

        option = self.options[key]
        option.execute()
