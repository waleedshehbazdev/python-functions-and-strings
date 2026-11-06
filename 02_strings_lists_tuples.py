"""
PSEB DEPLOY: Python, Django & AI Bootcamp
Lecture: Week 2 - Class 1 | Topic: Strings, Lists & Tuples
Author: Waleed Shehbaz (@waleedshehbazdev)
Key concepts: quotes, indexing, slicing, immutability, f-strings,
string cleaning, split/join, lists, list methods, comprehension, tuples, unpacking.
"""


def clean_user_input(raw_text: str) -> str:
    """Trim surrounding whitespace. Args: raw text. Returns: cleaned text."""
    return raw_text.strip()


def clean_email(raw_email: str) -> str:
    """Normalize an email. Args: raw email. Returns: lowercase trimmed email."""
    return raw_email.strip().lower()


def clean_phone_number(raw_phone: str) -> str:
    """Format Pakistani mobile numbers. Args: local or 92-prefixed number. Returns: +92 format."""
    digits = "".join(character for character in raw_phone if character.isdigit())
    if digits.startswith("0092"):
        digits = digits[2:]
    if digits.startswith("92") and len(digits) == 12:
        local = digits[2:]
    elif digits.startswith("03") and len(digits) == 11:
        local = digits[1:]
    else:
        raise ValueError("Enter a valid Pakistani mobile number.")
    if len(local) != 10 or not local.startswith("3"):
        raise ValueError("Enter a valid Pakistani mobile number.")
    return f"+92 {local[:3]} {local[3:]}"


def main() -> None:
    """Run the strings, lists, and tuples lecture demonstrations."""
    print("=" * 55)
    print("             PYTHON STRINGS")
    print("=" * 55)

    single_quotes = 'Ali'
    double_quotes = "Python Programming"
    multi_line = """Welcome to PSEB DEPLOY.
Today we are learning Python fundamentals.
Our campus is in Sahiwal."""
    print(single_quotes)
    print(double_quotes)
    print(multi_line)

    print("\n--- String Indexing ---")
    language = "Python"
    print("First character:", language[0])
    print("Last character:", language[-1])
    # P  y  t  h  o  n
    # 0  1  2  3  4  5
    #-6 -5 -4 -3 -2 -1

    print("\n--- String Slicing ---")
    course = "Programming"
    print("First four:", course[:4])
    print("From index four:", course[4:])
    print("Every second:", course[::2])
    print("Reversed:", course[::-1])

    print("\n--- String Immutability ---")
    city = "Sahiwal"
    # city[0] = "X"  # Uncomment to see TypeError: strings cannot be changed in place.
    updated_city = "X" + city[1:]  # Build a new string instead.
    print("Original:", city)
    print("New string:", updated_city)

    print("\n--- Formatted Strings ---")
    student = "Muhammad Ali"
    obtained_marks = 950
    total_marks = 1100
    percentage = obtained_marks / total_marks
    print(f"{'Student Name':<20}: {student}")
    print(f"{'Obtained Marks':<20}: {obtained_marks:,.2f}")
    print(f"{'Total Marks':<20}: {total_marks:,.2f}")
    print(f"{'Percentage':<20}: {percentage:.1%}")

    print("\n--- Defensive Input Cleaning ---")
    raw_name = "   mUHAMMAD aLI   "
    print("Original:", repr(raw_name))
    print("Clean title:", raw_name.strip().title())
    print("Clean email:", clean_email("  STUDENT@GMAIL.COM  "))
    print("Phone:", clean_phone_number("0300-1234567"))
    print("Phone with country code:", clean_phone_number("923001234567"))

    print("\n--- split() and join() ---")
    csv_skills = "Python, Django, HTML, CSS, JavaScript"
    skills = [skill.strip() for skill in csv_skills.split(",")]
    print("List:", skills)
    print("Joined:", " | ".join(skills))

    print("\n" + "=" * 55)
    print("             PYTHON LISTS")
    print("=" * 55)
    students = ["Ali", "Ahmed", "Sara", "Ayesha"]
    print("Students:", students)
    print("First:", students[0], "| Last:", students[-1])
    students[1] = "Usman"
    students.append("Hassan")
    students.insert(1, "Fatima")
    print("After update, append, insert:", students)
    students.remove("Sara")
    removed = students.pop()
    print("Removed with pop:", removed)
    print("Remaining:", students, "| Count:", len(students))

    print("\n--- List Slicing and Looping ---")
    marks = [85, 90, 78, 92, 88]
    print("First three:", marks[:3])
    print("Last two:", marks[-2:])
    for index, mark in enumerate(marks, start=1):
        print(f"Student {index}: {mark}")

    print("\n--- List Comprehension ---")
    numbers = [1, 2, 3, 4, 5, 6]
    squares = [number ** 2 for number in numbers]
    high_marks = [mark for mark in marks if mark >= 80]
    print("Squares:", squares)
    print("Marks >= 80:", high_marks)

    print("\n--- Student Marks Example ---")
    student_marks = [750, 820, 900, 670, 950]
    print("Total:", f"{sum(student_marks):,}")
    print("Average:", f"{sum(student_marks) / len(student_marks):.2f}")
    student_marks.sort()
    print("Sorted marks:", student_marks)

    print("\n" + "=" * 55)
    print("             PYTHON TUPLES")
    print("=" * 55)
    profile = ("Ali", 21, "Sahiwal", "Computer Science")
    print("Profile:", profile)
    print("Name:", profile[0], "| Age:", profile[1], "| City:", profile[2])
    one_item_tuple = ("Python",)  # A comma makes this a tuple.
    print("Single-item tuple:", one_item_tuple)

    print("\n--- Tuple Unpacking ---")
    student_record = ("Ahmed", 22, "Sahiwal")
    name, age, student_city = student_record
    print(f"Name: {name} | Age: {age} | City: {student_city}")

    print("\n--- List vs Tuple ---")
    course_list = ["Python", "Django", "AI"]
    course_list[0] = "Advanced Python"  # Lists are mutable.
    course_tuple = ("Python", "Django", "AI")  # Tuples are immutable.
    print("Updated list:", course_list)
    print("Tuple:", course_tuple)
    # course_tuple[0] = "Advanced Python"  # Uncomment to see TypeError.

    print("\n--- Student Records: List of Tuples ---")
    student_records = [
        ("Ali", 850, "Sahiwal"),
        ("Sara", 920, "Lahore"),
        ("Ahmed", 780, "Multan"),
    ]
    for record_name, record_marks, record_city in student_records:
        print(f"Name: {record_name:<10} | Marks: {record_marks:<4} | City: {record_city}")

    print("\nSTRINGS, LISTS & TUPLES LECTURE COMPLETED")


if __name__ == "__main__":
    main()
