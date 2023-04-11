my_agenda = []


def printList():
    print()
    for item in my_agenda:
        print(item)
    print()


while True:
    menu = input("Add or Remove?: ")
    if menu == "add":
        item = input("whats next on the Agenda?: ")
        my_agenda.append(item)
    elif menu == "remove":
        item = input("What do you want to remove?")
        if item in my_agenda:
            my_agenda.remove(item)
        else:
            print(f"{item} was not int he list")
    printList()
