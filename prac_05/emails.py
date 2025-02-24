"""
Emails to Names
Estimate time: 25 minutes
Actual time: 30 minutes

This program collects user emails and extracts names from them.
Users can confirm or edit the extracted name.
Finally, the program displays the email-name pairs.
"""


def main():
    """Collect emails and names, then display the results."""
    email_to_name = {}
    email = input("Email: ").strip()

    while email:
        name = extract_name_from_email(email)
        confirmation = input(f"Is your name {name}? (Y/n) ").strip().lower()

        if confirmation not in ("", "y", "yes"):
            name = input("Name: ").strip().title()

        email_to_name[email] = name
        email = input("Email: ").strip()

    print("\nCollected Email and Name Pairs:")
    for email, name in email_to_name.items():
        print(f"{name} ({email})")


def extract_name_from_email(email):
    """Extract a user name from an email address."""
    email_username = email.split("@")[0]
    name_parts = email_username.replace("_", " ").replace(".", " ").split()
    return " ".join(name_parts).title()



main()
