#-*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
from flask import Flask, render_template,request
app = Flask(__name__)

@app.route('/')
@app.route('/<string:answer>')
def main(answer=None):
    song_name = answer
    return render_template('main.html',render_answer = song_name)
@app.route('/lyrics')
def lyrics():
    data = request.args.get('input1')
    lyrics_url = 'https://www.google.com/search?q=' + data + '+ 가사' + '&rlz=1C1NDCM_koKR800KR800&oq=%ED%8C%94%EB%A0%88%ED%8A%B8+%EA%B0%80%EC%82%AC&aqs=chrome..69i57j0.1742j0j9&sourceid=chrome&ie=UTF-8'
    res =requests.get(lyrics_url)
    html = res.text
    print('connection: ',res.status_code)
    soup = BeautifulSoup(html, 'html.parser')
    lyrics = soup.select('div.hwc')

    return render_template('song.html',lyrics=lyrics)
