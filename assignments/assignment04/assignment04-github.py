# Lab Instruction : https://vlegalwaymayo.atu.ie/mod/page/view.php?id=1393877

#Write a program in python that will read a file from a repository, 
#The program should then replace all the instances of the text "Andrew" with your name. 
#The program should then commit those changes and push the file back to the repository (You will need authorisation to do this).
#I do not need to see your keys (see lab2)
#Handup: Push the program as assignment04-github.py to assignments repository.
#Marks: Marks will be given for the functionality and layout of the code; I do expect minimal comments to indicate you know what the program is doing.


# Lab Instruction : https://vlegalwaymayo.atu.ie/mod/page/view.php?id=1393877

# Write a program in python that will read a file from a repository
# Replace all instances of "Andrew" with my name
# Commit the updated file back to the repository

import requests
import json
import base64
from config import config as cfg

# GitHub API URL of the file
url = "https://api.github.com/repos/Mr-Scarf/web-services-and-applications/contents/assignments/assignment04/andrew.txt"

# Get GitHub token from config file
apikey = cfg["githubkey"]

# Authorisation header
headers = {
    "Authorization": "token " + apikey
}

# Step 1 - Get the file from GitHub
response = requests.get(url, headers=headers)
file_data = response.json()

print("File data retrieved from GitHub:")
print(file_data)
