import re

file = open('sample_text.txt')
txt = str(file.readlines())
print(type(txt))
# my_list = ["apple", "banana", "cherry"]
# my_string = "".join(txt)
# print(my_string)

# text = "TheREAL Book \nof \nReal Estate9781593155322_FM:real estate_new  3/25/09  3:52 PM  Page i', '9781593155322_FM:real estate_new  3/25/09  3:52 PM  Page ii\nThis page intentionally left blank ', 'The REAL Book \nof \nREAL EXPERTS. REAL STORIES. REAL LIFE.\nRobert Kiyosaki\nReal Estate9781593155322_FM:real estate_new  3/25/09  3:52 PM  Page iii', 'Copyright © 2009 by Robert T. Kiyosaki\nPublished by Vanguard PressAll rights reserved. No part of this publication may be reproduced, stored in a retrieval \nsystem"
# print(type(text))

# Input text containing newline characters
# text = "This is a\nsample text\nwith newline characters."

# Define a regex pattern to match newline characters
# pattern = r'\n'
pattern = r'\\'

# Replace newline characters with a space
# result = re.sub(pattern, ' ', text)
result = re.sub(pattern, '', txt)

# Print the result
print(result)
print(type(result))


# result = re.sub(pattern, ' ', text)
#
# # Print the result
# print(result)
