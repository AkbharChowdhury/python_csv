from dataclasses import dataclass

from custom_csv import CustomCSV


@dataclass(frozen=True, slots=True)
class Student:
    name: str
    address: str

    @staticmethod
    def print_details(students):
        for student in sorted(students, key=lambda i: i['name']):
            s = Student(student['name'], student['address'])
            print(f'{s.name.title()} lives in {s.address}')



    # lst = []
    # for row in data:
    #     if row['username'] == username and row['password'] == password:
    #         lst.append(True)
    # lst.append(False)
    # return any(lst)


if __name__ == '__main__':
    if res := (input("would you like to add students? ['Y','N'] ").lower()) == "y":
        CustomCSV.write_to_csv_file()
    print("Here's a list of student names and addresses")
    print()
    Student.print_details(CustomCSV.read_csv_file())
