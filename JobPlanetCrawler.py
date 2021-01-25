import requests
import time
from bs4 import BeautifulSoup
from selenium import webdriver

driver = webdriver.Chrome('/Users/SGC/Desktop/Job_Planet_Crawler/chromedriver')
PAGE=1


def get_soup(search='python',start_year=0,end_year=0,start_star=0,end_star=5):
    start_star=start_star*10
    end_star=end_star*10
    URL=f"https://www.jobplanet.co.kr/job/search?page={PAGE}&yoe={start_year}%3B{end_year}&q={search}&rs={start_star}%3B{end_star}"
    print(URL)
    driver.get(URL)
    html=driver.page_source
    soup=BeautifulSoup(html,'lxml')
    return soup

def get_title(soup):
    title=[]
    links=soup.select('a > p.jobs_title')
    for link in links:
        title.append(link.get_text(strip=True))
    return title
    
def get_company(soup):
    company=[]
    companys=soup.select('a > p.jobs_company')
    for c in companys:
        company.append(c.get_text(strip=True))
    return company

def get_score(soup):
    score=[]
    scores=soup.select('a > p.jobs_text')
    for s in scores:
        score.append(s.get_text(strip=True))
    return score

def get_Job_Planet(soup):
    title=get_title(soup)
    company=get_company(soup)
    score=get_score(soup)
    return {'title':title,'company':company,'score':score}

