from dataclasses import dataclass, field


@dataclass
class Student:
    name: str
    roll: int
    grades: list[float] = field(default_factory=list)
    # call the factory function each time a new instance is created

    def avg_grade(self):
        if not self.grades:
            return 0.0
        return round((sum(self.grades) / len(self.grades)), 2)


s1 = Student("laksh", 101)
s2 = Student("Arav", 102, [90, 80, 95])

print(s1.avg_grade())  # 0.0
print(s2.avg_grade())  # 88.33
