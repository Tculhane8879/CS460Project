""" Defines structure for how real SDSU courses will be modeled for my scheduler """

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
            hour_label = start.strftime("%I%p").lstrip("0").lower()
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