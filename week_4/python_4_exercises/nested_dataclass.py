from dataclasses import dataclass

from post_init_dataclass import Person


@dataclass
class Team:
    name: str
    members: list[Person]  # mutable default, all instances of Team share the same list

    def list_all_members(self):
        for member in self.members:
            print(member.name)


p1 = Person("suriya", 20, "suriya@gmail.com")
p2 = Person("laksh", 19, "laksh@gmail.com")
# Person(name='suriya', age=20, email='suriya@gmail.com')
# Person(name='suriya', age=21, email='suriya@gmail.com')

t1 = Team("Team 1", [p1, p2])
print(t1)
# Team(name='Team 1', members=[Person(name='suriya', age=20, email='suriya@gmail.com'), Person(name='laksh', age=19, email='laksh@gmail.com')])

t1.list_all_members()
# suriya
# laksh

print()

t2 = Team("Team 2", [p2])
t2.members[0].name = "Raji"
t2.list_all_members()
# Raji

t1.list_all_members()
# suriya
# Raji    -> 'laksh' changed into 'Raji'


# to ensure each instance gets its own separate list -> field(default_factory=list) can be used
