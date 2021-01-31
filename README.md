# Job_planet_Crawler
잡플래닛 채용 공고를 수집하기 위한 크롤러 입니다!

## Method
##### 매개변수 값을 설정해주지 않을 경우 Default로 설정된 값으로 URL을 받아옵니다.
##### search='검색할 내용', start_year=연차 시작,end_yea= 끝 연차 [ 0, 0 일땐 신입], 
##### start_star=회사의 최소점수, end_star=최대점수 [0,0 일땐 전체] ,page=긁어올 페이지
* get_soup(search='python',start_year=0,end_year=0,start_star=0,end_star=5,page=1)

##### 제목을 가져오는 메서드
* get_title(soup)
##### 회사를 가져오는 메서드
* get_company(soup)
##### 회사 점수를 가져오는 메서드
* get_score(soup)
##### 페이지의 최대 페이지를 가져오는 메서드
* get_max_page(soup)

##### title,company,score의 세 값을 가져오는 함수를 모아둔 메서드로 Dictionary값이 리턴된다.
* get_Job_Planet(soup)


## 실행화면 [get_Job_Planet(get_soup())]
![실행화면](https://user-images.githubusercontent.com/58453569/106359609-22ad0100-6357-11eb-90a3-f129ec4242f1.PNG)
