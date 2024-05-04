from bs4 import BeautifulSoup
import requests
import time

print(" skills that are unfamiliar ")
unfav = input('>')

def solve():
    html_page = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text
    soup = BeautifulSoup(html_page, 'lxml')
    jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')

    for ind,job in enumerate(jobs):
        datef = job.find('span',class_= 'sim-posted').text.strip()
        if 'few' in datef: 
            job_name = job.find('h3', class_='joblist-comp-name').text.strip()
            skill = job.find('span', class_='srp-skills').text.strip()
            apply_link = job.header.h2.a['href']
            if unfav not in skill:
                with open(f'post/{ind}.txt','w') as f:
                    f.write(f'Company : {job_name} \n' )
                    f.write(f'Skills : {skill} \n' )
                    f.write(f'Link : {apply_link} \n' )
                print(' file saved ')

if __name__ == '__main__':
        while True:
            solve()
            time_wait = 10
            print(f'waiting {time_wait} min..')
            time.sleep(time_wait*10)