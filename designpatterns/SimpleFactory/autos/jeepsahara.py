from .abs_auto import AbsAuto

class JeepSahara(AbsAuto):

    def car_name(self):
        return "Jeep Sahara"

    def start(self):
        print('Jeep Saraha running ruggedly.')

    def stop(self):
        print('Jeep Saraha shutting down.')
