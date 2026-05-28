import requests
from bs4 import BeautifulSoup
import csv

url = "https://realpython.github.io/fake-jobs/"
data = requests.get(url).text

soup = BeautifulSoup(data, "html.parser")

titles = soup.find_all('h2')
companies = soup.find_all('h3')
location = soup.find_all('p', attrs={"class":"location"})
job_urls= []

ju = soup.find_all('a',href=True)
for j in ju:
    if j.text == "Apply":
        job_urls.append(j.get('href'))

with open('jobs.csv', 'w', newline='') as csvfile:
    fieldnames = ['Job_Title', 'Company', 'Location', 'Job_Apply_URL']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for i in range(len(titles)):
        writer.writerow({'Job_Title': titles[i].text.strip(),
                         'Company': companies[i].text.strip(),
                         'Location': location[i].text.strip(),
                         'Job_Apply_URL': job_urls[i]})
    
