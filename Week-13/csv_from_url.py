import requests

csv_url = 'https://raw.githubusercontent.com/realpython/python-data-cleaning/master/Datasets/BL-Flickr-Images-Book.csv'

req = requests.get(csv_url) # Download the file and save it to the variable req
url_content = req.content # Get the content of the response
csv_file = open('Week-13/downloaded.csv', 'wb') # Create a new file or overwrite existing file
csv_file.write(url_content) # Write the content of the response to the new file
csv_file.close()