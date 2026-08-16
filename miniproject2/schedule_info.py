# Problem 1: Schedule Info
# This program looks up a course's room, instructor, and meeting time
# based on a course number entered by the user.

# Dictionary of course numbers and the room numbers where they meet
rooms = {
    'CS101': '3004',
    'CS102': '4501',
    'CS103': '6755',
    'NT110': '1244',
    'CM241': '1411'
}

# Dictionary of course numbers and the instructors that teach them
instructors = {
    'CS101': 'Haynes',
    'CS102': 'Alvarado',
    'CS103': 'Rich',
    'NT110': 'Burke',
    'CM241': 'Lee'
}

# Dictionary of course numbers and their meeting times
meeting_times = {
    'CS101': '8:00am',
    'CS102': '9:00am',
    'CS103': '10:00am',
    'NT110': '11:00am',
    'CM241': '1:00pm'
}

# Get the course number from the user
# Strip extra spaces and convert to uppercase so 'cs101' matches 'CS101'
course_number = input('Enter a class name: ').strip().upper()

# Display the course's room number, instructor, and meeting time,
# but only if the course number is actually in the dictionaries
if course_number in rooms:
    print('Class:', course_number)
    print('Room:', rooms[course_number])
    print('Instructor:', instructors[course_number])
    print('Time:', meeting_times[course_number])
else:
    print(course_number, 'is not a valid class name.')
