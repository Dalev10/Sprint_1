#@Author: Diego Alejandro Vergara Ruiz
 
from app.Service import Service

"""
This is a simple console application that allows you to register, 
validate and manage email addresses of both students and professors (Belonging to a ficticious institution).

For the development of this program, was used OOP (Object Oriented Programming), 
The Single Responsibility Principle (SRP), and the style guide for python code (PEP 8).

"""

def main():
    service = Service()
    print(service.get_welcome())

    while True:

        option = int(input("Select an option:\n1. Register Email\n2. Show Emails\n3. Search Email\n4. Exit\n"))

        if option == 1:
            service.register_email()
            service.save_email()
        elif option == 2:
            service.show_emails()
        elif option == 3:
            service.search_email()
        elif option == 4:
            print("Exiting the program.")
            break
        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()