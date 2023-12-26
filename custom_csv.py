import csv


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
