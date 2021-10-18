from bs4 import BeautifulSoup
import requests  # import the requests library module
import time

# ask user to enter an unfamiliar skill
unfamiliar_skill = input('Enter unfamiliar skill: ')
print(f'Filtering out {unfamiliar_skill}...')

# Define the scraping function
def find_jobs():
    # get the html text of the webpage and store it in a variable called 'html_text'
    html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=Industry&from=submit&clubJob=n&cboIndustry=27&gadLink=IT-Hardware/Networking').text
    soup = BeautifulSoup(html_text, "html.parser")
    jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')  # Get 1st job listings= by <li class="clearfix job-bx wht-shd-bx"> tag
    for index, job in enumerate(jobs):  # iterate through list of jobs
        publish_date = job.find('span', class_='sim-posted').span.text  # get publish date
        if 'today' in publish_date:  # only prints jobs posted today
            company_name = job.find('h3', class_='joblist-comp-name').text.replace(' ', '')  # get company name, remove white spaces
            skills = job.find('span', class_='srp-skills').text.replace(' ', '')  # get skills, remove white spaces
            link = job.header.h2.a['href']  # get link to job
            if unfamiliar_skill not in skills:  # filter out unfamiliar skill
                # Write job info to text file
                with open(f'posts/{index}.txt', 'w') as f:
                    f.write(f'Company name: {company_name.strip()} \n')
                    f.write(f'Required skills: {skills.strip()} \n')
                    f.write(f'More info: {link}')
                print(f'File saved: /posts/{index}.txt')



if __name__ == '__main__':
    while True:
        find_jobs()
        time_wait = 10
        print(f'Waiting {time_wait} minutes...')
        time.sleep(time_wait * 60)  # set program to run every 10 minutes
