import csv
from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class Student:
    name: str
    address: str

    @staticmethod
    def print_details(students):
        for student in sorted(students, key=lambda i: i['name']):
            s = Student(student['name'], student['address'])
            print(f'{s.name.title()} lives in {s.address}')


class CustomCSV:
    @staticmethod
    def write_to_csv_file(csv_file='students.csv'):
        student = {
            'name': input("name: "),
            'address': input("address: ")
        }
        with open(csv_file, "a") as file:
            writer = csv.DictWriter(file, fieldnames=['name', 'address'])
            writer.writerow(student)

    @staticmethod
    def read_csv_file(csv_file='students.csv'):
        data = []
        with open(csv_file) as file:
            for row in csv.DictReader(file):
                data.append(row)
        return data


if __name__ == '__main__':
    if res := (input("would you like to add students? ['Y','N'] ").lower()) == "y":
        CustomCSV.write_to_csv_file()
    print("Here's a list of student names and addresses")
    print()
    Student.print_details(CustomCSV.read_csv_file())
