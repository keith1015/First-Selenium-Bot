from splinter import Browser

#My first bot. Opens browser and navigates to facebook. It then logs in for me. 

with Browser('chrome') as browser:
    # Visit URL
    url = "https://www.facebook.com/"
    browser.visit(url)

    #fills out login information
    browser.fill('email', '#')
    browser.fill('pass', '#')  

    #locates login button and clicks
    button = browser.find_by_id('loginbutton')
    button.click()