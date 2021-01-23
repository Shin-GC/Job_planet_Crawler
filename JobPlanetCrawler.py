import requests
import time
from bs4 import BeautifulSoup
from selenium import webdriver
driver = webdriver.Chrome('/Users/SGC/Desktop/Job_Planet_Crawler/chromedriver')
PAGE=1

def get_soup(search='python',start_year=0,end_year=0):
    URL=f"https://www.jobplanet.co.kr/job/search?page={PAGE}&yoe={start_year}%3B{end_year}&q={search}"
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

