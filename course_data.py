""" SDSU Fall 2025/Spring 2026 course options """

from structure import Section, Course

courses = [
    Course("CS 420 - Advanced Programming Languages", required=True, sections=[
        Section("TTh", "3:30", "4:45"),
        Section("TTh", "7:00", "8:15"),
        Section("TTh", "12:00", "1:15")
    ]),
    Course("CS 370 - Computer Architecture", required=True, sections=[
        Section("TTh", "5:30", "6:45"),
        Section("MW", "4:00", "5:15"),
        Section("MW", "11:00", "12:15"),
        Section("MW", "2:00", "3:15")
    ]),
    Course("CS 450 - Introduction to Artificial Intelligence", required=True, sections=[
        Section("MW", "7:00", "8:15"),
        Section("M", "7:00", "9:40")
    ]),
    Course("CS 370 - Computer Architecture", required=True, sections=[
        Section("TTh", "5:30", "6:45"),
        Section("MW", "4:00", "5:15"),
        Section("MW", "11:00", "12:15"),
        Section("MW", "2:00", "3:15")
    ]),
    Course("CS 480 - Operating Systems", required=True, sections=[
        Section("TTh", "4:00", "5:15"),
        Section("TTh", "5:30", "6:45")
    ]),
    Course("CS 470 - UNIX System Administration", required=False, sections=[
        Section("M", "7:00", "9:40")
    ]),
    Course("CS 545 - Introduction to Web Application Development", required=False, sections=[
        Section("M", "7:00", "9:40")
    ]),
    Course("CS 583 - 3D Game Programming", required=False, sections=[
        Section("MW", "7:00", "8:15")
    ]),
    Course("CS 596 - Applied Security Management", required=False, sections=[
        Section("W", "7:00", "9:40")
    ]),
    Course("CS 596 - Wireless Network Security", required=False, sections=[
        Section("TTh", "5:30", "6:45")
    ]),
    Course("CS 496 - Cloud Computing", required=False, sections=[
        Section("MWF", "11:00", "11:50")
    ]),
    Course("CS 514 - Database Theory and Implementation", required=False, sections=[
        Section("TTh", "5:30", "6:45"),
        Section("TTh", "2:00", "3:15"),
        Section("TTh", "12:30", "1:45"),
        Section("TTh", "7:00", "8:15")
    ]),
    Course("CS 549 - Machine Learning", required=False, sections=[
        Section("TTh", "5:30", "6:45"),
        Section("TTh", "4:00", "5:15"),
        Section("TTh", "2:00", "3:15")
    ]),
    Course("CS 577 - Principles and Techniques of Data Science", required=False, sections=[
        Section("W", "7:00", "9:40"),
        Section("T", "7:00", "9:40")
    ])
]