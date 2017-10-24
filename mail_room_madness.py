"""Process a donation & issue a thank you letter or generate a report."""

DONORS_AMT = {'example': 100, 'other': 20, 'more': 200}
DONORS_CT = {'example': 1, 'other': 2, 'more': 3}


def main():  # pragma: no cover
    """Menu Interface. Input required."""
    reply = None
    while reply is not quit:
        print("Message")
        print("1: Process a Donation & Send a Thank You")
        print("2: Create a Report")
        print("3. Quit this program")
        print("(Enter 'q' at any time to return to this menu.)")
        reply = int(input("1, 2, or 3?"))  # Input
        if reply == 1:
            name, amount = receive_donation()
            add_amount(name, amount)
            print(write_letter(name, amount))
        if reply == 2:
            print_report()
        if reply == 3:
            reply = quit


def receive_donation():  # pragma: no cover
    """Receive new donation. Input required."""
    amount = ""
    name = input("Enter the donor's name: ")  # Input
    if name == "q":
        return
    while not amount.isdigit():
        amount = input("Enter their donation: ")  # Input
        if amount == "q":
            return
    return name, amount


def add_amount(donor, donation):
    """Add the [amount] to the [donor]'s total."""
    if donor in DONORS_AMT:
        DONORS_AMT[donor] += int(donation)
        DONORS_CT[donor] += 1
    else:
        DONORS_AMT[donor] = int(donation)
        DONORS_CT[donor] = 1


def sort_report():
    """Sort the DONORS_LIST by the DONORS_AMT."""
    print("\tName\t\tDonation\tTotal Amt\tAverage")
    sorted_list = sorted(DONORS_AMT, key=DONORS_AMT.get)
    return sorted_list


def print_report():
    """Print the sorted donor list."""
    x = sort_report()
    for donor in x:
        print("\t{}\t\t{}\t\t${}\t\t${}".format(
            donor,
            DONORS_CT[donor],
            DONORS_AMT[donor],
            DONORS_AMT[donor] / DONORS_CT[donor]))


def write_letter(letter_to, contribution):
    """Print the thank you letter to the donor."""
    letter = """Dear Mr. or Mrs. {},
    \n\tThank you very much for your generous donation of ${}. It's
        thanks to people like you that we are able to continue our noble
        cause of shaving the homeless. Without your generous contribution
        even more homeless people would be living on the streets with a
        full set of whiskers.\n""".format(
        letter_to, contribution)
    return letter

if __name__ == '__main__':
    main()
