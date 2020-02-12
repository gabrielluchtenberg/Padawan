from app.lib.interface import InterfaceSystem
from app.functions.car_functions import CarFunctions

appSystem = InterfaceSystem
appSystem.interface_options()
appStartSystem = CarFunctions
appStartSystem.turn_on()
