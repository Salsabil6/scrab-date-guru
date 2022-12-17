import requests
import lxml
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
soup = bs4.BeautifulSoup(src, "lxml")

company_name = soup.find_all("h3", {"class": "freelancerAvatar__screenName"})
job_titles = soup.find_all('h2', {'class': 'serviceListing__title serviceListing__title--dark'})
location_names = soup.find_all("span", {"class": "freelancerAvatar__location--country"})
salary = soup.find_all("span", {"class": "earnings__amount"})
job_skills = soup.find_all("div", {"class": "skillsList"})
quality_of_company = soup.find_all("span", {"class": "freelancerAvatar__feedback"})



for i in range(len(company_name)):
    job_title_list.append(job_titles[i].text.strip())
    company_name_list.append(company_name[i].text.strip())
    links_list.append("https://www.guru.com/" + job_titles[i].find("a").attrs['href'])
    location_name_list.append(location_names[i].text.strip())
    salary_list.append(salary[i].text.strip())
    skills_list.append(job_skills[i].text.strip())
    quality_list.append(quality_of_company[i].text.strip())




for link in links_list:
    result = requests.get(link)
    src = result.content
    soup = bs4.BeautifulSoup(src, "lxml")

    skill2 = soup.find_all("span", {"class": "skillsList__skill"})
    skills2 = []
    for skill in skill2:
        skills2.append(skill.text)
    skill2_list.append(skills2)

print(skill2_list)

# print(job_title, name, location_name, salaries, skills, quality, links, service, skill2)


file_list = [job_title_list, company_name_list, location_name_list, salary_list, skills_list, skill2_list, quality_list]
exported = zip_longest(*file_list)


with open("salsaa.csv", "w") as myfile:
    wr = csv.writer(myfile)
    wr.writerow(["job titles", "company_name", "location_names", "salary", "skills", "skills2", "quality"])
    wr.writerows(exported)
