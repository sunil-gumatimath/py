# sets
it_companies = {"Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

# 1. Find the length of the set it_companies
print(len(it_companies))  # 7

# 2. Add 'Twitter' to it_companies
it_companies.add("Twitter")
print(it_companies)

# 3. Insert multiple IT companies at once to the set it_companies
it_companies.update(["OpenAI", "Anthropic", "KimK2"])
print(it_companies)

# 4. Remove one of the companies from the set it_companies
rm_company = it_companies.pop()
print("removed : ", rm_company)
print(it_companies)

# 5. What is the difference between remove and discard
# remove(item) → error if item does NOT exist
# discard(item) → NO error even if item is missing


# Join A and B
result = A.union(B)
print(result)

# Find A intersection B
result = A.intersection(B)
print(result)

# Is A subset of B
result = A.issubset(B)
print(result)

# Are A and B disjoint sets
result = A.isdisjoint(B)
print(result)

# Join A with B and B with A
result = A.union(B)
final_result = result.union(A)
print(final_result)

# What is the symmetric difference between A and B
result = A.symmetric_difference(B)

# Delete the sets completely
# del A , B , age

# Convert the ages to a set and compare the length of the list and the set, which one is bigger?
age_set = set(age)

if len(age_set) > len(age):
    print("Set is bigger")
elif len(age_set) < len(age):
    print("List is bigger")
else:
    print("Both are equal")

print("List length:", len(age))
print("Set length:", len(age_set))


# Explain the difference between the following data types: string, list, tuple and set
# String: Ordered sequence of characters (immutable).
# List: Ordered, mutable collection that can store different data types.
# Tuple: Ordered, immutable collection of elements.
# Set: Unordered collection of unique elements (no duplicates).


# I am a teacher and I love to inspire and teach people. How many unique words have been used in the sentence? Use the split methods and set to get the unique words.
sentence = "I am a teacher and I love to inspire and teach people"
words = sentence.split()
unique_words = set(words)

print("Unique words ", unique_words)
print("Count : ", len(unique_words))
