def main():
    print("In here we are going to slice email")
    print("")

    email_input = input("Enter your email address here: ")
    (username, domain) = email_input.split("@")
    (domain, extension) = domain.split(".")

    print("Username: ", username)
    print("Domain: ", domain)
    print("Extension: ", extension)


while True:
    main()
