from datetime import date


class Event:

    def __init__(self, description, event_date):
        self.description = description
        self.date = event_date

    def __str__(self):
        return f"Event \"{self.description}\" at {self.date}"

    @classmethod
    def from_string(cls, user_input):
        description = extract_description(user_input)
        date = extract_date(user_input)
        return cls(description,date)


def extract_date(user_string):
    return date(2020, 4, 10)


def extract_description(user_string):
    return "New task created!"


from datetime import date

event_description = "Test task"
event_date = date.today()

event1 = Event(event_description, event_date)
event2 = Event.from_string("Todo at 14 April 2020")
print(event1, event2, sep="\n")
