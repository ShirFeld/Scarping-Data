
import requests
from bs4 import BeautifulSoup  #extract the data (html , xml )easily
import json


url = "https://informatica.gr8people.com/jobs?utm_medium=Direct"
response = requests.get(url) #200

soup = BeautifulSoup(response.text, 'html.parser') #structured, parse HTML files
table = soup.find('table')
jobs_list = []
jobs_description =[]



"""
This function will get a url and return the description of the job
"""
def find_description(url):
    response = requests.get(url)  # 200
    soup2 = BeautifulSoup(response.text, 'html.parser')
    job_article = soup2.find('article')
    return job_article.text


"""
Loop over the jobs table and extract the fields I need (title, city ,country ,description)
"""
for jobs in table.find_all('tbody'):
    rows = jobs.find_all('tr')
    for row in rows:
        name = row.find_all('td')[0].text  # job title
        # job_description  = row.find_all('td')[2].text
        location = row.find_all('td')[3].text
        job_id = row.find_all('td')[1].text


        name = name.strip()
        job_id = job_id.strip()
        # job_description = job_description.strip()
        job_description = 'https://informatica.gr8people.com/jobs/' +job_id +"/"+name
        print(job_description)

        location = location.strip()
        separator = ','
        country = location.split(separator, 1)[0] #gives us the first word = country
        result2 = location[len(country):]

        # for now the job description will be the link to the page
        #jobs_list.append({'Title': name,'job_description': job_description, 'Country': country , 'City' : result2})
        good = find_description(job_description).strip();
        good = good.replace("\n", "")
        good = good.replace("\t", "")

        jobs_list.append({'Title': name,'job_description':good , 'Country': country , 'City' : result2})



# print(find_description(urls[0]))


# print(jobs_list)

with open('json_data', 'w') as json_file:
    json.dump(jobs_list, json_file, indent=2)



