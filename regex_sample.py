import re
# ==========
# file = open('sample_text.txt')
file = open('raw_pdf_file.txt')
txt = str(file.readlines())
# print(type(txt))
# print(txt)

pattern1 = r'\\n' #creating a pattern to detect the breakline \n but this will still leave a single backslash to the output text
text1 = re.sub(pattern1, '', txt) #replacing the breakline with a single space, a single backslash will still remain in the output text
txt = text1 #assigning it the result to the original variable
# print(txt)

pattern2 = r'\\' #creating a second pattern to detect the single backslash, in this code we will use a double backslash for a single backslash to
# avoid SyntaxError
text2 = re.sub(pattern2,'',txt)
txt = text2
# print(txt)

pattern3 = r'-'
text3 = re.sub(pattern3,'',txt)
txt = text3
# print(txt)

pattern4 = r'n•'
text4 = re.sub(pattern4,'',txt)
txt = text4
# print(txt)

pattern5 = r'•'
text5 = re.sub(pattern5,'',txt)
txt = text5
# print(txt)

pattern6 = r'\d{13}' #finding all numeric characters with length of thirteen
text6 = re.sub(pattern6,'',txt)
txt = text6
# print(txt)

pattern7 = r'\D\d{2}$'
text7 = re.sub(pattern7,'',txt)
txt = text7
# print(txt)

pattern8 = r'THE REAL BOOK OF REAL ESTATE_'
text8 = re.sub(pattern8,'',txt)
txt = text8
# print(txt)

pattern9 = r'real estate_new'
text9 = re.sub(pattern9,'',txt)
txt = text9
print(txt)
# ==========




# THE REAL BOOK OF REAL ESTATE
# n•
# text = "Here is an example: AxZ BxC yDx EfG-v"
#
# # Define a regex pattern to detect a single character 'x' in between two letters
# # pattern = r'[A-Za-z]-[A-Za-z]'
# pattern = r'-'
#
# # Use re.findall() to find all occurrences of the pattern
# matches = re.findall(pattern, text)
# # replacing the patter
# newtext = re.sub(pattern,'',text)
# print(newtext)
#
# # Print the matches
# print(matches)

# text = "TheREAL Book \nof \nReal Estate9781593155322_FM:real estate_new  3/25/09  3:52 PM  Page i', '9781593155322_FM:real estate_new  3/25/09  3:52 PM  Page ii\nThis page intentionally left blank ', 'The REAL Book \nof \nREAL EXPERTS. REAL STORIES. REAL LIFE.\nRobert Kiyosaki\nReal Estate9781593155322_FM:real estate_new  3/25/09  3:52 PM  Page iii', 'Copyright © 2009 by Robert T. Kiyosaki\nPublished by Vanguard PressAll rights reserved. No part of this publication may be reproduced, stored in a retrieval \nsystem"
# print(type(text))



# text = "TheREAL Book \of \Real Estate9781593155322_FM:real estate_new  3/25/09  3:52 PM  Page i'"
# patt = r'\\'
# res = re.sub(patt,'',text)
# text = res
# print(text)
# Input text containing newline characters
# text = "This is a\nsample text\nwith newline characters."

# Define a regex pattern to match newline characters
# pattern = r'\n'
# pattern = r'\\n'
# x = re.compile(pattern)
# print(x)
#
# # Replace newline characters with a space
# # result = re.sub(pattern, ' ', text)
# result = re.sub(pattern, '', txt)
#
# # Print the result
# print(result)
# print(type(result))