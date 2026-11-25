
import re
import os

def extract_emails():
    # Read input file
    with open("input.txt", "r") as file:
        text = file.read()

    if not text.strip():
        print("\nInput file is empty!")
        return

    # Extract email addresses
    emails = re.findall(
        r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}',
        text
    )

    # Remove duplicates and sort
    emails = sorted(set(emails))

    if len(emails) == 0:
        print("\nNo email addresses found!")
        return

    # Display emails
    print("\nExtracted Email Addresses:")
    print("-" * 40)

    for number, email in enumerate(emails, start=1):
        print(f"{number}. {email}")

    # Save emails
    with open("output.txt", "w") as file:
        for email in emails:
            file.write(email + "\n")

    print("-" * 40)
    print("Total Emails Found:", len(emails))
    print("Emails saved successfully!")


def view_emails():
    if not os.path.exists("output.txt"):
        print("\nNo saved email file found!")
        return

    with open("output.txt", "r") as file:
        emails = file.read()

    if not emails.strip():
        print("\nNo saved emails available!")
    else:
        print("\nSaved Email Addresses:")
        print("-" * 40)
        print(emails)


def count_emails():
    if not os.path.exists("output.txt"):
        print("\nNo saved email file found!")
        return

    with open("output.txt", "r") as file:
        emails = file.readlines()

    print("\nTotal Saved Email Addresses:", len(emails))


# Main menu
while True:
    print("\n" + "=" * 40)
    print("       EMAIL ADDRESS EXTRACTOR")
    print("=" * 40)

    print("\n1. Extract Email Addresses")
    print("2. View Saved Email Addresses")
    print("3. Count Email Addresses")
    print("4. Exit")

    choice = input("\nEnter your choice (1-4): ")

    if choice == "1":
        extract_emails()

    elif choice == "2":
        view_emails()

    elif choice == "3":
        count_emails()

    elif choice == "4":
        print("\nThank you for using Email Extractor!")
        break

    else:
        print("\nInvalid choice! Please enter 1, 2, 3 or 4.")
