import requests
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome('/Users/SGC/Desktop/Job_Planet_Crawler/chromedriver')
PAGE=1


def get_soup(search='python',start_year=0,end_year=0,start_star=0,end_star=5,page=1):
    start_star=start_star*10
    end_star=end_star*10
    URL=f"https://www.jobplanet.co.kr/job/search?page={PAGE*page}&yoe={start_year}%3B{end_year}&q={search}&rs={start_star}%3B{end_star}"
    print(URL)
    driver.implicitly_wait(10)
    driver.get(URL)
    mycss=driver.find_element_by_css_selector('a > p.jobs_title')
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

def get_max_page(soup):    
    max_page=soup.select_one('#job_search_app > div > div.job_search_content > div.job_search_list > div.jply_pagination_ty1 > button:nth-child(5)').get_text()
    max_page=int(max_page)+1
    return max_page

def get_link(soup):
    link=soup.select_one('#job_search_app > div > div.job_search_content > div.job_search_list > div.list > ul > li:nth-child(1) > a')['href']
    return link


link=get_link(get_soup())
sample=f'https://www.jobplanet.co.kr/{link}'
print(sample)