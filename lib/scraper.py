from turtle import ht

from bs4 import BeautifulSoup
import requests

# Headers to mimic a browser request
headers = {'user-agent': 'my-app/0.0.1'}

# Send a GET request
response = requests.get("https://flatironschool.com/our-courses/", headers=headers)

# Parse the HTML content
soup = BeautifulSoup(response.text, 'html.parser')

# Select and print course names
courses = soup.select('.heading-60-black.color-black.mb-20')
for course in courses:
    print(course.get_text(strip=True))


