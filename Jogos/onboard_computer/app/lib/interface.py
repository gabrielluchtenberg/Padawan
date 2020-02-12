import os
class InterfaceSystem:
    def __init__(self, interface_options, options_if_the_car_is_on):
        self.interface_options = interface_options
        self.options_if_the_car_is_on = options_if_the_car_is_on

    @staticmethod
    def interface_options():
        optionsSystem = '[ 1 ] - Jogar\n[ 2 ] - Loja\n[ 3 ] - Options'
        print(optionsSystem)
        select = input('Me: ')
        if select == '1':
            os.system('cls')
            input('oi')

    def options_if_the_car_is_on(self):
        pass
