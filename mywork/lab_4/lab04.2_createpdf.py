#Lab instruction - https://vlegalwaymayo.atu.ie/pluginfile.php/1835868/mod_url/intro/Lab04.2%20API%20keys.pdf

import requests
import urllib.parse
from config import apikey # import the API key from the config.py file, which should contain a variable named 'apikey' with the value of your API key. This way, you can keep your API key secure and separate from your main code.

# Define the target URL and API key - need to get this from the API provider - in this case, HTML2PDF
targeturl = "https://andrewbeatty1.pythonanywhere.com/books"


# Define the API endpoint and parameters
apiurl = 'https://dash.html2pdf.app/v1/generate'

# Create the request URL with parameters
params = {'url': targeturl, 'apikey': apikey}

# Encode the parameters and construct the full request URL # ref: https://docs.python.org/3/library/urllib.parse.html#urllib.parse.urlencode
parsedparams = urllib.parse.urlencode(params)

# Construct the full request URL
requesturl = apiurl + '?' + parsedparams

response = requests.get(requesturl)
print(response.status_code)


#response = requests.get(apiurl, params=params) - # alternative way to send the GET request with parameters, requests will handle the encoding of parameters automatically

if response.status_code == 200:
    with open("books.pdf", "wb") as f:
        f.write(response.content)
    print("PDF saved as books.pdf")
else:
    print("Error:", response.status_code)