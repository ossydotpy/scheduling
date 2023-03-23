# this code is for transforming our excel data into dictionaries which will then be used to create groupings for students.

import pandas as pd

df = pd.read_excel('grouping.xlsx')

# create an empty dictionary
courses = {}

# loop through each row in the dataframe
for index, row in df.iterrows():
    # use the first element of the row as the key
    key = row[0]
    # use the rest of the elements as the values
    values = []
    for value in row[1:]:
        if not pd.isna(value):
            values.append(value)
    # add the key-value pair to the dictionary
    courses[key] = values
    
departments = sorted(list(set().union(*courses.values())))

groups = {i: set() for i in range(len(departments))}

# Sort the courses in descending order of the number of departments whose students have registered for the course.
sorted_courses = sorted(courses, key=lambda x: len(courses[x]), reverse=True)

# Assign each department to a group based on the courses they have registered for
for course in sorted_courses:
    departments_for_course = courses[course]
    for department in departments_for_course:
        # Find the first available group that does not contain a department with registered students for this course
        for group in groups.values():
            if not any(dept in group for dept in departments_for_course):
                group.add(department)
                break

# Print the groups
for i, group in groups.items():
    print(f"Group {i+1}: {', '.join(group)}")