from django.shortcuts import render
from bs4 import BeautifulSoup
import requests

# 생성해야 할 함수 목록
# 이미지 크롤링, 이미지 객체 생성, 연결 링크 크롤링, 연결 링크 객체 생성

# 이미지 크롤링 함수 구현
# 참고: https://softwaree.tistory.com/74


def fetch_musinsa_data():
    result = []
    url = "https://www.musinsa.com/mz/brandsnap?p=1"

    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # soup.set 객체에 img 태그 안의 src 속성 값 저장
    # 0번째 요소는 스타일과 관련 없는 링크이므로 저장하지 않아야 함

    soup.set = soup.find_all('img[src]')

# 이미지 객체 생성 함수 구현


# 연결 링크 크롤링 함수 구현


# 연결 링크 객체 생성 함수 구현
