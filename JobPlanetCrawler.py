import requests
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
driver = webdriver.Chrome('/Users/SGC/Desktop/Job_Planet_Crawler/chromedriver')
PAGE=1
def get_soup(search='python',start_year=0,end_year=0,start_star=0,end_star=5,page=1):
    start_star=start_star*10
    end_star=end_star*10
    URL=f"https://www.jobplanet.co.kr/job/search?page={PAGE*page}&yoe={start_year}%3B{end_year}&q={search}&rs={start_star}%3B{end_star}"
    driver.implicitly_wait(1)
    driver.get(URL)
    mycss=driver.find_element_by_css_selector('a > p.jobs_title')
    #jobs_title을 찾을때 까지 대기
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


def get_job_title(i):
    next_botton=driver.find_element_by_xpath(f'//*[@id="job_search_app"]/div/div[2]/div[1]/div[2]/ul/li[{i}]').click()
                                                    
    titles=driver.find_element_by_xpath('//*[@id="job_search_app"]/div/div[2]/div[2]/div[1]/div/div[2]/div/div/div[1]/h1')
    #titles=soup.select_one('div.lft > h1').get_text(strip=True)
    return titles.text

def get_job_card(search='python',start_year=0,end_year=0,start_star=0,end_star=5,page=1):
    start_star=start_star*10 #링크의 점수가 10단위이므로 *10 해주기
    end_star=end_star*10#위와 같음.
    URL=f"https://www.jobplanet.co.kr/job/search?page={PAGE*page}&yoe={start_year}%3B{end_year}&q={search}&rs={start_star}%3B{end_star}"
    driver.implicitly_wait(0.5)
    driver.get(URL)
    mycss=driver.find_element_by_css_selector('a > p.jobs_title')
    #jobs_title을 찾을때 까지 대기

    html=driver.page_source
    soup=BeautifulSoup(html,'lxml')
    #
    max_page=soup.select_one('#job_search_app > div > div.job_search_content > div.job_search_list > div.jply_pagination_ty1 > button:nth-child(5)').get_text()
    max_page=int(max_page)+1

    title=[]
    company=[]
    location=[]
    link=[]
    for max in range(1,2):
        URL=f"https://www.jobplanet.co.kr/job/search?page={PAGE*max}&yoe={start_year}%3B{end_year}&q={search}&rs={start_star}%3B{end_star}"
        driver.implicitly_wait(0.5)
        driver.get(URL)
        html=driver.page_source
        soup=BeautifulSoup(html,'lxml')
        for i in range(13,0,-1):
            try:
                next_botton=driver.find_element_by_xpath(f'//*[@id="job_search_app"]/div/div[2]/div[1]/div[2]/ul/li[{i}]').click()                                                
                titles=driver.find_element_by_xpath('//*[@id="job_search_app"]/div/div[2]/div[2]/div[1]/div/div[2]/div/div/div[1]/h1')
                #titles=soup.select_one('div.lft > h1').get_text(strip=True)
                title.append(titles.text)
                companys=driver.find_element_by_xpath('//*[@id="job_search_app"]/div/div[2]/div[2]/div[1]/div/div[2]/div/div/div[1]/div/div/div/span[1]/a')
                company.append(companys.text)
                locations=driver.find_element_by_xpath('//*[@id="job_search_app"]/div/div[2]/div[2]/div/div/div[2]/div/div/div[1]/div/div/div/span[3]/span')
                location.append(locations.text)
                links=driver.find_element_by_xpath('//*[@id="job_search_app"]/div/div[2]/div[1]/div[2]/ul/li[1]/a')['href']
                link.append(links.text)
                
            except:
                print('예외가 발생했습니다.')
                continue
   
    """
    for i in range(10,0,-1):
        title.append(get_job_title(i))
    """
    print(link)
    return {'title':title,'company':company,'location':location}
