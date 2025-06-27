"""
Personal Schedule Optimizer

Author:         Thomas Culhane

Description:    Greedy algorithm for assigning tasks to time slots based 
                on soft preferences and hard constraints.
"""

from collections import defaultdict

class Task:
    def __init__(self, name, duration, preference, prefs=None):
        self.name = name                    # name of the task
        self.duration = duration            # time (hrs) task will take
        self.preference = preference        # list of preferred time slots
        self.prefs = prefs if prefs else {} # dict containing general preferences

    def __repr__(self):
        return f"Task({self.name}, {self.duration}, {self.preference}, {self.prefs})"
    

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

def can_assign(task, start_idx, time_slots, schedule):
    """ Determines whether a given task can be assigned to a starting time slot and 
        proceed for its full duration, without conflictions with other tasks
    """
    
    duration = task.duration
    for i in range(duration):
        if start_idx + i < len(time_slots) - 1:
            slot = time_slots[start_idx + i]
        else:
            return False
        if slot in schedule:
            return False
    return True

def assign_score(task, start_idx, time_slots, schedule):
    """ Return the score for task being assigned at start_time. Considers soft preferences
        and ensures validity of slot assignment using can_assign()
    """

    # if start_idx is invalid, return -inf
    if not can_assign(task, start_idx, time_slots, schedule):
        return float('-inf')
    
    starting_time = time_slots[start_idx]
    day, hour = starting_time.split()
    score = 0

    # matching time slot preference bonus
    if starting_time in task.preference:
        score += 10
    else:
        score -= 5

    # time of day preference bonus
    if hour in {"7am", "8am", "9am", "10am"}:
        score += task.prefs.get("prefer_mornings", 0)
    if task.prefs.get("prefer_nights") and hour in {"8pm", "9pm", "10pm", "11pm"}:
        score += task.prefs.get("prefer_nights", 0)

    # weekend penalty
    if day in {"SA", "SU"}:
        score -= task.prefs.get("avoid_weekends", 0)

    # back-to-back tasks penalty
    prev_idx = start_idx - 1
    next_idx = start_idx + 1
    if prev_idx >= 0 and time_slots[prev_idx] in schedule:
        score -= 2
    if next_idx < len(time_slots) and time_slots[next_idx] in schedule:
        score -= 2

    return score

def schedule_tasks(tasks, time_slots):
    """ Greedily assign tasks to the best available time slot based on preference scores """
    
    schedule = {}

    for task in tasks:
        best_score = float('-inf')
        best_idx = None

        for i in range(len(time_slots) - task.duration + 1):
            score = assign_score(task, i, time_slots, schedule)
            if score > best_score:
                best_score = score
                best_idx = i

        if best_idx is not None:
            for j in range(task.duration):
                schedule[time_slots[best_idx + j]] = task
            print(f"Scheduled '{task.name}' at {time_slots[best_idx]} (score={best_score})")
        else:
            print(f"Could not schedule '{task.name}")

    return schedule

def display_schedule(schedule, time_slots):
    """ Displays weekly schedule in table format """

    days = ["M", "T", "W", "TH", "F", "SA", "SU"]
    hours = [
        "7am", "8am", "9am", "10am", "11am", "12pm", "1pm", "2pm", "3pm", 
        "4pm", "5pm", "6pm", "7pm", "8pm", "9pm", "10pm", "11pm", "12am"
    ]

    col_width = 18
    total_cols = len(days) + 1
    separator = "+" + "+".join(["-" * col_width for _ in range(total_cols)]) + "+"

    # Build the schedule table
    table = defaultdict(lambda: {day: "" for day in days})
    for slot, task in schedule.items():
        day, hour = slot.split()
        table[hour][day] = task.name

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
    with open("final_schedule.txt", "w") as f:
        f.write("Final Weekly Schedule\n\n")
        for line in lines:
            f.write(line + "\n")

def main():
    print("Scheduler initialized.")

if __name__ == "__main__":
    main()

    # FOR TESTING PURPOSES
    # Define tasks
    task1 = Task("Study Algorithms", 1, ["M 9am", "T 9am"],
                prefs= {
                    "prefer_mornings": 3,
                    "avoid_weekends": 2,
                    })
    task2 = Task("Gym", 2, ["T 5pm", "W 4pm"],
                prefs= {
                    "prefer_nights": 2,
                    "avoid_weekends": 0
                })
    tasks = [task1, task2]

    # Print tasks for now
    for task in tasks:
        print(task)

    # Initialize empty schedule
    schedule = {}

    # FIRST TESTING OF CAN_ASSIGN(), ASSIGN_SCORE()
    print("\nScoring options for task1:")
    for i, slot in enumerate(time_slots):
        s = assign_score(tasks[0], i, time_slots, schedule)
        if s > float('-inf'):
            print(f"{slot}: {s}")

    print("\nScoring options for task2:")
    for i, slot in enumerate(time_slots):
        s = assign_score(tasks[1], i, time_slots, schedule)
        if s > float('-inf'):
            print(f"{slot}: {s}")

    # Placeholder for scheduling logic
    print("\nEmpty schedule initialized.")

    # Initialize and run the greedy scheduler
    final_schedule = schedule_tasks(tasks, time_slots)

    # Print the final schedule
    display_schedule(final_schedule, time_slots)