from custom_csv import CustomCSV
from student import Student
if __name__ == '__main__':

    if res := (input("would you like to add students? ['Y','N'] ").lower()) == "y":
        CustomCSV.write_to_csv_file()
    print("Here's a list of student names and addresses")
    print()
    Student.print_details(CustomCSV.read_csv_file())
