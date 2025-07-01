import unittest
from semester_scheduler import create_schedule, time_slots
from course_data import courses

class SchedulerTest(unittest.TestCase):

    def test_work_hours_minimum(self):
        """Ensure at least 20 hours of work are scheduled."""
        prefs = {
            "num_required": 2,
            "num_electives": 1,
            "class_prefs": {
                "prefer_morning_class": 1,
                "prefer_night_class": 1
            },
            "work_prefs": {
                "prefer_morning_work": 1,
                "prefer_night_work": 1,
                "avoid_weekend_work": 0
            }
        }
        schedule = create_schedule(courses, prefs, time_slots)
        work_slots = [slot for slot, name in schedule.items() if name == "Work"]
        self.assertGreaterEqual(len(work_slots), 20, "Should schedule at least 20 work hours")

    def test_required_courses_scheduled(self):
        """Ensure the correct number of required courses are selected."""
        prefs = {
            "num_required": 3,
            "num_electives": 0,
            "class_prefs": {
                "prefer_morning_class": 0,
                "prefer_night_class": 0
            },
            "work_prefs": {
                "prefer_morning_work": 0,
                "prefer_night_work": 0,
                "avoid_weekend_work": 0
            }
        }
        schedule = create_schedule(courses, prefs, time_slots)
        class_slots = [slot for slot, name in schedule.items() if name != "Work"]
        self.assertGreaterEqual(len(class_slots), 6, "Should have scheduled 3 courses (each with ~2 time slots)")

    def test_work_spread_across_multiple_days(self):
        """Ensure work is distributed across at least 3 different days."""
        prefs = {
            "num_required": 2,
            "num_electives": 2,
            "class_prefs": {
                "prefer_morning_class": 0,
                "prefer_night_class": 0
            },
            "work_prefs": {
                "prefer_morning_work": 0,
                "prefer_night_work": 0,
                "avoid_weekend_work": 0
            }
        }
        schedule = create_schedule(courses, prefs, time_slots)
        work_days = set(slot.split()[0] for slot, name in schedule.items() if name == "Work")
        self.assertGreaterEqual(len(work_days), 3, "Work hours should be spread across at least 3 days")

    def test_avoids_weekends_when_preferred(self):
        """Ensure weekend slots are avoided if user strongly prefers not to work weekends."""
        prefs = {
            "num_required": 2,
            "num_electives": 1,
            "class_prefs": {
                "prefer_morning_class": 0,
                "prefer_night_class": 0
            },
            "work_prefs": {
                "prefer_morning_work": 0,
                "prefer_night_work": 0,
                "avoid_weekend_work": 3
            }
        }
        schedule = create_schedule(courses, prefs, time_slots)
        weekend_slots = [slot for slot, name in schedule.items() if name == "Work" and slot.split()[0] in {"SA", "SU"}]
        self.assertLessEqual(len(weekend_slots), 6, "Should mostly avoid weekends when avoid_weekend_work=3")

    def test_prefers_morning_classes(self):
        """Verify that morning class preference influences section selection."""
        prefs = {
            "num_required": 2,
            "num_electives": 1,
            "class_prefs": {
                "prefer_morning_class": 3,
                "prefer_night_class": 0
            },
            "work_prefs": {
                "prefer_morning_work": 0,
                "prefer_night_work": 0,
                "avoid_weekend_work": 0
            }
        }
        schedule = create_schedule(courses, prefs, time_slots)
        morning_class_slots = [slot for slot, name in schedule.items()
                            if name != "Work" and slot.split()[1] in {"7am", "8am", "9am", "10am", "11am", "12pm"}]
        self.assertGreaterEqual(len(morning_class_slots), 6, "Should assign classes to morning slots when preferred")

if __name__ == "__main__":
    unittest.main()
