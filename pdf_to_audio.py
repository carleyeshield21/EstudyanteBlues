import pyttsx3
import PyPDF2

with open("the Real book of Real estate - robert kiyosaki.pdf", 'rb') as pdf:
    reader = PyPDF2.PdfReader(pdf, strict=False)
    pdf_text = []

    pages = 0
    for page in reader.pages:
        content = page.extract_text()
        pdf_text.append(content)
        pages += 1
print(pages)

# pages = PyPDF2.PdfReader.getPage()
# text = pages.extractText()

pdf_text_to_string = str(pdf_text)

text_file = open('raw_pdf_file.txt', 'w')
text_file.writelines(pdf_text_to_string)


speaker = pyttsx3.init()
speaker.say('How are you doing?')
speaker.runAndWait()