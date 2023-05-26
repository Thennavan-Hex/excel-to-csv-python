import csv

def print_csv_file(filename):
    with open(filename, 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            print(row)

filename = "output.csv" #enter your csv output file name
print_csv_file(filename)

