def create_course_room_dictionary():
    course_keys = {
        'CS101': 3004,
        'CS102': 4501,
        'CS103': 6755,
        'NT110': 1244,
        'CM241': 1411
    }
    return course_keys
    
        
def create_instructor_dictionary():
    instructor_dict = {
        'CS101': 'Haynes',
        'CS102': 'Alvarado',
        'CS103': 'Rich',
        'NT110': 'Burke',
        'CM241': 'Lee'
    }
    return instructor_dict
    
def meeting_time():
    meeting_time = {
        'CS101': '8:00am',
        'CS102': '9:00am',
        'CS103': '10:00am',
        'NT110': '11:00am',
        'CM241': '1:00pm'
    }
    return meeting_time

def main():
    courses = create_course_room_dictionary()  
    instructors = create_instructor_dictionary()
    schedules = meeting_time()
    
    user_input = input(f'Enter a course (i.e., {list(courses.keys())}):')
    
      
    if user_input in courses:  
        print(f'Class: {user_input}')
        print(f'Room: {courses[user_input]}') 
        print(f'Instructor: {instructors[user_input]}')
        print(f'Time: {schedules[user_input]}')
    else:
        print('Invalid course number')

if __name__ == "__main__":
    main()
