# hqbot
<strong> A simple bot to automate answers in HQTrivia </strong>

<h3>What Is HQ Trivia</h3>
HQ Trivia is an online game that resembles the concept of "Who wants to be a Millionaire" and its various derivatives. 

The game airs on the official HQ Trivia smartphone application at specific timings. 

<h3>How It Works</h3>
This script OCRs the game real time for question and answers. Parses the generated strings for better processing. And, then uses web scraping to predict the most probable answer. It also uses the concept of Multithreading to improve the time efficiency of the script.

The script is still in making and takes more time to process than needed. This bot is  approximately 50-60% efficient in answering the questions.

![test_image](https://github.com/sharmadeepesh/hqbot/blob/master/Test%20Case.PNG?raw=true)

What it basically does is that it counts the number of times each answer appears in the top Five results in Google SERP. The script returns the possible answer for each result.

<h3>REQUIREMENTS</h3>
<ol>
  <li>pyautogui</li>
  <li>Pillow / PIL</li>
  <li>Pytesseract</li>                                                                                    
  <li>googlesearch</li>
</ol>

<strong>Note</strong> - The script is developed to run on a Windows Machine. However, the script is still compatible with Unix. Just change the directory of the Pytesseract OCR.

Add all the modules by entering "pip install -r Requirements.txt" in the terminal.

Windows users need to install PyTesseract as a standalone executable. <underline>(Add the module + Install as exe too)</underline>
Linux users need to download "tesseract-ocr" package using their system's package manager. </br>
<code>sudo apt-get install tesseract-ocr</code></br>
Linux users must also comment out the "Pytesseract Path Line from the code" otherwise it would raise an error.
