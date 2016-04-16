from selenium import webdriver#TODO: Import the module that will allow you to use Selenium
from selenium.webdriver.common.keys import Keys#TODO: Import the module that will allow you to use the up, down, left, and right keys on your keyboard

def play2048( times ):
    browser = webdriver.Firefox()
    browser.get('https://gabrielecirulli.github.io/2048/')    # 1. opens a game of 2048 from the URL: https://gabrielecirulli.github.io/2048/
    htmlElem = browser.find_element_by_tag_name('html')
    SCORE = browser.find_element_by_class_name('score-container')#inspected element on score box in firefox and found the class name
    
    for time in range(times):    # 2. uses the parameter 'times' to determine how many times your code will try to play the game
        htmlElem.send_keys(Keys.UP)    # 3. for each 'time', press these keys in this order: UP, RIGHT, DOWN, LEFT
        htmlElem.send_keys(Keys.RIGHT)    # 3. for each 'time', press these keys in this order: UP, RIGHT, DOWN, LEFT
        htmlElem.send_keys(Keys.DOWN)    # 3. for each 'time', press these keys in this order: UP, RIGHT, DOWN, LEFT
        htmlElem.send_keys(Keys.LEFT)    # 3. for each 'time', press these keys in this order: UP, RIGHT, DOWN, LEFT
    print('Score= '+SCORE.text)    # 4. print the final score after all tries to the screen 
