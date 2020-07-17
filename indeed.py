import requests
from bs4 import BeautifulSoup

LIMIT = 50    #한페이지에 50개 \씩 나오게 설정했으니까

URL = f"https://www.indeed.com/jobs?q=python&limit={LIMIT}"

def extract_indeed_pages():
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


def extract_indeed_jobs(last_page):
  for page in range(last_page):
    result = requests.get(f"{URL}&start={page*LIMIT}")

    print(result.status_code)