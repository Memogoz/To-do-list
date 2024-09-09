
class Task():

    name = None
    details = None
    date = None
    priority = None
    status = None

    def __init__(self, name, details, date, priority, status):
        self.name = name
        self.details = details
        self.date = date
        self.priority = priority
        self.status = status