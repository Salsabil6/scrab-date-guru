import math

import requests
import bs4
import csv
from itertools import zip_longest

job_title_list = []
company_name_list = []
location_name_list = []
salary_list = []
skills_list = []
skill2_list = []
links_list = []
quality_list = []

result = requests.get('https://www.guru.com/d/freelancers/skill/iOS-App-Development/')
src = result.content
soup = bs4.BeautifulSoup(src, "html.parser")


jobs_count = (soup.find("h2", {"class": "secondaryHeading"})).find("label").text
jobs_count = int(jobs_count.split(" ")[0].replace(',', ''))

pages_count = math.ceil(jobs_count / 20)


page = 1
while page <= pages_count:
    result = requests.get('https://www.guru.com/d/freelancers/skill/iOS-App-Development/pg/{}/'.format(page))
    src = result.content
    soup = bs4.BeautifulSoup(src, "html.parser")
    company_name = soup.find_all("h3", {"class": "freelancerAvatar__screenName"})
    job_titles = soup.find_all('h2', {'class': 'serviceListing__title serviceListing__title--dark'})
    location_names = soup.find_all("span", {"class": "freelancerAvatar__location--country"})
    salary = soup.find_all("span", {"class": "earnings__amount"})
    job_skills = soup.find_all("div", {"class": "skillsList"})
    quality_of_company = soup.find_all("span", {"class": "freelancerAvatar__feedback"})

    page += 1


    for i in range(len(company_name)):
        print(i)
        try:
            job_title_list.append(job_titles[i].text.strip())
        except:
            job_title_list.append("")

        try:
            company_name_list.append(company_name[i].text.strip())
        except:
            company_name_list.append("")

        try:
            location_name_list.append(location_names[i].text.strip())
        except:
            location_name_list.append(location_names[i].text.strip())

        try:
            salary_list.append(salary[i].text.strip())
        except:
            salary_list.append("")

        try:
            skills_list.append(job_skills[i].text.strip())
        except:
            skills_list.append("")


        try:
            quality_list.append(quality_of_company[i].text.strip())
        except:
            quality_list.append("")


        links_list.append("https://www.guru.com/" + job_titles[i].find("a").attrs['href'])




    for link in links_list:
        result = requests.get(link)
        src = result.content
        soup = bs4.BeautifulSoup(src, "html.parser")
        # services = soup.find_all("h2", {"class": "serviceListing__title"})
        # service.append(services)
        skill2 = soup.find_all("span", {"class": "skillsList__skill"})
        skills2 = []
        for skill in skill2:
            skills2.append(skill.text)
        skill2_list.append(skills2)







# print(job_title, name, location_name, salaries, skills, quality, links, service, skill2)


file_list = [job_title_list, company_name_list, location_name_list, salary_list, skills_list, skill2_list, quality_list]
exported = zip_longest(*file_list)


with open("text.csv", "w") as myfile:
    wr = csv.writer(myfile)
    wr.writerow(["job titles", "company_name", "location_names", "salary", "skills", "skills2", "quality"])
    wr.writerows(exported)
