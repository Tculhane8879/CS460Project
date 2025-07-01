# Semester Scheduler

**Author:** Thomas Culhane

---

## Description

This project builds a personal semester schedule using a custom greedy algorithm. The scheduler assigns class sections and fills in available work hours based on user preferences, while respecting hard constraints like time conflicts and work block minimums. The core algorithm is greedy and uses heuristic scoring to accomplish this.

The result is a full weekly schedule that:
- Prioritizes required courses
- Avoids overlapping class times
- Suggests realistic, distributed work availability

---

## Features

- Preference-based scheduling (class time, work time, weekend avoidance)
- No time conflicts
- 20+ hours of work availability per week (4-8 hour blocks only)
- Clear weekly schedule exported to a file
- Automated test suite

---

## How to Run

### Requirements
- Python 3.10+
- No external packages required

### Steps

1. Clone or download the project files:

```bash
git clone https://github.com/your-username/semester-scheduler.git
cd semester-scheduler
```

2. Run the scheduler
```python scheduler.py```

3. Enter input when prompted

4. View formatted weekly schedule in:
```schedule.txt```

---

## File Structure

```scheduler.py```
- Main program, core algorithm (create_schedule()), display

```structure.py```
- Models data for ```Course``` and ```Section```

```course_data.py```
- ```Course``` representations of FA/SP SDSU class options

```test_scheduler.py```
- Python ```unittest``` test suite
- Run test suite using ```python test_scheduler.py```
