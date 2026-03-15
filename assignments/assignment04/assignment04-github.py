# Lab Instruction : https://vlegalwaymayo.atu.ie/mod/page/view.php?id=1393877
# Lab with similar ask: https://vlegalwaymayo.atu.ie/pluginfile.php/1835869/mod_url/intro/Lab04.3%20using%20the%20package.pdf

#Write a program in python that will read a file from a repository, 
#The program should then replace all the instances of the text "Andrew" with your name. 
#The program should then commit those changes and push the file back to the repository (You will need authorisation to do this).

# Author: David Scally
# Reference: Completed with Github copilot assistance + referring to lab
# https://pygithub.readthedocs.io/en/latest/introduction.html
# https://pygithub.readthedocs.io/en/latest/examples.html
# https://pygithub.readthedocs.io/en/latest/reference.html

# pip install pygithub
from github import Github
from config import config as cfg

# GitHub API URL of the file - not needed when using the PyGithub library, but included here for reference
#url = "https://api.github.com/repos/Mr-Scarf/web-services-and-applications/contents/assignments/assignment04/andrew.txt"




# Get GitHub token from config file
apikey = cfg["githubkey"]

# Connect to GitHub
g = Github(apikey)

# Get the repository
repo = g.get_repo("Mr-Scarf/web-services-and-applications")

# Get the file
file = repo.get_contents("assignments/assignment04/andrew.txt")

# Read the file content
file_content = file.decoded_content.decode("utf-8")

print("Original Content:")
print(file_content)

# Replace "Andrew" with "David"
updated_content = file_content.replace("Andrew", "David")

print("Updated Content:")
print(updated_content)


# Update the file on GitHub
repo.update_file(file.path, "Update file", updated_content, file.sha)
