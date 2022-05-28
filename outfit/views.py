from django.shortcuts import render
from bs4 import BeautifulSoup
import requests

# 생성해야 할 함수 목록
# 이미지 url 스크래핑, 이미지 객체 생성, 상세 페이지 url 스크래핑, 상세 페이지 객체 생성

# 구현 순서 -> 스크래핑 함수 구현 -> 객체 생성 함수 구현

# 참고: https://coding-kindergarten.tistory.com/37


def get_musinsa_request():
    url = "https://www.musinsa.com/mz/brandsnap?p=1"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup

# 이미지 url 스크래핑 함수 구현


def get_musinsa_images(soup):
    list_items = soup.select('div.articleImg>a>img')
    list_images = [i.attrs['src'] for i in list_items]
    return list_images


# 상세 페이지 스크래핑 함수 구현
def get_musinsa_links(soup):
    list_items = soup.select('div.articleImg>a')
    list_links = [i.attrs['href'] for i in list_items]
    return list_links

# 이미지 객체 생성 함수 구현

# 상세 페이지 객체 생성 함수 구현
