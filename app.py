import os
import json
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
    
    json_return = {
        "message":{
            "text" : msg
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
