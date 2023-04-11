my_agenda = []


def printList():
    print()
    for item in my_agenda:
        print(item)
    print()


while True:
    item = input("whats next on the Agenda?: ")
    my_agenda.append(item)
    printList()
