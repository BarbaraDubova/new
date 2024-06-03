def filter_students(students):
    def sr(grades):
        return sum(grades) / len(grades) if grades else 0

    return [student['name'] for student in students if sr(student['grades']) > 4]

students = [
    {'name': 'Sara', 'grades': [3, 2, 3, 4, 5, 3, 4]},
    {'name': 'Alex', 'grades': [5, 4, 3, 4, 3, 5, 5]},
    {'name': 'Ron', 'grades':  []},
    {'name': 'Shon', 'grades': [5, 4, 3, 5]},
    {'name': 'Bo', 'grades': [5, 2]},
]

filtered_students = filter_students(students)
print(filtered_students) 