from .abs_auto import AbsAuto

class FordFusion(AbsAuto):

    def car_name(self):
        return "Fusion"

    def start(self):
        print('Cool Ford Fusion running smoothly.')

    def stop(self):
        print('Ford Fusion shutting down.')
