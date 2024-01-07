# Example file for Advanced Python: Language Features by Joe Marini
# Demonstrate how to use list comprehensions


# define two lists of numbers
evens = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
odds = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

# TODO: Perform a mapping and filter function on a list
even_squared = list(map(lambda e:e**2, evens))
print(even_squared)

even_squared_filtered = list(map(lambda e:e**2,
    filter(lambda e: e>4 and e<16, evens)))
print(even_squared_filtered)


# TODO: Derive a new list of numbers frm a given list
even_squared_2 = [e ** 2 for e in evens]
print(even_squared_2)

# TODO: Limit the items operated on with a predicate condition
odd_squared_filtered = [o ** 2 for o in odds if o>3 and o<17]
print(odd_squared_filtered)