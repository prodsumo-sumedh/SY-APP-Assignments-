import re

with open("python.txt", "r") as file:
    paragraph = file.read()

letter = input("Enter the starting letter: ")

pattern = r'\b' + re.escape(letter) + r'\w*'
words = re.findall(pattern, paragraph, re.IGNORECASE)

print("Words beginning with", letter, "are:")
print(words)
