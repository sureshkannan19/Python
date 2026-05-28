from .abs_auto import AbsAuto

class ChevyVolt(AbsAuto):

    def car_name(self):
        return "Chevy Volt"

    def start(self):
        print('Chevrolet Volt running with shocking power!')

    def stop(self):
        print('Chevrolet Volt shutting down.')
