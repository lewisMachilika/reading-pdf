import pyttsx3
import PyPDF2
from tkinter.filedialog import *

book = askopenfilename()
pdfreader = PyPDF2.PdfFileReader(book)
pages = pdfreader.numPages

for number in range (1,pages):
    page =  pdfreader.getPage(number)
    text = page.extractText()
    print(text)
    player = pyttsx3.init()
    player.say(text)
    player.runAndWait()