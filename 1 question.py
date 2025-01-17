
from datetime import date, datetime

# Define a function to calculate the user's age
def calculate_age(birth_date, today):
    # Calculate the difference in years between today's date and the user's birth date
    # Subtract one if the user has not had a birthday this year
    Age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    return Age

# Define a function to check if a date is valid
def is_valid_date(date_text):
    try:
        datetime.strptime(date_text, "%d/%m/%Y")
        return True
    except ValueError:
        return False

# Define the main function
def main():
    # Get today's date
    today = date.today()

    # Prompt the user to enter their date of birth
    birth_date_str = input("Please enter your date of birth in the format dd/mm/yyyy: ")

    # Check if the input is a valid date
    if not is_valid_date(birth_date_str):
        # If the date is invalid, display an error message and exit the program
        print("Invalid date format. Please enter a valid date in the format dd/mm/yyyy.")
        return

    # Convert the date string to a date object
    birth_date = datetime.strptime(birth_date_str, "%d/%m/%Y").date()

    # Calculate the user's age
    Age = calculate_age(birth_date, today)

    # Check if today is the user's birthday
    is_birthday = today.month == birth_date.month and today.day == birth_date.day

    # Display the result
    if is_birthday:
        # If it is the user's birthday, display a birthday message
        print("Happy birthday! You are", Age, "years old today.")
    else:
        # If it is not the user's birthday, display a normal age message
        print("You are", Age, "years old.")

# Call the main function to run the program
if __name__ == "__main__":
    main()