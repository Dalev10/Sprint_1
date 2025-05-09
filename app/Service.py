#@Author: Diego Alejandro Vergara Ruiz
import re
from app.Email import Email 

class Service():

    data: list
    EMAIL_REGEX = r"^[a-zA-Z0-9._%+-]+@(estudiantes\.utv\.edu\.co|utv\.edu\.co)$"


    def __init__(self, data: list = None) -> None:
        self.email = Email()
        self.data = data if data is not None else []


    def get_welcome(self) -> str:
        return "Welcome to the service of validate and manage emails!"


    def register_email(self) -> None:
        """
        Register a new email address.
        """
        address = str(input("Enter the email address: ").strip())
        valid = self.validate_email(address)
        category = self.categorize_email(address) if valid else "Unknown"
        self.email.set_address(address)
        self.email.set_category(category)
        self.email.set_valid(valid) 


    def validate_email(self, address: str) -> bool:
        """
        Validate the email address.
        """
        return bool(re.match(self.EMAIL_REGEX, address))


    def categorize_email(self, address: str) -> str:
        """
        Categorize the email address.
        """
        if "estudiantes.utv.edu.co" in address.lower():
            return "Student"
        elif "utv.edu.co" in address.lower():
            return "Professor"
        return "Unknown"


    def save_email(self) -> None:
        """
        Save the email address to the list of the dictionaries.
        """
        if self.email.get_valid():
            self.data.append({
                "address": self.email.get_address(),
                "category": self.email.get_category()
            })
            print(f"Email {self.email.get_address()} saved successfully!")
        else:
            print(f"Email {self.email.get_address()} is invalid and cannot be saved.")


    def show_emails(self) -> None:
        """
        Show all saved email addresses.
        """
        if not self.data:
            print("No emails registered.")
            return
        print("Registered emails:")
        for email in self.data:
            print(f"Email: {email['address']}, Category: {email['category']}")


    def search_email(self) -> None:
        """
        Search for an email address in the list.
        """
        search_address = str(input("Enter the email address to search: ").strip())
        found = False
        for email in self.data:
            if search_address in email["address"]:
                print(f"Email found: {email['address']}, Category: {email['category']}")
                found = True
                break
        if not found:
            print(f"Email {search_address} not found.")
