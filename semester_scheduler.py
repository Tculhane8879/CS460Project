"""
Personal Semester Scheduler

Author:         Thomas Culhane

Description:    Greedy algorithm for assigning tasks to time slots based 
                on soft preferences and hard constraints.
"""

class Section:
    def __init__(self, days, start_time, end_time):
        self.days = days              # e.g. "MW", "TTh"
        self.start_time = start_time  # "9:00"
        self.end_time = end_time      # "10:15"

    def __repr__(self):
        return f"{self.days} {self.start_time}-{self.end_time}"

    def get_time_slots(self):
        """Return a list of slot strings this section occupies, e.g., ['M 9am', 'W 9am']"""
        days_map = {
            "M": "M", "T": "T", "W": "W", "TH": "TH", "F": "F", "SA": "SA", "SU": "SU",
            "MW": ["M", "W"], "TTh": ["T", "TH"], "TTH": ["T", "TH"],
            "MWF": ["M", "W", "F"]
        }
        import datetime

        def time_range(start, end):
            """Generate hour slot labels like '9am', '10am'"""
            fmt = "%I:%M" if ":" in start else "%I"
            s = datetime.datetime.strptime(start, fmt)
            e = datetime.datetime.strptime(end, fmt)
            result = []
            while s < e:
                label = s.strftime("%-I%p").lower() if hasattr(s, "strftime") else str(s)
                result.append(label)
                s += datetime.timedelta(hours=1)
            return result

        hours = time_range(self.start_time, self.end_time)
        section_days = days_map[self.days] if isinstance(days_map[self.days], list) else [days_map[self.days]]
        return [f"{day} {hour}" for day in section_days for hour in hours]


class Course:
    def __init__(self, name, required, sections):
        self.name = name
        self.required = required  # True = required, False = elective
        self.sections = sections  # list of Section objects

    def __repr__(self):
        return f"{self.name} ({'Required' if self.required else 'Elective'})"