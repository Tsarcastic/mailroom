DONORS_AMT = {'example': 100, 'other': 20, 'more': 200}
DONORS_CT = {'example': 1, 'other': 2, 'more':}


def mail_room():
    """Menu Interface"""
    reply = None
    while reply is not quit:
        print("Message")
        print("1: Process a Donation & Send a Thank You")
        print("2: Create a Report")
        print("3. Quit this program")
        print("(Enter 'q' at any time to return to this menu.)")
        reply = int(input("1 or 2?"))  #Input
        if reply == 1:
            add_amount()
        if reply == 2:
            report()
        if reply == 3:
            reply = quit


def add_amount(): #Assert that DONOR is now in DONORS_AMT?
    """Adds the amount to the donor's total"""
    amount = ""
    name = input("Enter the donor's name: ")  #Input
    if name == "q":
        return
    while not amount.isdigit():
        amount = input("Enter their donation: ")  #Input
        if amount == "q":
            return
    if name in DONORS_AMT:
        DONORS_AMT[name] += amount
        donors_ct[name] += 1
    else:
        DONORS_AMT[name] = amount
        donors_ct[name] = 1
    #print_letter()


def report():
    """This will print out the report"""   
    print("\tName\t\tTimes\tAmount\tAverage")
    #for donor in DONORS_AMT:
        #print("\t{}\t\t{}\t${}\t${}".format(donor, donors_ct[donor], DONORS_AMT[donor], DONORS_AMT[donor]/donors_ct[donor] ))
    s = [(k, d[k]) for k in sorted(DONORS_AMT, key=d.get)]
#def print_letter():
    
    #This is where we'll print the letter


mail_room()