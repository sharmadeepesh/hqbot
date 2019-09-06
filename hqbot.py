'''Importing all the necessary modules and libraries'''

import pyautogui                                                                                                        #for screen-captures
from PIL import Image, ImageFile, ImageDraw, ImageChops, ImageFilter, ImageEnhance                                      #for OCR Preprocessing
from pytesseract import *                                                                                               #OCR
import requests                                                                                                         #for sending requests
import string                                                                                                           #string module
from googlesearch import *                                                                                              #for google searches
import threading                                                                                                        #for parallel threading

pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"                     #Providing the path to Tesseract OCR directory



def text_extraction():                                                                          #This function captures screen in real time and processes it for OCR
	global text
	screenshot = pyautogui.screenshot()
	cropped = screenshot.crop((115,266,556,649))
	contrasted = ImageEnhance.Contrast(cropped).enhance(5.0)
	text=image_to_string(contrasted)
	ocr_text_parse()


                                                                                        #This function parses the OCR generated text into Question & Answers Strings
def ocr_text_parse():
	global text
	global question
	global answers
	clean_text=("".join([s for s in text.strip().splitlines(True) if s.strip()]))
	question = clean_text.split("?")[0]
	print(question)
	answers = clean_text.split("?")[1]
	answers=("".join([s for s in answers.strip().splitlines(True) if s.strip()]))
	answers = answers.split('\n')
	print(answers)
	find_url()


def find_url():                                                                                  #This function finds the top five URLs. Threading is used here
	global text
	global question
	global answers
	url=[]
	for j in search(question, stop=5):
		url.append(j)
	t1 = threading.Thread(count_calc(answers, url[0]))
	t2 = threading.Thread(count_calc(answers, url[1]))
	t3 = threading.Thread(count_calc(answers, url[2]))
	t4 = threading.Thread(count_calc(answers, url[3]))
	t5 = threading.Thread(count_calc(answers, url[4]))
	t1.start()
	t2.start()
	t3.start()
	t4.start()
	t5.start()
	t1.join()
	t2.join()
	t3.join()
	t4.join()
	t5.join()


def count_calc(answers, url):                                           #This function provides the most probable answer by scraping the website for given choices
	count=[1,1,1]
	for i in range(3):
		count[i]=requests.get(url).text.count(answers[i])
	maxnumber = max(count)
	if count[0]==maxnumber:
		draft_answer= answers[0]
	elif count[1]==maxnumber:
		draft_answer=answers[1]
	elif count[2]==maxnumber:
		draft_answer=answers[2]
	print(draft_answer)
        
if __name__ == "__main__":
        text_extraction()

