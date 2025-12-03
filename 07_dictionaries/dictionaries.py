# Dictionaries
# A dictionary is a collection of unordered, modifiable(mutable) paired (key: value) data type.

# To create a dictionary we use curly brackets, {} or the dict() built-in function.

empty_dct = {}

dct = {
    "key1": "value1",
    "key2": "value2",
    "key3": "value3",
    "key4": "value4",
}

# Example

person = {
    "fname": "sunil",
    "lname": "ted",
    "age": 24,
    "country": "India",
    "is_married": False,
    "skills": ["javascript", "Java", "SQL", "Python", "ReactJS"],
    "address": {
        "state": "Karnataka",
        "city": "bangalore",
        "street": "Btm 2nd layout",
    },
}
print(dct)
print(person)

# It checks the number of 'key: value' pairs in the dictionary.
print(len(dct))
print(len(person))

# We can access Dictionary items by referring to its key name.
# dct = {"key1": "value1","key2": "value2","key3": "value3","key4": "value4",}
print(dct["key1"])
print(dct["key2"])

print(person["fname"])
print(person["lname"])
print(person["age"])
print(person["country"])
print(person["is_married"])
print(person["skills"][3])
print(person["address"]["state"])

# Accessing an item by key name raises an error if the key does not exist. To avoid this error first we have to check
# if a key exist or we can use the get method. The get method returns None, which is a NoneType object data type, if the key does not exist.
print(person.get("fname"))
print(person.get("country"))
print(person.get("skills"))
print(person.get("address"))

# We can add new key and value pairs to a dictionary
person["job_title"] = "Full Stack Engineer"
person["skills"].append("Docker")

print(person)

# We can modify items in a dictionary
person["age"] = 25
print(person.get("age"))

# We use the in operator to check if a key exist in a dictionary
print("name" in person)
print("fname" in person)

# Removing Key and Value Pairs from a Dictionary
# pop(key): removes the item with the specified key name:
# popitem(): removes the last item
# del: removes an item with specified key name

# syntax
dct = {"key1": "value1", "key2": "value2", "key3": "value3", "key4": "value4"}
dct.pop("key1")

dct = {"key1": "value1", "key2": "value2", "key3": "value3", "key4": "value4"}
dct.popitem()  # removes the last item

del dct["key2"]  # removes key2 item

person.pop("lname")
person.popitem()
del person["is_married"]

# Changing Dictionary to a List of Items
# The items() method changes dictionary to a list of tuples.
# syntax
dct = {"key1": "value1", "key2": "value2", "key3": "value3", "key4": "value4"}
print(
    dct.items()
)  # dict_items([('key1', 'value1'), ('key2', 'value2'), ('key3', 'value3'), ('key4', 'value4')])

# Clearing a Dictionary
# If we don't want the items in a dictionary we can clear them using clear() method
# syntax
dct = {"key1": "value1", "key2": "value2", "key3": "value3", "key4": "value4"}
print(dct.clear())  # None

# Deleting a Dictionary
# If we do not use the dictionary we can delete it completely
dct = {"key1": "value1", "key2": "value2", "key3": "value3", "key4": "value4"}
del dct

# Copy a Dictionary
# We can copy a dictionary using a copy() method. Using copy we can avoid mutation of the original dictionary.
dct = {"key1": "value1", "key2": "value2", "key3": "value3", "key4": "value4"}
dct_copy = dct.copy()
print(dct_copy)

# Getting Dictionary Keys as a List
# The keys() method gives us all the keys of a a dictionary as a list.
dct = {"key1": "value1", "key2": "value2", "key3": "value3", "key4": "value4"}
keys = dct.keys()
print(keys)

# Getting Dictionary Values as a List
# The values method gives us all the values of a a dictionary as a list.
dct = {"key1": "value1", "key2": "value2", "key3": "value3", "key4": "value4"}
values = dct.values()
print(values)
