import os, time

list_of_emails = []

while True:
    print("SPAMMER Inc.")
    menu = input("1: Add email\n2: Remove email\n3:"
                 "show emails\n4: Get SPAMMING\n> ")

    if menu == "1":
        email = input("Email > ")
        list_of_emails.append(email)
    elif menu == "2":
        email = input("Email >")
        if email in list_of_emails:
            list_of_emails.remove(email)
    time.sleep(1)
    os.system("clear")
