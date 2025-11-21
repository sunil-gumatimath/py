# Exercises: Level 1
# Declare an empty list

empty_list = list()

# Declare a list with more than 5 items
items = ['item1','item2','item3','item4','item5','item6']

# Find the length of your list
len_list = len(items)

# Get the first item, the middle item and the last item of the list
first_element = items[0]
middle_item = items[len(items)//2]
last_element = items[-1]

# Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
mixed_data_types = ["Ted", 22, 5.4, "Single", "Bangalore, India"]

# Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle','Amazon']

# Print the list using print()
print(it_companies)

# Print the number of companies in the list
print(len(it_companies))

# Print the first, middle and last company
first_company = it_companies[0]
middle_company = it_companies[len(it_companies)//2]
last_company = it_companies[-1]

# Print the list after modifying one of the companies
# ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
it_companies[0] = 'OpenAi'

# Add an IT company to it_companies
it_companies.append('Anthropic')

# Insert an IT company in the middle of the companies list
it_companies.insert(len(it_companies) // 2 ,'Tesla')
print(it_companies)

# Change one of the it_companies names to uppercase (IBM excluded!)
for i,company in enumerate(it_companies):
    if company != 'IBM':
        it_companies[i] = company.upper()
        break

# Join the it_companies with a string '#;  '
joined_companies = '#; '.join(it_companies)

# Check if a certain company exists in the it_companies list.
print('OpenAi' in it_companies or 'OPENAI' in it_companies)

# Sort the list using sort() method
it_companies.sort()

# Reverse the list in descending order using reverse() method
it_companies.reverse()

# Slice out the first 3 companies from the list
first_three_company = it_companies[:3]

# Slice out the last 3 companies from the list
last_three_company = it_companies[-3:]

# Slice out the middle IT company or companies from the list
n = len(it_companies)
if n % 2 == 1:
    middle_company = it_companies[n // 2]
else:
    middle_company = it_companies[n // 2 - 1 : n // 2 + 1]

# Remove the first IT company from the list
# del it_companies[0]
it_companies.pop(0)

# Remove the middle IT company or companies from the list
mid = len(it_companies)//2
it_companies.pop(mid)

# Remove the last IT company from the list
# del it_companies[-1]
it_companies.pop()

# Remove all IT companies from the list
it_companies.clear()

# Destroy the IT companies list
del it_companies

# Join the following lists:
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
joined_stack = front_end + back_end

# front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
# back_end = ['Node','Express', 'MongoDB']
# After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack, then insert Python and SQL after Redux.

full_stack = joined_stack.copy()
full_stack.insert(5,'Python') 
full_stack.insert(6,'SQL')
print(full_stack)

# Exercises: Level 2
# The following is a list of 10 students ages:
# ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
# Sort the list and find the min and max age
min_age = min(ages)
max_age = max(ages)
print(min_age)
print(max_age)

# Add the min age and the max age again to the list
ages.append(min_age)
ages.append(max_age)
ages.sort()
print(ages)

# Find the median age (one middle item or two middle items divided by two)
middle_index = len(ages) // 2
if len(ages) % 2 == 0:
    median_age = (ages[middle_index - 1] + ages[middle_index]) / 2
else:
    median_age = ages[middle_index]
print("Median age:", median_age)

# Find the average age (sum of all items divided by their number )
average = sum(ages) / len(ages)

# Find the range of the ages (max minus min)
age_range = max(ages) - min(ages)

# Compare the value of (min - average) and (max - average), use abs() method
diff_min = abs(min(ages) - average)
diff_max = abs(max(ages) - average)
print("Min deviation:", diff_min)
print("Max deviation:", diff_max)

# Find the middle country(ies) in the countries list
countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
mid_country = len(countries) // 2
print(countries[mid_country])

# Divide the countries list into two equal lists if it is even if not one more country for the first half.
countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
n = len(countries)
mid = (n + 1) // 2  # This ensures first half gets one more element if odd length
first_half = countries[:mid]
second_half = countries[mid:]
print("First half:", first_half)
print("Second half:", second_half)


# ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']. Unpack the first three countries and the rest as scandic countries.
first_country, second_country, third_country, *rest = countries
print('first company :',first_country)
print('second company :',second_country)
print('third company :',third_country)
print('rest',rest)