"""
Personal Semester Scheduler

Author:         Thomas Culhane

Description:    Greedy algorithm for assigning tasks to time slots based 
                on soft preferences and hard constraints.
"""

from structure import Section, Course
from collections import defaultdict
from course_data import courses

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
    num_required = int(input("How many required classes would you like to take? (between 2-4) "))
    num_electives = int(input("How many elective classes would you like to take? (between 1-3) "))

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

def display_schedule(schedule, time_slots):
    """ Displays weekly schedule in a txt file in table format """

    days = ["M", "T", "W", "TH", "F", "SA", "SU"]
    hours = [
        "7am", "8am", "9am", "10am", "11am", "12pm", "1pm", "2pm", "3pm", 
        "4pm", "5pm", "6pm", "7pm", "8pm", "9pm", "10pm", "11pm", "12am"
    ]

    col_width = 50
    total_cols = len(days) + 1
    separator = "+" + "+".join(["-" * col_width for _ in range(total_cols)]) + "+"

    valid_days = {"M", "T", "W", "TH", "F", "SA", "SU"}

    # Build the schedule table
    table = defaultdict(lambda: {day: "" for day in days})
    for slot, activity in schedule.items():
        day, hour = slot.split()
        table[hour][day] = activity
        # print(f"Placing '{activity}' in column '{day}' at row '{hour}'")

    # Build output lines manually
    lines = []
    lines.append("Final Weekly Schedule\n")
    lines.append(separator)

    # Header row
    header = ["Time".center(col_width)] + [day.center(col_width) for day in days]
    lines.append("|" + "|".join(header) + "|")
    lines.append(separator)

    # Body rows
    for hour in hours:
        row = [hour.center(col_width)]
        for day in days:
            cell = table[hour][day]
            row.append(cell.center(col_width))
        lines.append("|" + "|".join(row) + "|")
        lines.append(separator)

    # Write to file
    with open("schedule.txt", "w") as f:
        for line in lines:
            f.write(line + "\n")

def assign_course_score(section, class_prefs):
    """ Score a course/section based on user class time preferences. """
    score = 0
    for slot in section.get_time_slots():
        _, hour = slot.split()

        # Time-of-day scoring
        if hour in {"7am", "8am", "9am", "10am", "11am", "12pm"}:
            score += class_prefs.get("prefer_morning_class", 0)
        else:
            score += class_prefs.get("prefer_night_class", 0)

        # Bonus for 1 day/week sections
        unique_days = {slot.split()[0] for slot in time_slots}
        if len(unique_days) == 1:
            score += 2 

    return score

def find_work_blocks(schedule, time_slots, min_block_size=4):
    """ Creates a list of valid work availability blocks (at least 4 consecutive hours). """
    
    open_blocks = []
    i = 0
    # Iterate until time block is < 4 hours, becoming invalid for work availability
    while i <= len(time_slots) - min_block_size:
        block = []
        for j in range(i, len(time_slots)):
            slot = time_slots[j]
            # Stop if part of time block is already scheduled
            if slot in schedule:
                break
            # Record time blocks of >= 4 hours, continue until time block becomes invalid
            block.append(slot)
            if len(block) >= min_block_size:
                open_blocks.append((i, len(block)))
        # If time block was invalid check starting at next index, else jump to after previous valid time block 
        i += 1 if not block else len(block)
    # Return list of valid work availability blocks
    return open_blocks

def score_work_block(block_slots, work_prefs, days_with_work=None):
    """ Scores valid work availability blocks of time. """
    score = 0
    slots_by_day = defaultdict(list)

    for slot in block_slots:
        day, hour = slot.split()
        slots_by_day[day].append(hour)

        # Time-of-day scoring
        if hour in {"7am", "8am", "9am", "10am", "11am"}:
            score += work_prefs.get("prefer_morning_work", 0)
        elif hour in {"5pm", "6pm", "7pm", "8pm", "9pm"}:
            score += work_prefs.get("prefer_night_work", 0)
        # Weekend working preference scoring
        if day in {"SA", "SU"}:
            score -= work_prefs.get("avoid_weekend_work", 0)

        # Bonus for work on a day with no other work
        if days_with_work is not None:
            new_days = [day for day in slots_by_day if day not in days_with_work]
            score += len(new_days)

        # Bonus for longer blocks
        score += len(block_slots) // 2

    return score

