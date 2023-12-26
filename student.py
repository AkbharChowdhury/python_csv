from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class Student:
    name: str
    address: str

    @staticmethod
    def print_details(students):
        for student in sorted(students, key=lambda i: i['name']):
            s = Student.from_dictionary(student)
            print(f'{s.name.title()} lives in {s.address}')

    @classmethod
    def from_dictionary(cls, student):
        return cls(student['name'], student['address'])
