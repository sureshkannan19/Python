from dataclasses import dataclass


def add_speech(cls):
    cls.speak = lambda self: f"Hello, I'm a {self.__class__.__name__} instance"
    return cls


@add_speech
@dataclass(slots=True)
class UserDetails:
    username: str
    role: str


obj = UserDetails('Jim', 'Administrator')
print(obj.speak())
