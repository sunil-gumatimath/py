# Create an empty dictionary called dog
dog = {}
# Add name, color, breed, legs, age to the dog dictionary
dog = {"name": "Luna", "color": "white", "breed": "Siberian Husky", "legs": 4, "age": 3}

# Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
student = {
    "first_name": "vaishali",
    "last_name": "gumatimath",
    "gender": "Female",
    "age": 24,
    "marital_status": "Married",
    "skills": ["cooking", "eating", "sleeping"],
    "country": "India",
    "city": "bangalore",
    "address": "Btm 2nd layout",
}
# Get the length of the student dictionary
len_student = len(student)

# Get the value of skills and check the data type, it should be a list
skills = student.get("skills")
print(type(skills))

# Modify the skills values by adding one or two skills
student.get("skills").append("dancing")
print(student.get("skills"))

# Get the dictionary keys as a list
student_keys = student.keys()
print(student_keys)

# Get the dictionary values as a list
student_values = student.values()
print(student_values)

# Change the dictionary to a list of tuples using items() method
student_lst = student.items()
print(student_lst)

# Delete one of the items in the dictionary
student.pop("last_name")
student.popitem()

# Delete one of the dictionaries
del dog
