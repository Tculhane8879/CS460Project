""" SDSU Fall 2025/Spring 2026 course options """

from structure import Section, Course

courses = [
    Course("CS 420 - Advanced Programming Languages", required=True, sections=[
        Section("TTH", "3:30pm", "4:45pm"),
        Section("TTH", "7:00pm", "8:15pm"),
        Section("TTH", "12:00pm", "1:15pm")
    ]),
    Course("CS 370 - Computer Architecture", required=True, sections=[
        Section("TTH", "5:30pm", "6:45pm"),
        Section("MW", "4:00pm", "5:15pm"),
        Section("MW", "11:00am", "12:15pm"),
        Section("MW", "2:00pm", "3:15pm")
    ]),
    Course("CS 450 - Introduction to Artificial Intelligence", required=True, sections=[
        Section("MW", "7:00pm", "8:15pm"),
        Section("M", "7:00pm", "9:40pm")
    ]),
    Course("CS 370 - Computer Architecture", required=True, sections=[
        Section("TTH", "5:30pm", "6:45pm"),
        Section("MW", "4:00pm", "5:15pm"),
        Section("MW", "11:00am", "12:15pm"),
        Section("MW", "2:00pm", "3:15pm")
    ]),
    Course("CS 480 - Operating Systems", required=True, sections=[
        Section("TTH", "4:00pm", "5:15pm"),
        Section("TTH", "5:30pm", "6:45pm")
    ]),
    Course("CS 470 - UNIX System Administration", required=False, sections=[
        Section("M", "7:00pm", "9:40pm")
    ]),
    Course("CS 545 - Introduction to Web Application Development", required=False, sections=[
        Section("M", "7:00pm", "9:40pm")
    ]),
    Course("CS 583 - 3D Game Programming", required=False, sections=[
        Section("MW", "7:00pm", "8:15pm")
    ]),
    Course("CS 596 - Applied Security Management", required=False, sections=[
        Section("W", "7:00pm", "9:40pm")
    ]),
    Course("CS 596 - Wireless Network Security", required=False, sections=[
        Section("TTH", "5:30pm", "6:45pm")
    ]),
    Course("CS 496 - Cloud Computing", required=False, sections=[
        Section("MWF", "11:00am", "11:50am")
    ]),
    Course("CS 514 - Database Theory and Implementation", required=False, sections=[
        Section("TTH", "5:30pm", "6:45pm"),
        Section("TTH", "2:00pm", "3:15pm"),
        Section("TTH", "12:30pm", "1:45pm"),
        Section("TTH", "7:00pm", "8:15pm")
    ]),
    Course("CS 549 - Machine Learning", required=False, sections=[
        Section("TTH", "5:30pm", "6:45pm"),
        Section("TTH", "4:00pm", "5:15pm"),
        Section("TTH", "2:00pm", "3:15pm")
    ]),
    Course("CS 577 - Principles and Techniques of Data Science", required=False, sections=[
        Section("W", "7:00pm", "9:40pm"),
        Section("T", "7:00pm", "9:40pm")
    ])
]