"""
PSEB DEPLOY: Python, Django & AI Bootcamp
Lecture: Week 2 - Class 1 | Topic: Python Functions Fundamentals
Author: Waleed Shehbaz (@waleedshehbazdev)
Key concepts: functions, parameters, arguments, defaults, print vs return,
scope, *args, **kwargs, validation, reusable function design.
"""


def print_banner() -> None:
    """Display the bootcamp welcome banner."""
    print("=" * 55)
    print("       PSEB DEPLOY - PYTHON BOOTCAMP")
    print("       Functions & Programming Fundamentals")
    print("=" * 55)


def greet_student(name: str, city: str = "Sahiwal") -> None:
    """Display a welcome message. Args: name and optional city. Returns: None."""
    print(f"Welcome {name}! Greetings from {city}.")


def calculate_percentage(obtained_marks: float, total_marks: float = 1100.0) -> float:
    """Calculate and return percentage. Args: obtained and total marks. Returns: percentage."""
    if total_marks <= 0:
        raise ValueError("Total marks must be greater than zero.")
    if not 0 <= obtained_marks <= total_marks:
        raise ValueError("Obtained marks must be within the valid range.")
    return (obtained_marks / total_marks) * 100


def get_grade(percentage: float) -> str:
    """Return a grade for a percentage. Args: percentage. Returns: grade label."""
    if not 0 <= percentage <= 100:
        raise ValueError("Percentage must be between 0 and 100.")
    if percentage >= 80:
        return "A-1"
    if percentage >= 70:
        return "A"
    if percentage >= 60:
        return "B"
    if percentage >= 50:
        return "C"
    return "F"


# Global scope: available throughout this module.
campus_name = "Sahiwal Campus"


def show_campus_information() -> None:
    """Show global campus_name and a function-local classroom variable."""
    classroom = "Python Lab"  # Local scope: available only inside this function.
    print(f"Campus: {campus_name}")
    print(f"Classroom: {classroom}")


def calculate_total_expenses(*amounts: float) -> float:
    """Add any number of expenses. Args: variable expense amounts. Returns: total."""
    if any(amount < 0 for amount in amounts):
        raise ValueError("Expense amounts cannot be negative.")
    return sum(amounts)


def register_student(student_id: int, name: str, **extra_details: object) -> None:
    """Display a student profile. Args: ID, name, and extra keyword metadata. Returns: None."""
    print(f"Student ID: {student_id}")
    print(f"Name: {name}")
    for key, value in extra_details.items():
        print(f"{key.replace('_', ' ').title()}: {value}")


def apply_canteen_discount(bill_amount: float, is_student: bool = True) -> float:
    """Return a PKR bill after a 10% student discount. Args: bill and student status."""
    if bill_amount < 0:
        raise ValueError("Bill amount cannot be negative.")
    discount = bill_amount * 0.10 if is_student else 0.0
    return bill_amount - discount


def get_student_name() -> str:
    """Return a sample student name. Returns: student name."""
    return "Ahmed Khan"


def calculate_student_bill(price: float, quantity: int) -> float:
    """Calculate item cost. Args: unit price and quantity. Returns: total in PKR."""
    if price < 0 or quantity < 0:
        raise ValueError("Price and quantity cannot be negative.")
    return price * quantity


def display_student_bill(name: str, total: float) -> None:
    """Print a student bill. Args: student name and total amount. Returns: None."""
    print(f"Student: {name}")
    print(f"Total Bill: PKR {total:,.2f}")


if __name__ == "__main__":
    print_banner()
    print("\n--- Student Greetings ---")
    greet_student("Ali")
    greet_student("Ahmed", "Lahore")

    print("\n--- Matric / FSc Result ---")
    marks = 950
    percentage = calculate_percentage(marks)
    print(f"Obtained Marks: {marks}/1100")
    print(f"Percentage: {percentage:.2f}%")
    print(f"Grade: {get_grade(percentage)}")

    print("\n--- print() vs return ---")
    # print() displays a value; return sends a value back for reuse.
    reusable_result = calculate_percentage(950)
    print(f"Returned value reused in another calculation: {get_grade(reusable_result)}")

    print("\n--- Local vs Global Scope ---")
    show_campus_information()

    print("\n--- Student Monthly Expenses ---")
    expenses = calculate_total_expenses(500, 2500, 1500, 300)
    print(f"Total Expenses: PKR {expenses:,.2f}")

    print("\n--- Student Registration (**kwargs) ---")
    register_student(101, "Muhammad Ali", city="Sahiwal", course="Python", university="University of Sahiwal")

    print("\n--- Campus Canteen Bill ---")
    original_bill = 1200
    final_bill = apply_canteen_discount(original_bill)
    print(f"Original: PKR {original_bill:,.2f}")
    print("Student Discount: 10%")
    print(f"Final: PKR {final_bill:,.2f}")

    print("\n--- Single Responsibility Function Design ---")
    display_student_bill(get_student_name(), calculate_student_bill(250, 3))
    print("\nFUNCTIONS LECTURE COMPLETED")
