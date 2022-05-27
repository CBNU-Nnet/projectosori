from django.shortcuts import render
from bs4 import BeautifulSoup
import requests

# 생성해야 할 함수 목록
# 이미지 url 스크래핑, 이미지 객체 생성, 상세 페이지 url 스크래핑, 상세 페이지 객체 생성

# 구현 순서 -> 스크래핑 함수 구현 -> 객체 생성 함수 구현


def get_musinsa_request(key):
    result = []
    url = "https://www.musinsa.com/mz/brandsnap?p=1"

    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    print(type(soup))


# 이미지 url 스크래핑 함수 구현
# 참고: https://softwaree.tistory.com/74


def fetch_img_data():
    pass
    # soup.set 객체에 img 태그 안의 src 속성 값 저장
    # 0번째 요소는 스타일과 관련 없는 링크이므로 저장하지 않아야 함
    # soup.set = soup.find_all('img', {'src': ''})

    # 제대로 스크래핑되었는지 확인
    # for image in soup.set[1:]:
    # print(image['src'])

    # 상세 페이지 스크래핑 함수 구현

    # 이미지 객체 생성 함수 구현

    # 상세 페이지 객체 생성 함수 구현
