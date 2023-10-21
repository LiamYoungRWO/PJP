class Ticket:
    def __init__(self, ticket_id, status, dependencies=None):
        self.ticket_id = ticket_id
        self.status = status  # "resolved" or "unresolved"
        self.dependencies = dependencies or []  # List of dependent tickets

def can_close_ticket(ticket):
    # Base case: if the ticket itself is unresolved, return False
    if ticket.status == "unresolved":
        return False
    
    # Recursive case: check the status of each dependent ticket
    for dependent_ticket in ticket.dependencies:
        if not can_close_ticket(dependent_ticket):
            return False

    return True

# Example usage:
ticket3 = Ticket(3, "resolved")
ticket2 = Ticket(2, "unresolved", [ticket3])
ticket1 = Ticket(1, "resolved", [ticket2])

print(can_close_ticket(ticket1))  # Expected output: False (because ticket2 is unresolved)
