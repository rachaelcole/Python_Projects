'''
WEB SCRAPING

FreeCodeCamp.org - Web Scraping with Python - BeautifulSoup Crash Course by JimShapedCoding

We need to look at the HTML of the web page(s) we want to scrape. We search the HTML tags when scraping.

Packages used: BeautifulSoup4
'''

from bs4 import BeautifulSoup  # import BeautifulSoup library

with open('home.html', 'r') as html_file:  # opens home.html in read mode
    content = html_file.read()  # reads the html_file content
    soup = BeautifulSoup(content, "html.parser")  # Create BeautifulSoup object and define parser

    # SAMPLE 1
    courses_html_tags = soup.find_all("h5")  # Grab all h5 tags and store them in a list
    for course in courses_html_tags:  # Iterates through each item in tag list
        print(course.text)  # Prints the text inside the h5 tags; a list of courses on the webpage

    # SAMPLE 2
    course_cards = soup.find_all('div', class_='card')  # grabs all <div class="card"> tags

    for course in course_cards:
        course_name = course.h5.text
        course_price = course.a.text.split()[-1]
        print(f'{course_name} costs {course_price}')

