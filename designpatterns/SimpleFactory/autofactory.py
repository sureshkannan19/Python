from inspect import getmembers,  isclass, isabstract
import autos

class AutoFactory:
    autos = {}  # Key = car model name, Value = class for the car

    def __init__(self):
        self.load_autos()

    def load_autos(self):
        if not AutoFactory.autos:
            classes = getmembers(autos, lambda m: isclass(m) and not isabstract(m))
            for name, _type in classes:
                if isclass(_type) and issubclass(_type, autos.AbsAuto):
                    car_instance = _type()
                    AutoFactory.autos[car_instance.car_name()] = car_instance

    def create_instance(self, carname):
        car = AutoFactory.autos.get(carname)
        if car is None:
            raise ValueError("Unknown car %s" % carname)
        return car