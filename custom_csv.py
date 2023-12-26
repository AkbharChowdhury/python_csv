import csv
class CustomCSV:
    @staticmethod
    def write_to_csv_file(csv_file='students.csv', fields_to_write=['name', 'address']):
        if fields_to_write is None:
            fields_to_write = ['name', 'address']
        student = {
            'name': input("name: "),
            'address': input("address: ")
        }
        with open(csv_file, "a") as file:
            writer = csv.DictWriter(file, fieldnames=fields_to_write)
            writer.writerow(student)

    @staticmethod
    def read_csv_file(csv_file='students.csv'):
        data = []
        with open(csv_file) as file:
            for row in csv.DictReader(file):
                data.append(row)
        return data
