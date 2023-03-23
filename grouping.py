# The code is designed to categorize the departments offering a set of courses into groups such that 
# no two courses of the same department are assigned to the same group.
# The logic behind this code can be broken down into the following steps:

# Read in an Excel file containing data on courses and the departments that offer them.

# Sort the courses in descending order based on the number of departments that offer the course.

# Initialize an empty list to store the student groups.

# Loop through each course, and for each course, assign departments to groups.

# For each department offering the course, check if it is already assigned to a group for that course.

# If the department is already assigned to a group, add the group index to a set of group indices.

# If the department is not assigned to a group, create a new group for it and add the group index to the set of group indices.

# For each group index in the set of group indices, add the department and the course code to the corresponding group.

# Print the final student groups.

# By following this logic, 
# the code ensures that each department offering a course is assigned to a unique group, 
# thereby preventing any conflicts in scheduling exams for those courses.

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