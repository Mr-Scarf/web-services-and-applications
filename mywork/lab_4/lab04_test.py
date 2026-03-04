import requests

# A public URL so the API can fetch it
targeturl = "https://www.example.com"

# API endpoint that doesn’t require a key (free demo)
apiurl = "https://html2pdf.fly.dev/api/generate"

# JSON body telling it what to convert
data = {
    "html": targeturl  # Convert a URL by passing it as "html"
}

# Send the request as POST
response = requests.post(apiurl, json=data)

print("Status code:", response.status_code)
print("Content-Type:", response.headers.get("Content-Type"))

if response.status_code == 200:
    with open("books.pdf", "wb") as f:
        f.write(response.content)
    print("PDF saved as books.pdf")
else:
    print("Error:", response.status_code)