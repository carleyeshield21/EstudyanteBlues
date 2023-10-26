import re

# file = open('sample_text.txt')
file = open('raw_pdf_file.txt')
txt = str(file.readlines())
# print(type(txt))
# print(txt)

pattern1 = r'\\n' #creating a pattern to detect the breakline \n but this will still leave a single backslash to the output text
text1 = re.sub(pattern1, '', txt) #replacing the breakline with a single space, a single backslash will still remain in the output text
txt = text1 #assigning it the result to the original variable
print(txt)

pattern2 = r'\\' #creating a second pattern to detect the single backslash, in this code we will use a double backslash for a single backslash to
# avoid SyntaxError
text2 = re.sub(pattern2,'',txt)
txt = text2
print(txt)


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