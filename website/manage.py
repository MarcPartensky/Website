#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_project.settings")
    try:
        from django.core.management import execute_from_command_line
        from django.db import utils
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    try:
        execute_from_command_line(sys.argv)
    except utils.OperationalError as e:
        # Log the error or perform necessary actions
        print(f"OperationalError occurred: {e}")
        # Optionally, you can choose to exit the application or raise an exception to halt the execution
        # raise e  # This will re-raise the exception and halt the application
        import sys
        sys.exit(1)  # This will exit the application with an error code

