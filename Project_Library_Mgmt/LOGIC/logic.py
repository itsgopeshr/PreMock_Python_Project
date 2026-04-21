from datetime import datetime
import math

class Library:
    def __init__(self):
        # Dictionary to manage book records
        self.catalog = {
            "B101": {"title": "Python Programming", "available": True},
            "B102": {"title": "Data Structures", "available": True},
            "B103": {"title": "Operating Systems", "available": True}
        }
        self.issued_records = {}

    def display_books(self):
        return self.catalog

    def issue_book(self, book_id, student_name, issue_date_str, days_allotted):
        if book_id not in self.catalog:
            return False, "Book ID does not exist."
        
        if not self.catalog[book_id]["available"]:
            return False, "Book is currently issued to someone else."

        try:
            issue_date = datetime.strptime(issue_date_str, "%Y-%m-%d")
        except ValueError:
            return False, "Invalid date format. Use YYYY-MM-DD."

        self.catalog[book_id]["available"] = False
        self.issued_records[book_id] = {
            "student_name": student_name,
            "issue_date": issue_date,
            "days_allotted": days_allotted
        }
        return True, f"Book issued successfully to {student_name}."

    def calculate_fine(self, days_overdue):
        if days_overdue <= 0:
            return 0
        
        fine = 0
        for day in range(1, days_overdue + 1):
            week_number = ((day - 1) // 7) + 1
            daily_rate = 10 * math.factorial(week_number)
            fine += daily_rate
        return fine

    def return_book(self, book_id, return_date_str):
        if book_id not in self.issued_records:
            return False, "This book was not issued or doesn't exist.", 0

        try:
            return_date = datetime.strptime(return_date_str, "%Y-%m-%d")
        except ValueError:
            return False, "Invalid date format. Use YYYY-MM-DD.", 0

        record = self.issued_records[book_id]
        issue_date = record["issue_date"]
        days_allotted = record["days_allotted"]

        actual_days_kept = (return_date - issue_date).days
        days_overdue = actual_days_kept - days_allotted

        fine_amount = self.calculate_fine(days_overdue)

        # Update dictionaries
        self.catalog[book_id]["available"] = True
        del self.issued_records[book_id]

        status_msg = "Book returned on time." if fine_amount == 0 else f"Book returned late by {days_overdue} days."
        return True, status_msg, fine_amount