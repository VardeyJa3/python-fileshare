import os
import uuid
from datetime import datetime, timedelta


def generate_unique_id():
    """
    Generate a unique ID for files or links.
    """
    return str(uuid.uuid4())


def validate_file(filename, allowed_extensions):
    """
    Check if the uploaded file has an allowed file extension.
    """
    if '.' in filename and filename.rsplit('.', 1)[1].lower() in allowed_extensions:
        return True
    return False


def calculate_expiration_date(days):
    """
    Calculate an expiration date based on the number of days from the current date.
    """
    if not days:
        return None
    return datetime.utcnow() + timedelta(days=days)


def delete_file(file_path):
    """
    Delete a file from the local storage.
    """
    try:
        os.remove(file_path)
        return True
    except FileNotFoundError:
        return False
    except Exception as e:
        print(f"Error deleting file: {e}")
        return False