def create_schedule(courses, prefs, time_slots):
    """ Core scheduling algorithm. """
    
    # Create empty schedule dict[str, str]
    schedule = {}  # time_slot → course_name
    selected_courses = []

    # Get user preferences
    num_required = prefs["num_required"]
    num_electives = prefs["num_electives"]
    class_prefs = prefs["class_prefs"]
    work_prefs = prefs["work_prefs"]

    # Split potential course options into required and elective
    required_courses = [c for c in courses if c.required]
    elective_courses = [c for c in courses if not c.required]

    # Add required courses to schedule
    for course in required_courses:
        # Do not assign more than preferred number of required courses
        if len(selected_courses) >= num_required:
            break
        
        best_section = None
        best_score = float('-inf')

        # Assign scores to each section
        for section in course.sections:
            slots = section.get_time_slots()
            # Ensure each section's time does not overlap with any other times on the schedule
            if all(slot not in schedule for slot in slots):
                # Use score assignments to determine best fitting section
                score = assign_course_score(section, class_prefs)
                if score > best_score:
                    best_score = score
                    best_section = section

        # Schedule the best fitting course
        if best_section:
            for slot in best_section.get_time_slots():
                schedule[slot] = course.name
            selected_courses.append((course.name, best_section))

    # Add elective courses to schedule
    for course in elective_courses:
        # Do not assign more than preferred number of total courses
        if len(selected_courses) >= num_required + num_electives:
            break

        best_section = None
        best_score = float('-inf')

        # Assign scores to each section
        for section in course.sections:
            slots = section.get_time_slots()
            # Ensure each section's time does not overlap with any other times on the schedule
            if all(slot not in schedule for slot in slots):
                # Use score assignments to determine best fitting section
                score = assign_course_score(section, class_prefs)
                if score > best_score:
                    best_score = score
                    best_section = section

        # Schedule the best fitting course
        if best_section:
            for slot in best_section.get_time_slots():
                schedule[slot] = course.name
            selected_courses.append((course.name, best_section))

    # Output courses selected
    print("\nCourses Selected :")
    for name, section in selected_courses:
        print(f"  {name} → {section}")

    # Assign work availability time blocks
    total_availability_hrs = 0
    min_block_size = 4
    min_required_hrs = 20

    # Search for valid time blocks for work availability
    blocks = find_work_blocks(schedule, time_slots, min_block_size)
    block_scores = []

    # Loop through all open blocks
    for start_idx, size in blocks:
        block_slots = time_slots[start_idx:start_idx + size]    # Get time block string representation
        score = score_work_block(block_slots, work_prefs)       # Assign scores to time blocks
        block_scores.append((score, start_idx, size))           # Add scores of each time block to list

    # Sort scores highest to lowest
    block_scores.sort(reverse=True)

    days_with_work = set()
    # max of 8 hrs availability per day
    max_hours_per_day = 8
    daily_work_hours = defaultdict(int)

    # Loop through work blocks from highest score to lowest
    for score, start_idx, size in block_scores:
        # Stop if min hrs are reached
        if total_availability_hrs >= min_required_hrs:
            break

        # Get list of time slots for work scheduling
        block_slots = time_slots[start_idx:start_idx + size]

        # Count work hours per day
        slots_by_day = defaultdict(list)
        for slot in block_slots:
            day, hour = slot.split()
            slots_by_day[day].append(slot)

        accepted_slots = []

        for day, slots in slots_by_day.items():
            # Continue if max hrs for a day is reached
            if daily_work_hours[day] >= max_hours_per_day:
                continue
            # Assign available work blocks until min hrs reached
            available = max_hours_per_day - daily_work_hours[day]
            to_use = min(len(slots), available, min_required_hrs - total_availability_hrs)
            accepted_slots.extend(slots[:to_use])
            daily_work_hours[day] += to_use
            days_with_work.add(day)
            total_availability_hrs += to_use
            # Stop when min hrs are assigned
            if total_availability_hrs >= min_required_hrs:
                break
    
    # Schedule work slots            
    for slot in accepted_slots:
        schedule[slot] = "Work"

    # Output total availability hours
    print(f"Total work availability hours: {total_availability_hrs}")

    # Return the completed schedule
    return schedule

if __name__ == "__main__":
    prefs = get_user_preferences()
    schedule = create_schedule(courses, prefs, time_slots)
    display_schedule(schedule, time_slots)
