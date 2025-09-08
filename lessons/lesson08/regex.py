import re

text = """This is a sample text for regex testing.
It includes some email addresses: test@example.com, hello@world.com
And some phone numbers: (123) 456-7890, 987-654-3210
Let's see how well our regex patterns can match these formats."""

pattern = "Thi"
print(re.search(pattern, text))  # Should print a match object if found, else None

print(re.findall(pattern, text))  # Should print a list of all matches

com = re.compile(pattern)
print(com.findall(text))  # Should print a list of all matches using the compiled pattern

print(re.split(":", text))  # Should split the text at each match of the pattern
print(re.sub(":", " - ", text))  # Should replace each match of the pattern with " - "

pattern = "[a-z12:]+"
print(re.findall(pattern, text))  # Should print a list of all lowercase words

pattern = "\d"
print(re.findall(pattern, text))  # Should print a list of all digits

pattern = "t..t"
print(re.findall(pattern, text))  # Should print a list of all digits

pattern = "^It"
print(re.findall(pattern, text, re.M))  # Should print a list of all matches at the start of lines

pattern = "\d{3}"
print(re.findall(pattern, text))  # Should print a list of all 3-digit sequences
pattern = "\d{3, 5}"
print(re.findall(pattern, text))  # Should print a list of all 3-digit sequences

pattern_email = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
print(re.findall(pattern_email, text))  # Should print a list of all email addresses

print(re.sub("[A-Z]{1}[a-z]{2}", " - ", text))  # Should replace each match of the pattern with " - "