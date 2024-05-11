class UserTicket:
    flight = None
    source = None
    dest = None
    seat = None

    def __init__(self, flight, source, dest, seat):
        self.flight = flight
        self.source = source
        self.dest = dest
        self.seat = seat

