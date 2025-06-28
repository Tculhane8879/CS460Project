"""
Personal Semester Scheduler

Author:         Thomas Culhane

Description:    Greedy algorithm for assigning tasks to time slots based 
                on soft preferences and hard constraints.
"""

from structure import Section, Course

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

def get_user_preferences():

    # Number of classes
    num_required = int(input("How many required classes would you like to take? (max 3)"))
    num_electives = int(input("How many elective classes would you like to take? (max 3)"))

    print("\nNow rate your preferences on a scale from 0 (no preference) to 3 (strong preference):\n")

    # Class preferences
    class_morning_pref = int(input("Preference for morning classes (start before 1pm): "))
    class_night_pref = int(input("Preference for night classes (start after 1pm): "))

    # Work preferences
    work_morning_pref = int(input("Preference for working in the morning: "))
    work_night_pref = int(input("Preference for working in the evening: "))
    work_weekend_pref = int(input("How much do you want to avoid working on weekends (0 = don’t care, 3 = strongly avoid)? "))

    return {
        "num_required": num_required,
        "num_electives": num_electives,
        "class_prefs": {
            "prefer_morning_class": class_morning_pref,
            "prefer_night_class": class_night_pref
        },
        "work_prefs": {
            "prefer_morning_work": work_morning_pref,
            "prefer_night_work": work_night_pref,
            "avoid_weekend_work": work_weekend_pref
        }
    }

if __name__ == "__main__":
    prefs = get_user_preferences()
    print("\nYour preferences have been recorded:")
    print(prefs)
