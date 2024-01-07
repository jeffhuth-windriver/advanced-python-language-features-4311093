# Example file for Advanced Python: Language Features by Joe Marini
# Programming challenge for comprehensions

import string
import pprint


test_str = "2 apples, 9 oranges?, 4 pears, Mike's 1 egg, Jane's 2 kiwis, $50!"

# YOUR CODE HERE

# print the data
str_data = {
    "Length": len(test_str),
    "Digits": len([t for t in test_str if t.isnumeric()]),
    "Punctuation": len([t for t in test_str if t in string.punctuation]),
    "Unique Letters": (u := "".join({t for t in test_str if t.isalpha()})),
    "Unique Count": len(u)
}
pprint.pp(str_data)
