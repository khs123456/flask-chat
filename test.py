import requests
import random
from bs4 import BeautifulSoup

url = "https://movie.naver.com/movie/running/current.nhn"
req = requests.get(url).text
doc = BeautifulSoup(req, 'html.parser')

# class가 tit인 dt 태그 아래에 있는 a 태그만 보고싶어(단 중간경로도 있으면 다 적어줘야한다.)
titles = doc.select('dt.tit > a')

# 평점 가져오기(copy selector 해온 것 중 div:nth-child(1)와 같이 자식 구조가 있을 때 div만 남기고 빼준다.)
stars = doc.select('#content > div.article > div > div.lst_wrap > ul > li > dl > dd.star > dl.info_star > dd > div > a > span.num')

# 예매율 가져오기
reserve = doc.select('#content > div.article > div > div.lst_wrap > ul > li > dl > dd.star > dl.info_exp > dd > div > span.num')

# 영화 포스터 이미지 가져오기
image = doc.select('div.thumb > a > img')

# TOP10 영화 딕셔너리 만들기
movie_dic = {}
for i in range(0,10):
    movie_dic[i] = {
        "title": titles[i].text,
        "star": stars[i].text,
        "reserve": reserve[i].text,
        # img태그 안의 src 속성 부분만 가져오기
        "img": image[i].get('src')
    }

# 하나의 영화만 pick해주기
pick_movie = movie_dic[random.randrange(0,10)]
print(pick_movie)

