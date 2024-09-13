"""import re to validate and parse email addresses.
Specifically, the re.match() function is used with a regular expression pattern to check
if the input is a valid email and to extract the user name and domain
"""

import re
from urllib.parse import urlparse


# Function to parse and display the URL parts
def parse_url(url):
    parsed_url = urlparse(url)

    print(f"\nURL: {url}")
    print(f"  Scheme: {parsed_url.scheme}")
    print(f"  Hostname: {parsed_url.hostname}")
    print(f"  Port: {parsed_url.port}")
    print(f"  Path: {parsed_url.path}")
    print(f"  Params: {parsed_url.params}")
    print(f"  Query: {parsed_url.query}")
    print(f"  Fragment: {parsed_url.fragment}")

    # Domain level analysis
    if parsed_url.hostname:
        domain_parts = parsed_url.hostname.split(".")
        domain_levels = len(domain_parts)
        print(f"  Domain Levels: {domain_levels} ({domain_parts})")


# Function to parse and display email parts
def parse_email(email):
    email_regex = r"([\w\.-]+)@([\w\.-]+)"
    match = re.match(email_regex, email)

    if match:
        user = match.group(1)
        domain = match.group(2)
        print(f"\nEmail: {email}")
        print(f"  Username: {user}")
        print(f"  Domain: {domain}")

        # Domain level analysis
        domain_parts = domain.split(".")
        domain_levels = len(domain_parts)
        print(f"  Domain Levels: {domain_levels} ({domain_parts})")
    else:
        print(f"\nInvalid email address: {email}")


# Main function to choose input type and loop until user exits
def main():
    while True:
        choice = (
            input(
                "\nWould you like to input a (1) URL or (2) Email? Enter 1 or 2 (or 'exit' to quit): "
            )
            .strip()
            .lower()
        )

        if choice == "1":
            url = input("Enter the URL: ")
            parse_url(url)
        elif choice == "2":
            email = input("Enter the email address: ")
            parse_email(email)
        elif choice == "exit":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 'exit' to quit.")


# Run the main function
if __name__ == "__main__":
    main()
