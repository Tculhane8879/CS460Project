"""
Personal Schedule Optimizer
Author: <your name>
Description: Greedy algorithm for assigning tasks to time slots based 
             on soft preferences and hard constraints.
"""
class Task:
    def __init__(self, name, duration, preference):
        self.name = name                # name of the task
        self.duration = duration        # time (hrs) task will take
        self.preference = preference    # list of preferred time slots

    def __repr__(self):
        return f"Task({self.name}, {self.duration}, {self.preference})"


def main():
    print("Scheduler initialized.")

if __name__ == "__main__":
    main()
    task1 = Task("Study Algorithms", 1, ["Mon 9am", "Tue 9am"])
    task2 = Task("Gym", 2, ["Tue 5pm", "Wed 4pm"])
    print(task1)
    print(task2)