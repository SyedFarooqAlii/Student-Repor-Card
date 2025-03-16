import csv

# def calculate_grade(percentage):
#     if percentage >= 80:
#         return 'A+'
#     elif percentage >= 70:
#         return 'A'
#     elif percentage >= 60:
#         return 'B'
#     elif percentage >= 50:
#         return 'C'
#     else:
#         return 'F'
def calculate_grade(percentage):
     if percentage>= 80:
         return 'A+'
     elif percentage>=70:
         return 'A'
     elif percentage>=60:
         return 'B'
     elif percentage>=50:
         return 'C'
     else:
         return 'F'


def generate_report_card(student):
    total_marks = sum(student['marks'].values())
    percentage = (total_marks / 500) * 100
    grade = calculate_grade(percentage)
    
    print("\nReport Card")
    print("-" * 40)
    print(f"Name: {student['name']}")
    print(f"Roll Number: {student['roll_no']}")
    print("Subjects and Marks:")
    for subject, marks in student['marks'].items():
        print(f"{subject}: {marks}")
    print(f"Total Marks: {total_marks}/500")
    print(f"Percentage: {percentage:.2f}%")
    print(f"Grade: {grade}")
    print("-" * 40)
    
    return [student['name'], student['roll_no'], total_marks, percentage, grade]

def save_to_csv(students):
    with open('student_report_cards.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Roll Number", "Total Marks", "Percentage", "Grade"])
        for student in students:
            writer.writerow(generate_report_card(student))

def main():
    students = []
    subjects = ['Math', 'Physics', 'Urdu', 'English', 'Computer']
    
    while True:
        student = {}
        student['name'] = input("Enter Student Name: ")
        student['roll_no'] = input("Enter Roll Number: ")
        student['marks'] = {}
        
        for subject in subjects:
            while True:
                try:
                    marks = int(input(f"Enter marks for {subject} (0-100): "))
                    if 0 <= marks <= 100:
                        student['marks'][subject] = marks
                        break
                    else:
                        print("Marks should be between 0 and 100. Try again.")
                except ValueError:
                    print("Invalid input! Please enter a number between 0 and 100.")
        
        students.append(student)
        print(f"\nRecord of {student['name']} inserted successfully.")
        
        while True:
            more = input("Do you want to insert more? (Y/N): ").strip().lower()
            if more in ['y', 'n']:
                break
            else:
                print("Invalid choice! Please enter 'Y' or 'N'.")
        
        if more == 'n':
            break
    
    print("\nFinal Report Cards:")
    for student in students:
        generate_report_card(student)
    
    save_to_csv(students)
    print("\nAll report cards have been saved to 'student_report_cards.csv'.")

if __name__ == "__main__":
    main()
