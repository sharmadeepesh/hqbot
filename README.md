# hqbot
A simple bot to automate answers in HQTrivia

HQ Trivia is an online game that resembles the concept of "Who wants to be a Millionaire" and its various derivatives. 

The game airs on the official HQ Trivia smartphone application at specific timings. 

This script OCRs the game real time for question and answers. Parses the generated strings for better processing. And, then uses web scraping to predict the most probable answer. It also uses the concept of Multithreading to improve the time efficiency of the script.

The script is still in making and takes more time to process than needed. This bot is  approximately 50-60% efficient in answering the questions.

REQUIREMENTS -
pyautogui <br>
Pillow / PIL
Pytesseract                                                                                    
googlesearch

Note - The script is developed to run on a Windows Machine. However, the script is still compatible with Unix. Just change the directory of the Pytesseract OCR.

Windows users need to install PyTesseract as a standalone executable. (Add the module + Install as exe too)
