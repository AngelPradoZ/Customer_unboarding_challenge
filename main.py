import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
customer_excel= pd.read_csv("customer-onboarding-challenge.csv")
driver = webdriver.Chrome()
options= webdriver.ChromeOptions()
driver.get("https://developer.automationanywhere.com/challenges/automationanywherelabs-customeronboarding.html")
for index,row in customer_excel.iterrows():
    customername = row["Company Name"]
    username = driver.find_element(By.XPATH,'//input[@id="customerName"]')
    username.send_keys(customername)

    customerid= row["Customer ID"]
    id = driver.find_element(By.XPATH,'//input[@id="customerID"]')
    id.send_keys(customerid)

    contact= row["Primary Contact"]
    primary = driver.find_element(By.XPATH,'//input[@id="primaryContact"]')
    primary.send_keys(contact)

    address= row["Street Address"]
    str = driver.find_element(By.XPATH,'//input[@id="street"]')
    str.send_keys(address)

    addresss= row["City"]
    cty = driver.find_element(By.XPATH,'//input[@id="city"]')
    cty.send_keys(addresss)

    code= row["Zip"]
    zip = driver.find_element(By.XPATH,'//input[@id="zip"]')
    zip.send_keys(code)

    email= row["Email Address"]
    ad = driver.find_element(By.XPATH,'//input[@id="email"]')
    ad.send_keys(email)

    state_excel = row['State']
    state = driver.find_element(By.XPATH,'//select[@id="state"]')
    state.click()
    state = driver.find_element(By.XPATH,f'//option[@value="{state_excel}"]')
    state.click()

    offer= row["Offers Discounts"]
    if offer == "YES":
        discount = driver.find_element(By.XPATH,'//input[@id="activeDiscountYes"]')
        discount.click()
    
    else : 
        discount = driver.find_element(By.XPATH,'//input[@id="activeDiscountNo"]')
        discount.click()

    nda = row["Non-Disclosure On File"]
    if nda == "YES":
        disclo = driver.find_element(By.XPATH,'//input[@id="NDA"]')
        disclo.click()

    button = driver.find_element(By.XPATH,'//button[@id="submit_button"]')
    button.click()

input("wait")