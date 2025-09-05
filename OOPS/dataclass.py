from dataclasses import dataclass
from typing import Optional


@dataclass(slots=True)
class Project:
    name: str
    payment: int
    client: str
    description: Optional[str] = None

    def notify_client(self):
        print("Notifying client...")

class Developer:
    def __init__(self, name, skill, project):
        self.name = name
        self.skill = skill
        self.project = project

p = Project("Python App", 500000, "SK", "Python app build by SK")
dev = Developer("SK", "Programmer", p)

print(dev.project)
print(dev.project.notify_client())