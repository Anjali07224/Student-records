import csv
import argparse

# Accept filename using argparse
parser = argparse.ArgumentParser()
parser.add_argument("--file", required=True, help="CSV file name")
args = parser.parse_args()

# Read student records
students = []

try:
    with open(args.file, "r", newline="") as file:
        reader = csv.DictReader(file)
        students = list(reader)

    # Display all student records
    print("\nAll Student Records:")
    for student in students:
        print(student)

    # Search student using roll number
    roll = input("\nEnter Roll Number to search: ")

    found = False
    for student in students:
        if student["Roll_No"] == roll:
            print("\nStudent Found:")
            print("Roll Number:", student["Roll_No"])
            print("Name:", student["Name"])
            print("Branch:", student["Branch"])
            print("Marks:", student["Marks"])
            found = True
            break

    if not found:
        print("Student not found.")

except FileNotFoundError:
    print("File not found:", args.file)
