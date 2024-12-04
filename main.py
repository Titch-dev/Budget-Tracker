import os

from app import app_logic
from db_build import build_database


def main():
    # Check if the database file exists
    if not os.path.exists("budget_tracker.db"):
        print("Database not found. Building the database...")
        build_database()
    else:
        print("Database already exists. Skipping build step.")

    # Run the application logic
    app_logic()


if __name__ == "__main__":
    main()
