from bs4 import BeautifulSoup

with open('index.html' , 'r') as html_file:
    content = html_file.read()
    
    soup = BeautifulSoup(content,'lxml')
    cources_html = soup.find_all('h5')
    for course in cources_html:
        print(course.text)