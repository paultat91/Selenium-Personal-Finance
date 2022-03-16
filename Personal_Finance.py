#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 15 12:42:21 2022

@author: paul
"""

import selenium as s
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from pykeepass import PyKeePass

def string_to_float(Str):
    num = ''
    for i in range(len(Str)):
        if Str[i]!=',' and Str[i]!='$':
            num +=  Str[i]           
    num = float(num)
    return num

def get_total(Dict):
    total = 0
    for value in Dict.values():
        if value != []:
            total += string_to_float(value[0])    
    return total

class web(object):
    
    def __init__(self, headless=True):
        
        KeePass = input("Enter KeePass: ")
        self.kp = PyKeePass('/home/paul/Documents/Passwords.kdbx', password=KeePass)
        
        # selenium setup
        o = s.webdriver.FirefoxOptions()
        if headless:
            o.add_argument('-headless')
        self.driver = s.webdriver.Firefox(options=o)
        return
    
    def quit_web(self):
        self.driver.quit()
        return
    
    def get_BOA_balance(self):
        entry = self.kp.find_entries(title='BOA', first=True)
        username = entry.username
        password = entry.password
        
        # go to bank
        print("Going to Bank of America...")
        self.driver.get(entry.url)
        
        # sign in
        current_url = self.driver.current_url
        user_input = self.driver.find_element_by_name("onlineId1")
        password_input = self.driver.find_element_by_name("passcode1")
        user_input.send_keys(username)
        password_input.send_keys(password)
        sign_in_button = self.driver.find_element_by_xpath("/html/body/div[1]/div/div/section[2]/div/div/div[2]/div/div[4]/div[1]/div/div/form/div[1]/div/div[1]/div[6]/button/span[1]")
        sign_in_button.click()
        WebDriverWait(self.driver, 20).until(EC.url_changes(current_url))
        print("Sign in Successful...")
          
        sleep(10)
        
        # get BOA_balance 
        print("Getting BOA Balance...")
        BOA_balance = self.driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/ul/li/div[1]/div[1]/span").text    
        print("Balanced BOA Recieved...")
        
        # get Merrill_balance 
        print("Getting Merrill Balance...")
        Merrill_balance = self.driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/div[3]/div/li/div[1]/div[1]/span").text    
        print("Balanced Merrill Recieved...")
        
        del(username, password)
        return BOA_balance, Merrill_balance
        
    def get_M1_balance(self):
        entry = self.kp.find_entries(title='M1', first=True)
        username = entry.username
        password = entry.password   
               
        # go to M1
        print("Going to M1...")
        self.driver.get(entry.url)
        
        sleep(10)
        
        # sign in
        current_url = self.driver.current_url
        user_input = self.driver.find_element_by_name("username")
        password_input = self.driver.find_element_by_name("password")
        user_input.send_keys(username)
        password_input.send_keys(password)
        sign_in_button = self.driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div[2]/div/div/form/div[4]/div/button")
        sign_in_button.click()
        WebDriverWait(self.driver, 20).until(EC.url_changes(current_url))
        print("Sign in Successful...")
        
        # get M1_balance 
        print("Getting BOA Balance...")
        M1_balance = self.driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div[2]/div/div[2]/div[1]/div[4]/div[1]/h1").text    
        print("Balanced BOA Recieved...")
        return M1_balance

        # get usr/pw
        entry = self.kp.find_entries(title='BOA', first=True)
        username = entry.username
        password = entry.password
        
        # go to bank
        print("Going to Bank of America...")
        self.driver.get(entry.url)
        
        # sign in
        current_url = self.driver.current_url
        user_input = self.driver.find_element_by_name("onlineId1")
        password_input = self.driver.find_element_by_name("passcode1")
        user_input.send_keys(username)
        password_input.send_keys(password)
        sign_in_button = self.driver.find_element_by_xpath("/html/body/div[1]/div/div/section[2]/div/div/div[2]/div/div[4]/div[1]/div/div/form/div[1]/div/div[1]/div[6]/button/span[1]")
        sign_in_button.click()
        WebDriverWait(self.driver, 20).until(EC.url_changes(current_url))
        print("Sign in Successful...")
        sleep(10)
        # get BOA_balance 
        print("Getting BOA Balance...")
        BOA_balance = self.driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/ul/li/div[1]/div[1]/span").text    
        print("Balanced BOA Recieved...")
        
        # get Merrill_balance 
        print("Getting Merrill Balance...")
        Merrill_balance = self.driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/div[3]/div/li/div[1]/div[1]/span").text    
        print("Balanced Merrill Recieved...")
        
        del(username, password)
        return BOA_balance, Merrill_balance
    
    def get_Vanguard_balance(self):
        entry = self.kp.find_entries(title='Vanguard', first=True)
        username = entry.username
        password = entry.password   
        
        # go to Vanguard
        print("Going to Vanguard...")
        self.driver.get(entry.url)
        
        # sign in
        current_url = self.driver.current_url
        user_input = self.driver.find_element_by_name("USER")
        password_input = self.driver.find_element_by_name("PASSWORD-blocked")
        user_input.send_keys(username)
        password_input.send_keys(password)
        sign_in_button = self.driver.find_element_by_css_selector(".vui-button")
        sign_in_button.click()
        WebDriverWait(self.driver, 30).until(EC.url_changes(current_url))
        print("Sign in Successful...")
          
        sleep(20)
      
        # get Vanguard_balance 
        print("Getting Vanguard Balance...")
        Vanguard_balance = self.driver.find_element_by_xpath("/html/body/secure-overview-root/pssn-personal-secure-nav/div/div[1]/div[1]/div/div[1]").text    
        print("Balanced Vanguard Recieved...")
        return Vanguard_balance
    
    def get_GreatLakes_debt(self):
        entry = self.kp.find_entries(title='Great Lakes', first=True)
        username = entry.username
        password = entry.password      
               
        # go to Great Lakes
        print("Going to Great Lakes...")
        self.driver.get(entry.url)
        
        # sign in
        current_url = self.driver.current_url
        user_input = self.driver.find_element_by_name("username")
        user_input.send_keys(username)
        sign_in_button = self.driver.find_element_by_css_selector("#authenticate")
        sign_in_button.click()
        pin_input = self.driver.find_element_by_name("pinNumber")
        pin_input.send_keys(entry.notes)
        sign_in_button = self.driver.find_element_by_css_selector("#authenticate")
        sign_in_button.click()
        password_input = self.driver.find_element_by_name("password")
        password_input.send_keys(password)
        sign_in_button = self.driver.find_element_by_css_selector("#authenticate")
        sign_in_button.click()
        WebDriverWait(self.driver, 10).until(EC.url_changes(current_url))
        print("Sign in Successful...")
        
        sleep(10)
      
        # get GreatLakes_balance 
        print("Getting Great Lakes Debt...")
        GreatLakes_debt = self.driver.find_element_by_css_selector("#current-balance").text    
        print("Great Lakes Debt Recieved...")
        return GreatLakes_debt

    def get_Discover_debt(self):
        entry = self.kp.find_entries(title='Discover', first=True)
        username = entry.username
        password = entry.password      
             
        # go to Discover
        print("Going to Discover...")
        self.driver.get(entry.url) 
        
        sleep(10)
        
        # sign in
        current_url = self.driver.current_url
        user_input = self.driver.find_element_by_css_selector("#userid-content")
        password_input = self.driver.find_element_by_css_selector("#password-content")
        sleep(10)
        user_input.send_keys(username)
        password_input.send_keys(password)
        sign_in_button = self.driver.find_element_by_css_selector("input.btn-primary:nth-child(3)")
        sign_in_button.click()
        WebDriverWait(self.driver, 10).until(EC.url_changes(current_url))
        print("Sign in Successful...")
        
        sleep(10)
      
        # get Discover_debt 
        print("Getting Discover Debt...")
        Discover_debt = self.driver.find_element_by_xpath("/html/body/div[1]/main/div[4]/div[1]/div[1]/div[1]/p[1]/span").text    
        print("Discover Debt Recieved...")
        return Discover_debt
    
    def get_Robinhood_balance(self):
        entry = self.kp.find_entries(title='Robinhood', first=True)
        username = entry.username
        password = entry.password      
            
        # go to Robinhood
        print("Going to Robinhood...")
        self.driver.get(entry.url)
        
        sleep(10)
        
        # sign in
        current_url = self.driver.current_url
        user_input = self.driver.find_element_by_name("username")
        password_input = self.driver.find_element_by_name("password")
        user_input.send_keys(username)
        password_input.send_keys(password)
        sign_in_button = self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div/div/div/div/form/footer/div[1]/div/button/span/span/span")
        sign_in_button.click()
        WebDriverWait(self.driver, 10).until(EC.url_changes(current_url))
        print("Sign in Successful...")
        
        sleep(10)
      
        # get Robinhood_balance 
        print("Getting Robinhood Balance...")
        Robinhood_balance = self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div/div/div/div/form/footer/div[1]/div/button").text    
        print("Balanced Robinhood Recieved...")
        return Robinhood_balance
    
    def get_Sallie_debt(self):
        entry = self.kp.find_entries(title='Sallie Mae', first=True)
        username = entry.username
        password = entry.password      
            
        # go to Sallie Mae
        print("Going to Sallie Mae...")
        self.driver.get(entry.url)
        
        sleep(10)
        
        # sign in
        current_url = self.driver.current_url
        user_input = self.driver.find_element_by_name("UserID")
        password_input = self.driver.find_element_by_name("Password")
        user_input.send_keys(username)
        password_input.send_keys(password)
        sign_in_button = self.driver.find_element_by_css_selector("#button_1142036278")
        sign_in_button.click()
        WebDriverWait(self.driver, 10).until(EC.url_changes(current_url))
        print("Sign in Successful...")
        
        sleep(20)
      
        # get Sallie debt 
        print("Getting Sallie Mae debt...")
        Sallie_debt = self.driver.find_element_by_name("selen_current_total_balance").text    
        print("Sallie Mae Debt Recieved...")
        return Sallie_debt
    
    def get_all_balances(self):
        Balances = {'BOA_balance': [], 'Merrill_balance': [], 'M1_balance': [], 'Vanguard_balance': [], 'Robinhood_balance': []}
        Debts = {'Sallie_debt': [],'GreatLakes_debt': [], 'Discover_debt': []}
    
        BOA_balance, Merrill_balance = self.get_BOA_balance()
        Balances["BOA_balance"].append(BOA_balance)
        Balances["Merrill_balance"].append(Merrill_balance)
        
        Vanguard_balance = self.get_Vanguard_balance()
        Balances["Vanguard_balance"].append(Vanguard_balance)
        
        #M1_balance = self.get_M1_balance()
        #Balances["M1_balance"].append(M1_balance)
    
        #Robinhood_balance = self.get_Robinhood_balance()
        #Balances["Robinhood_balance"].append(Robinhood_balance)
    
        GreatLakes_debt = self.get_GreatLakes_debt()
        Debts["GreatLakes_debt"].append(GreatLakes_debt)
    
        Discover_debt = self.get_Discover_debt()
        Debts["Discover_debt"].append(Discover_debt)
        
        Sallie_debt = self.get_Sallie_debt()
        Debts["Sallie_debt"].append(Sallie_debt)
    
        print("")
        print("BOA Balance is: ", BOA_balance) 
        print("Merrill Balance is: ", Merrill_balance) 
        print("Vanguard Balance is: ", Vanguard_balance)
        #print("M1 Balance is: ", M1_balance)
        #print("Robinhood Balance is: ", Robinhood_balance)
        print("Great Lakes Debt is: ", GreatLakes_debt)
        print("Discover Debt is: ", Discover_debt)       
        print("Sallie Mae Debt is: ", Sallie_debt)       
        return Balances, Debts

if __name__=="__main__":
    w = web(headless=False)
    Balances, Debts = w.get_all_balances()   
    Total_Balance = round(get_total(Balances),2)
    Total_Debt = round(get_total(Debts),2)
    w.quit_web() 
     
    print("")    
    print("Your total balance is: ", Total_Balance)
    print("Your total debt is: ", Total_Debt)
    

    