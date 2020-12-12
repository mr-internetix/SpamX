# imporitng modules
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import pyautogui
from time import sleep

#showing details about program
print(" welcome to SpamX")
#insta gram code
def InstagramLogin():
    # Enter Your Email ID And Password
    user=insta_id
    password=insta_pass

    # Opening Facebook.
    driver.get('https://www.instagram.com/')
    time.sleep(1)

    # Entering Email and Password
    username_box=driver.find_element_by_name("username")
    username_box.send_keys(user)
    time.sleep(1)

    password_box=driver.find_element_by_name("password")
    password_box.send_keys(password)

    # Pressing The Login Button
    login_box=driver.find_element_by_css_selector("button.sqdOP.L3NKy.y3zKF")
    login_box.click()
    time.sleep(5)

    save_button=driver.find_element_by_css_selector(
        "button.sqdOP.L3NKy.y3zKF")
    save_button.click()
    time.sleep(5)

    not_button=driver.find_element_by_css_selector("button.aOOlW.HoLwm")
    not_button.click()
    time.sleep(5)

    pratik=driver.find_element_by_xpath("//input[@type='text']")
    pratik.send_keys(victim)
    time.sleep(1)
    pyautogui.press('enter')
    pyautogui.press('enter')
    time.sleep(3)
    driver.find_element_by_css_selector(
        "button.sqdOP.L3NKy._4pI4F._8A5w5").click()

        
# scripting program
insta_id = input("Enter your insta id =>")
insta_pass = input("Enter your password =>")
victim = input("Enter victim insta id => ")
text = input("Enter the text you want to spam => ")
count  = int(input("No Of Message => "))

# using selenium as a driver
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
InstagramLogin()
for _ in range(count):
    pyautogui.typewrite(text)
    pyautogui.press("enter")
    time.sleep(1)
   
def exit():
    driver.quit()

exit()


