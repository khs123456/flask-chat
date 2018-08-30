import os
import json
import random
import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def hello():
    return '챗봇페이지 입니다!'
    
@app.route('/keyboard')
def keyboard():
    # keyboard 딕셔너리 생성
    keyboard = {
        "type" : "buttons",
        "buttons" : ["메뉴", "로또", "고양이", "영화"]
    }
    
    # 딕셔너리를 json으로 바꿔서 리턴 해주기 위한 코드
    json_keyboard = json.dumps(keyboard)
    return json_keyboard


# POST방식으로 URL에 안 찍히도록    
@app.route('/message', methods=['POST'])
def message():
    # content라는 key의 value를 msg에 json타입으로 저장
    msg = request.json['content']
    img_bool = False
    if msg == "메뉴":
        menu = ["20층", "멀캠식당", "꼭대기", "급식"]
        return_msg = random.choice(menu)
    elif msg == "로또":
        # range(1,46)을 반드시 list로 감싸줘야 원하는 형태가 된다.
        number = list(range(1,46))
        pick = random.sample(number,6)
        # list를 string으로 변환을 시켜줘야 return_msg가 될 자격이 생긴다.
        return_msg = str(pick)
    elif msg == "고양이":
        img_bool = True
        url = "https://api.thecatapi.com/v1/images/search?mime_type=jpg"
        req = requests.get(url).json()
        cat_url = req[0]['url']
    else:
        return_msg = "아직 지원하지 않습니다."
        
    if img_bool == True:
        json_return = {
            "message":{
                "photo": {
                    "url": cat_url,
                    "width": 720,
                    "height": 640
                }
            },
            "keyboard": {
                "type" : "buttons",
                "buttons" : ["메뉴", "로또", "고양이", "영화"]
            }
        }
    else:    
        json_return = {
            "message":{
                "text" : return_msg
            },
            "keyboard": {
                "type" : "buttons",
                "buttons" : ["메뉴", "로또", "고양이", "영화"]
            }
        }
    
    # jsonify도 json.dumps와 똑같은 기능을 한다. 취사선택하면 됨.
    return jsonify(json_return)
    
# 서버 실행 코드    
app.run(host=os.getenv('IP', '0.0.0.0'),port=int(os.getenv('PORT', 8080)))
