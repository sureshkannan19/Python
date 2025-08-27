from dataclasses import dataclass

@dataclass(slots=True)
class Project:
    name: str
    payment: int
    client: str

    def notify_client(self):
        print("Notifying client...")

class Developer:
    def __init__(self, name, skill, project):
        self.name = name
        self.skill = skill
        self.project = project

p = Project("Python App", 500000, "SK")
dev = Developer("SK", "Programmer", p)

print(dev.project.notify_client())