"""
CP1404/CP5632 Practical
Data file -> lists program
"""

"""
function main()
    data = load_data()
    display data
    display_subject_details(data)


function load_data()
    subject_list = []
    with open(FILENAME, 'r') as input_file
        for line in input_file:
            line = line.strip()
            parts = line.split(',')
            parts[2] = int(parts[2])
            subject_list.append(parts)
    return subject_list


function display_subject_details(subjects)
    for subject_code, lecturer, student_count in subjects:
        display "{subject_code} is taught by {lecturer} and has {student_count} students"

"""

FILENAME = "subject_data.txt"


def main():
    data = load_data()
    print(data)
    display_subject_details(data)


def load_data():
    subject_list = []
    with open(FILENAME, 'r') as input_file:
        for line in input_file:
            line = line.strip()
            parts = line.split(',')
            parts[2] = int(parts[2])
            subject_list.append(parts)
    return subject_list


def display_subject_details(subjects):
    for subject_code, lecturer, student_count in subjects:
        print(f"{subject_code} is taught by {lecturer} and has {student_count} students")

main()
