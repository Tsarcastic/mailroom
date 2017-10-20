"""Process a donation & issue a thankyou letter or generate a report."""

DONORS_AMT = {'example': 100, 'other': 20, 'more': 200}
DONORS_CT = {'example': 1, 'other': 2, 'more': 3}


def mail_room():
    """Menu Interface."""
    reply = None
    while reply is not quit:
        print("Message")
        print("1: Process a Donation & Send a Thank You")
        print("2: Create a Report")
        print("3. Quit this program")
        print("(Enter 'q' at any time to return to this menu.)")
        reply = int(input("1 or 2?"))  # Input
        if reply == 1:
            add_amount()
        if reply == 2:
            report()
        if reply == 3:
            reply = quit


def add_amount():  # Assert that DONOR is now in DONORS_AMT?
    """Add the amount to the donor's total."""
    amount = ""
    name = input("Enter the donor's name: ")  # Input
    if name == "q":
        return
    while not amount.isdigit():
        amount = input("Enter their donation: ")  # Input
        if amount == "q":
            return
    if name in DONORS_AMT:
        DONORS_AMT[name] += int(amount)
        DONORS_CT[name] += 1
    else:
        DONORS_AMT[name] = int(amount)
        DONORS_CT[name] = 1
    print_letter()


def report():
    """Print the donor report."""
    print("\tName\t\tDonation\tTotal Amt\tAverage")
    x = sorted(DONORS_AMT, key=DONORS_AMT.get)
    for donor in x:
        print("\t{}\t\t{}\t\t${}\t\t${}".format(
            donor,
            DONORS_CT[donor],
            DONORS_AMT[donor],
            DONORS_AMT[donor] / DONORS_CT[donor]))


def print_letter(to, contribution):
    """Print the thank you letter to the donor."""
    print("""Dear Mr. or Mrs. {},
    \nThank you very much for your generous donation of ${}. It's thanks
     to people like you that we are able to continue our noble cause of
     shaving cats. Without your generous contribution even more cats
     would be living on the streets with a full coat of hair""".format(
        to, contribution))

mail_room()
