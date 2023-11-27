from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random
from selenium.webdriver.common.by import By
# Replace <username> and <password> with your Instagram credentials

def likecom(driver,comments,lin):
    
    fln=len(lin)
    itr=9
    lnk=[]
    for i in lin:
        try:
            print(i.get_attribute("href"))
            lnk.append(i.get_attribute("href"))
        except:
            print("Could not find")
    print(len(lin),fln)
    while itr<len(lnk):
        try:
            link=lnk[itr]
            
            driver.implicitly_wait(4)

            driver.get(link)

            # Wait for the search results to load
            time.sleep(8)

            driver.implicitly_wait(7)


            # Like the post
            like_button = driver.find_elements(By.XPATH,'//*[@aria-label="Like"]')[1]
            like_button.click()

            # Wait for a random amount of time
            time.sleep(3)

            #Comment on the post
            comment_button = driver.find_elements(By.XPATH,'//*[@aria-label="Comment"]')[1]
            comment_button.click()

            # Wait for the comment field to load
            time.sleep(2)

            # Type a comment
            comment_field = driver.find_element(By.XPATH,'//*[@aria-label="Add a comment…"]')
            comment_field.send_keys(random.choice(comments))
            #comment_field.send_keys(Keys.RETURN)
            time.sleep(2)
            postcom=driver.find_element(By.XPATH,'//div[contains(text(), "Post")]')
            postcom.click()
            # Wait for a random amount of time
            time.sleep(random.randint(6,10))


            
            time.sleep(random.randint(6,10))
        except:
            print("Cant load comment")
            pass
        
        itr=itr+1
        


# username = "smaronbi"
# password = "No pass"



hashtags = open("hashtags.txt", "r")
hashtags=(hashtags.read()).split("\n")
comments=open("comments.txt", "r")
comments=(comments.read().replace("-","")).split("\n")
accounts=open("accounts.txt","r")
accounts=(accounts.read()).split("\n")




"""
can you write a python program where i will enter a csv file the code will extract each data and search in web using requests and then get the email using re module what find "@". after getting the email the code will write that beside the link column when that is finished then the file will close 
"""



for account in accounts:
    print(account)
    account=eval(account)
    username=account[0]
    password=account[1]



    options = webdriver.ChromeOptions()
    # options.add_argument('--disable-blink-features=AutomationControlled')
    # options.add_argument("--disable-extensions")
    # options.add_argument("--disable-gpu")
    options.add_argument("--incognito")

        #options.add_argument("--headless")
        #driver = webdriver.Chrome(options=options)
    driver = webdriver.Chrome(options=options)
    # Set up the Chrome driver

    driver.get("https://www.instagram.com/")

    # Wait for the page to load
    time.sleep(2)

    # Find the username and password fields and fill them in
    username_input = driver.find_element(By.NAME,"username")
    password_input = driver.find_element(By.NAME,"password")
    username_input.send_keys(username)
    password_input.send_keys(password)
    time.sleep(random.randint(3,6))
    # Submit the login form
    login_button = driver.find_element(By.XPATH,"//button[@type='submit']")
    login_button.click()

    # Wait for the page to load
    time.sleep(random.randint(10,15))

    driver.implicitly_wait(5)


    # Wait for the page to load
    time.sleep(random.randint(5,12))

    # Find the profile icon and click it
    try:
        btn=driver.find_element(By.XPATH,'//*[contains(text(),"Not Now")]')
        btn.click()
    except:
        pass
    time.sleep(random.randint(3,6))

    for i in range(0,len(hashtags)):
    # Find the search field and click it
        try:
            time.sleep(random.randint(6,10))
            search_field = driver.find_element(By.XPATH,'//*[@aria-label="Search"]')
            search_field.click()

            # Wait for the search field to load
            time.sleep(2)
            searchinput=driver.find_element(By.XPATH,'//input[@aria-label="Search input"]')
            # Type in a search query
            search_query = random.choice(hashtags)
            searchinput.send_keys(search_query)
            # searchinput.send_keys(Keys.RETURN)
            time.sleep(3)
            # try:
            # except:

            driver.implicitly_wait(3)
            st=driver.find_elements(By.XPATH,'//div[@role="none"]')[0]
            st.click()
            time.sleep(9)
            driver.implicitly_wait(5)
            lin=driver.find_elements(By.XPATH,'//div[@class="_aabd _aa8k  _al3l"]//a[@href]')
            likecom(driver,comments,lin)
        except:
            print("Can't Login......")
    
    







# time.sleep(random.randint(6,10))
# settings_button = driver.find_element(By.XPATH,'//*[@aria-label="Settings"]')
# settings_button.click()

# # Wait for the settings

# time.sleep(random.randint(5,10))
# logout=driver.find_element(By.XPATH,'//span[contains(text(), "Log out")]')
# logout.click()



# search = //*[@aria-label="Search"] then click
#then wait for some time then type 
#click links. = //a[@role="link"] starts from 20
#like button = //span[@class=""] 1st one
#COMMENT //*[@aria-label="Comment"] 2ND ONE
#TYPE SOMETHING THEN ENTER
#click on close = //*[@aria-label="Close"]
#then scroll down wait for some time 
#then click back to click link section now it will be 21th 
#do this from click link section for 20 times every time random time sleep
# at last search =//*[@aria-label="Settings"] then click
#following button = //a[@role="link"] on 7th index /// //*[contains(text(),'Follow')]
#following button = //div[@dir="auto"] index 11th
# search = //span[contains(text(), "Log out")] then click
# close button = //*[@aria-label="Close"]
#profile link = //a[@role="link"] on 5th index
#my following link= //a[@role="link"] on 10th index
#followers link = //a[@role="link"] on 9th index
#my following button = //*[contains(text(),'Following')]
#search  link click = //a[@role="link"] on 10th index
##############
#settings fot logout = //*[@aria-label="Settings"]
#logut button = 