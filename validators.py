import re
from datetime import datetime, date


def validate_email(email):
    """Validate email format."""
    pattern = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"

    if re.match(pattern, email):
        return True, ""

    return False, "Invalid email address format."


def validate_date_of_birth(dob_text):
    """
    Expected format: dd.mm.yyyy
    Converts valid DOB to dd/mm/yyyy format.
    """

    try:
        dob = datetime.strptime(dob_text, "%d.%m.%Y").date()

        if dob > date.today():
            return False, None, "Date of birth cannot be in the future."

        return True, dob.strftime("%d/%m/%Y"), ""

    except ValueError:
        return False, None, (
            "Invalid date of birth. "
            "Please use a valid date in dd.mm.yyyy format."
        )


def validate_blood_value(value, field_name):
    """Validate that a blood test value is numeric."""

    try:
        number = float(value)

        if number < 0:
            return False, None, f"{field_name} cannot be negative."

        return True, number, ""

    except (ValueError, TypeError):
        return False, None, f"{field_name} must be numeric."