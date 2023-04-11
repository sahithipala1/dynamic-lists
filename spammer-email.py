import os, time

list_of_emails = []


def pretty_print():
    os.system("clear")
    print(list_of_emails)
    print()
    counter = 1
    for email in list_of_emails:
        print(f"{counter} : {email}")
        counter += 1
    time.sleep(1)


while True:
    print("SPAMMER Inc.")
    menu = input("1: Add email\n2: Remove email\n3:"
                 "show emails\n4: Get SPAMMING\n> ")

    if menu == "1":
        email = input("Email > ")
        list_of_emails.append(email)
    elif menu == "3":
        pretty_print()
    elif menu == "2":
        email = input("Email >")
        if email in list_of_emails:
            list_of_emails.remove(email)
    time.sleep(1)
    os.system("clear")
