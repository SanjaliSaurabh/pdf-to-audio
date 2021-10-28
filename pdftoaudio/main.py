# importing the modules
import PyPDF2
import pyttsx3

# path of the PDF file
book = open('E:\python\Web Developement\pdftoaudio\Cracking_the_Coding_Interview_6th_Editio.pdf', 'rb')

# creating a PdfFileReader object
pdfReader = PyPDF2.PdfFileReader(book)

# the page with which you want to start
# this will read the page of 25th page.
from_page = pdfReader.getPage(24)

# extracting the text from the PDF
text = from_page.extractText()

# reading the text
speak = pyttsx3.init()
speak.say(text)
speak.runAndWait()