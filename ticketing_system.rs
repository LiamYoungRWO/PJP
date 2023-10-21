pub struct Ticket {
    ticket_id: u32,
    status: Status,
    dependencies: Vec<Ticket>,
}

impl Ticket {
    pub fn new(ticket_id: u32, status: Status, dependencies: Vec<Ticket>) -> Self {
        Ticket {
            ticket_id,
            status,
            dependencies,
        }
    }

    pub fn can_close(&self) -> bool {
        if let Status::Unresolved = self.status {
            return false;
        }

        for dependent_ticket in &self.dependencies {
            if !dependent_ticket.can_close() {
                return false;
            }
        }

        true
    }
}

pub enum Status {
    Resolved,
    Unresolved,
}

fn main() {
    let ticket3 = Ticket::new(3, Status::Resolved, vec![]);
    let ticket2 = Ticket::new(2, Status::Unresolved, vec![ticket3]);
    let ticket1 = Ticket::new(1, Status::Resolved, vec![ticket2]);

    if ticket1.can_close() {
        println!("Ticket 1 can be closed.");
    } else {
        println!("Ticket 1 cannot be closed due to unresolved dependencies.");
    }
}
