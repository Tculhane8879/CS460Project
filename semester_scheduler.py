"""
Personal Semester Scheduler

Author:         Thomas Culhane

Description:    Greedy algorithm for assigning tasks to time slots based 
                on soft preferences and hard constraints.
"""

class Section:
    def __init__(self, days, start_time, end_time):
        self.days = days              # e.g. "MW", "TTh"
        self.start_time = start_time  # e.g. "9:00"
        self.end_time = end_time      # e.g. "10:15"

    def __repr__(self):
        return f"{self.days} {self.start_time}-{self.end_time}"

    def get_time_slots(self):
        """Return list of time slots (e.g., ['M 9am', 'W 9am']) for this section."""
        import datetime

        days_map = {
            "M": ["M"], "T": ["T"], "W": ["W"], "TH": ["TH"],
            "F": ["F"], "SA": ["SA"], "SU": ["SU"],
            "MW": ["M", "W"], "TTh": ["T", "TH"], "MWF": ["M", "W", "F"]
        }

        # Convert time string to hour integers
        def parse_time(tstr):
            return datetime.datetime.strptime(tstr, "%I:%M" if ":" in tstr else "%I")

        start = parse_time(self.start_time)
        end = parse_time(self.end_time)
        hour_range = []
        while start < end:
            hour_label = start.strftime("%-I%p").lower()
            hour_range.append(hour_label)
            start += datetime.timedelta(hours=1)

        return [f"{day} {hour}" for day in days_map[self.days] for hour in hour_range]


class Course:
    def __init__(self, name, required, sections):
        self.name = name
        self.required = required  # True = required, False = elective
        self.sections = sections  # list of Section objects

    def __repr__(self):
        return f"{self.name} ({'Required' if self.required else 'Elective'})"
    
# all time slots tasks can be assigned to
time_slots = [
    "M 7am", "M 8am", "M 9am", "M 10am", "M 11am", "M 12pm", "M 1pm", "M 2pm", "M 3pm", 
    "M 4pm", "M 5pm", "M 6pm", "M 7pm", "M 8pm", "M 9pm", "M 10pm", "M 11pm", "M 12am",
    "T 7am", "T 8am", "T 9am", "T 10am", "T 11am", "T 12pm", "T 1pm", "T 2pm", "T 3pm", 
    "T 4pm", "T 5pm", "T 6pm", "T 7pm", "T 8pm", "T 9pm", "T 10pm", "T 11pm", "T 12am",
    "W 7am", "W 8am", "W 9am", "W 10am", "W 11am", "W 12pm", "W 1pm", "W 2pm", "W 3pm", 
    "W 4pm", "W 5pm", "W 6pm", "W 7pm", "W 8pm", "W 9pm", "W 10pm", "W 11pm", "W 12am",
    "TH 7am", "TH 8am", "TH 9am", "TH 10am", "TH 11am", "TH 12pm", "TH 1pm", "TH 2pm", "TH 3pm", 
    "TH 4pm", "TH 5pm", "TH 6pm", "TH 7pm", "TH 8pm", "TH 9pm", "TH 10pm", "TH 11pm", "TH 12am",
    "F 7am", "F 8am", "F 9am", "F 10am", "F 11am", "F 12pm", "F 1pm", "F 2pm", "F 3pm", 
    "F 4pm", "F 5pm", "F 6pm", "F 7pm", "F 8pm", "F 9pm", "F 10pm", "F 11pm", "F 12am",
    "SA 7am", "SA 8am", "SA 9am", "SA 10am", "SA 11am", "SA 12pm", "SA 1pm", "SA 2pm", "SA 3pm", 
    "SA 4pm", "SA 5pm", "SA 6pm", "SA 7pm", "SA 8pm", "SA 9pm", "SA 10pm", "SA 11pm", "SA 12am",
    "SU 7am", "SU 8am", "SU 9am", "SU 10am", "SU 11am", "SU 12pm", "SU 1pm", "SU 2pm", "SU 3pm", 
    "SU 4pm", "SU 5pm", "SU 6pm", "SU 7pm", "SU 8pm", "SU 9pm", "SU 10pm", "SU 11pm", "SU 12am",
]

