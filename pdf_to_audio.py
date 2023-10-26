# import pyttsx3
# import PyPDF2
#
# with open("the Real book of Real estate - robert kiyosaki.pdf", 'rb') as pdf:
#     reader = PyPDF2.PdfReader(pdf, strict=False)
#     pdf_text = []
#
#     pages = 0
#     for page in reader.pages:
#         content = page.extract_text()
#         pdf_text.append(content)
#         pages += 1
# print(pages)
#
# pdf_text_to_string = str(pdf_text)
#
# text_file = open('raw_pdf_file.txt', 'w')
# text_file.writelines(pdf_text_to_string)
#
# speaker = pyttsx3.init()
# speaker.say('How are you doing?')
# speaker.runAndWait()

import re

text = "Hello, my email is example@email.com and my phone number is 123-456-7890."

# Find an email address
email_pattern = r'\S+@\S+'
email = re.search(email_pattern, text)
print("Email:", email.group() if email else "Not found")

# Find all phone numbers
# phone_pattern = r'\d{3}-\d{3}-\d{4}'
# phones = re.findall(phone_pattern, text)
# print("Phone Numbers:", phones)
#
# # Replace phone numbers with "REDACTED"
# redacted_text = re.sub(phone_pattern, "REDACTED", text)
# print("Redacted Text:", redacted_text)