class Tickets:
    flight = None
    seat = None
    source = None
    dest = None

    def __init__(self, flight, seat, source, dest):
        self.flight = flight
        self.seat = seat
        self.source = source
        self.dest = dest


def main():
    # ticket = Tickets("Vistara", "1A", "Mumbai", "Chandigarh")
    # print("Flight is : ", ticket.flight)
    # print("Source is : ", ticket.source)
    # print("Destination is : ", ticket.dest)
    # print("Seat is : ", ticket.seat)

    def UserInput():
        flight = input("Enter flight name: ")
        source = input("Enter source: ")
        dest = input("Enter destination ")
        seat = input("Enter seat number: ")

        new_ticket = Tickets(flight, seat, source, dest)
        print("Flight is : ", new_ticket.flight)
        print("Source is : ", new_ticket.source)
        print("Destination is : ", new_ticket.dest)
        print("Seat is : ", new_ticket.seat)

    UserInput()


main()
