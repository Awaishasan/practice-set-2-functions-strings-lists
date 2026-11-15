# Task 1: Student Result Card Generator
# Topics: Functions (def, parameters, return) and String Manipulation

SUBJECTS = ["English", "Math", "Physics", "Chemistry", "Urdu"]
MAX_MARKS_PER_SUBJECT = 100


def format_name(name):
    """Clean the student's name using .strip() and .title()."""
    return name.strip().title()


def get_valid_marks(subject):
    """Ask for marks in one subject and validate them (0 to 100)."""
    while True:
        marks = input(f"Enter marks in {subject} (0-100): ").strip()
        if not marks.isdigit():
            print("Invalid input! Marks must be a number.")
            continue
        marks = int(marks)
        if marks < 0 or marks > 100:
            print("Invalid marks! Marks must be between 0 and 100.")
            continue
        return marks


def calculate_percentage(total, max_total):
    """Return the percentage for total marks out of max_total."""
    return (total / max_total) * 100


def get_grade(percentage):
    """Return the grade for a percentage."""
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    else:
        return "Fail"


def main():
    name = format_name(input("Enter student name: "))
    while not name:
        print("Name cannot be empty!")
        name = format_name(input("Enter student name: "))

    while True:
        roll_number = input("Enter roll number: ").strip()
        if roll_number.isdigit():
            break
        print("Invalid roll number! Roll number must contain digits only.")

    marks_list = []
    for subject in SUBJECTS:
        marks_list.append(get_valid_marks(subject))

    total = sum(marks_list)
    max_total = MAX_MARKS_PER_SUBJECT * len(SUBJECTS)
    percentage = calculate_percentage(total, max_total)
    grade = get_grade(percentage)

    # If any subject mark is below 40, the final result is Fail,
    # regardless of the overall percentage.
    if any(marks < 40 for marks in marks_list):
        result = "Fail"
    else:
        result = "Pass" if percentage >= 50 else "Fail"

    print("---------------------------------")
    print("       STUDENT RESULT CARD")
    print("---------------------------------")
    print(f"Name: {name}")
    print(f"Roll Number: {roll_number}")
    print("---------------------------------")
    for subject, marks in zip(SUBJECTS, marks_list):
        print(f"{subject}: {marks}")
    print("---------------------------------")
    print(f"Total Marks: {total} / {max_total}")
    print(f"Percentage: {percentage:.2f}%")
    print(f"Grade: {grade}")
    print(f"Result: {result}")
    print("---------------------------------")


if __name__ == "__main__":
    main()
