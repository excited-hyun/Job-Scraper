import requests
from bs4 import BeautifulSoup

LIMIT = 50    #한페이지에 50개 \씩 나오게 설정했으니까

URL = f"https://www.indeed.com/jobs?q=python&limit={LIMIT}"

def get_last_page():
  result = requests.get(URL)

  soup = BeautifulSoup(result.text, "html.parser")

  pagination = soup.find("div", {"class": "pagination"})

  links = pagination.find_all('a')
  #페이지 링크 받아옴
  pages= []
  for link in links[:-1]:
    pages.append(int(link.find("span").string)) #페이지 숫자만 떼서 리스트에 저장

  max_page = pages[-1]  #마지막 페이지

  return max_page

def extract_job(html):
  title = html.find("h2", {"class": "title"}).find("a")["title"]
  company = html.find("span", {"class": "company"})

  if company:
    company_anchor= company.find('a')

    if company_anchor is not None:
      company = str(company_anchor.string)
    else:
      company = str(company.string)
    company = company.strip()
  else:
    company = None

  location = html.find("div", {"class": "recJobLoc"})["data-rc-loc"]
  job_id = html["data-jk"]

  return {'title': title, 'company':company, 'location': location, "link": f"https://www.indeed.com/viewjob?jk={job_id}&from=web&vjs=3"}


def extract_jobs(last_page):

  jobs = []
  for page in range(last_page):
    print(f"Scrapping page {page}")
    result = requests.get(f"{URL}&start={0*LIMIT}")
    soup=BeautifulSoup(result.text, "html.parser")
    results = soup.find_all("div", {"class": "jobsearch-SerpJobCard"})

    for res in results:
      job = extract_job(res)
      jobs.append(job)
  return jobs

def get_jobs():
  last_page = get_last_page()
  jobs = extract_jobs(last_page)
  return jobs