HOMEWORK_MAX = 800.0
QUIZZES_MAX = 400.0
MIDTERM_MAX = 150.0
FINAL_MAX = 200.0

# Grade Calculator Program
# Calculates a course grade from homework, quiz, midterm, and final points.
# Weighting differs for undergrads (UG), grads (G), and distance learners (DL).

import sys

# --- On-screen instructions telling the user what to enter ---
print("Enter student status on the first line: UG, G, or DL")
print("Then enter 4 scores on the next line, separated by spaces:")
print("  homework_points  quiz_points  midterm_score  final_score")
print("Example:  UG  then  600.0 300.0 120.0 185.0")

# --- Step 1: read status, validate, read scores, compute category averages ---
status = input()

# Status must be one of the three valid codes, otherwise stop the program
if status != "UG" and status != "G" and status != "DL":
    print("Error: student status must be UG, G or DL")
    sys.exit()

# Read the four score values (floats) from one space-separated line
hw_points, quiz_points, midterm_points, final_points = input().split()
hw_points = float(hw_points)
quiz_points = float(quiz_points)
midterm_points = float(midterm_points)
final_points = float(final_points)

# Convert each category's points into a percentage of its maximum
homework = hw_points / HOMEWORK_MAX * 100
quizzes = quiz_points / QUIZZES_MAX * 100
midterm = midterm_points / MIDTERM_MAX * 100
final_exam = final_points / FINAL_MAX * 100

# --- Step 2: cap any average that exceeds 100% ---
if homework > 100:
    homework = 100
if quizzes > 100:
    quizzes = 100
if midterm > 100:
    midterm = 100
if final_exam > 100:
    final_exam = 100

print(f"Homework: {homework:2.1f}%")
print(f"Quizzes: {quizzes:2.1f}%")
print(f"Midterm: {midterm:2.1f}%")
print(f"Final Exam: {final_exam:2.1f}%")

# --- Step 3: weighted course average based on student status ---
if status == "UG":
    course_avg = homework * 0.20 + quizzes * 0.20 + midterm * 0.30 + final_exam * 0.30
elif status == "G":
    course_avg = homework * 0.15 + quizzes * 0.05 + midterm * 0.35 + final_exam * 0.45
else:  # DL
    course_avg = homework * 0.05 + quizzes * 0.05 + midterm * 0.40 + final_exam * 0.50

print(f"{status} average: {course_avg:.1f}%")

# --- Step 4: determine the letter grade from the course average ---
if course_avg >= 90.0:
    grade = "A"
elif course_avg >= 80.0:
    grade = "B"
elif course_avg >= 70.0:
    grade = "C"
elif course_avg >= 60.0:
    grade = "D"
else:
    grade = "F"

print(f"Course grade: {grade}")
