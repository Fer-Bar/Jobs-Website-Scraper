import requests
from bs4 import BeautifulSoup
import time

# Le preguntamos al usuario las tecnologías con las que no este familiarizado
# para filtrar ofertas de empleo adecuadas a las habilidades del usuario
unfamiliar_skills = input('Put some skills that you are not familiar with: ').split(' ') # Use spaces between every unfamiliar skill that you have
print(f'Filrering out {unfamiliar_skills}...')

def find_jobs():
    url = ('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=')
    html_text = requests.get(url).text
    soup = BeautifulSoup(html_text, 'lxml')

    jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')
    for index, job in enumerate(jobs):
        published_date = job.find('span', class_='sim-posted').span.text
        if 'few' in published_date:
            company_name = job.find('h3', class_='joblist-comp-name').text.replace(' ', '')
            skills = job.find('span', class_='srp-skills').text.replace(' ', '')
            more_info = job.header.h2.a['href']
            # Ponemos todas las habilidades requeridas en una lista
            skills_list = skills.strip().split(',') 
            # Si no esta familiarizado con x tecnología requirida en la oferta de trabajo se descarta 
            if (all(unf_skill not in skills_list for unf_skill in unfamiliar_skills)):
                with open(f'posts/{index}.txt', 'w') as f:
                    f.write(f'Company Name: {company_name.strip()} \n')
                    f.write(f'Skills required: {skills.strip()} \n')
                    f.write(f'More Info: {more_info} ')
                print(f'File Saved: {index} ')

if __name__ == '__main__':
    while True:
        find_jobs()
        time_wait = 60 # El formato es en minutos.
        print(f'Waiting {time_wait} minutes for the next scrap...')
        time.sleep(time_wait * 60)