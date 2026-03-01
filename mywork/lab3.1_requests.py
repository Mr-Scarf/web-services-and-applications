import requests

#url = 'http://google.com'
#response = requests.get(url)
#print (response.text)

# Write the code to get the books from http://andrewbeatty1.pythonanywhere.com/books 


url = 'https://andrewbeatty1.pythonanywhere.com/books'
response = requests.get(url)

#print (response.text)


 #3. Convert that into a function and call it from inside a if __name__ == “__main__”: ************************ 

def readbooks():
    response = requests.get(url)
    if response.status_code != 200:
        return "Error fetching books"
    return response.json()
if __name__ == "__main__":
    #print(readbooks())

#4.Write the function for  find by id and test it (you need to write the testing code) ***********************

def readbooksid(id):
    geturl = url + '/' + str(id)
    response = requests.get(geturl)
    if response.status_code != 200:
        return "Error fetching book with id " + str(id)
    return response.json()
if __name__ == "__main__":    
    print(readbooksid(1686))


#5. write the code to create and test it (you need to write your own testing code)******************


def createbook(book):
    response = requests.post(url, json=book)
    if response.status_code != 200:
        return "Error creating book"
    return response.json()
if __name__ == "__main__":
    book = {
        "author": "Test Author",
        "title": "Test Book",
        "price": 12.99
    }

    print(createbook(book))

#6. Write the update function **********************

def updatebook(id, book):
    geturl = url + '/' + str(id)
    response = requests.put(geturl, json=book)
    if response.status_code != 200:
        return "Error updating book with id " + str(id)
    return response.json()   

if __name__ == "__main__":
    book = {
        "author": "Test Author",
        "title": "Test Book Updated",
        "price": 14.99
    }
    print(updatebook(1686, book))


# 7. Write the delete function********************
 
def deletebook(id):
    deleteurl = url + '/' + str(id)
    response = requests.delete(deleteurl)
    if response.status_code != 200:
        return "Error deleting book with id " + str(id)
    return response.json()

if __name__ == "__main__":
    print(deletebook(1686))