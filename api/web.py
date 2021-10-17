from flask import Flask, Response, request
from flask import Flask, render_template
from random import choice

app = Flask(__name__)


list=["让人迷茫的原因只有一个，那就是本该拼搏的年纪，想的太多，却做的太少！","你知道吗，你红尘梦醒的那一刻，是我看过的，最美丽的画面。",\
    "跟你在一起的时光都很耀眼,因为天气好,因为天气不好,因为天气刚刚好,每一天，都很美好。","凌晨四点钟，我看见海棠花未眠。总觉得这时，你应该在我身边。",\
    "一个人至少拥有一个梦想，有一个理由去坚强。心若没有栖息的地方，到哪里都是在流浪。","无论靠近还是远离，最后的结果都是难过。","被大雨淋湿时就想想晒干衣服的阳光和彩虹歉意的微笑"]

name = 'Grey Li'
movies = [
    {'title': '让人迷茫的原因只有一个，那就是本该拼搏的年纪，想的太多，却做的太少！': '1988'},
    {'title': '因为天气好', 'year': '1989'},
    {'title': 'A Perfect World', 'year': '1993'},
    {'title': 'Leon', 'year': '1994'},
    {'title': 'Mahjong', 'year': '1996'},
    {'title': 'Swallowtail Butterfly', 'year': '1996'},
    {'title': 'King of Comedy', 'year': '1999'},
    {'title': 'Devils on the Doorstep', 'year': '1999'},
    {'title': 'WALL-E', 'year': '2008'},
    {'title': 'The Pork of Music', 'year': '2012'},
]

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    
    return Response(choice(list), mimetype="text/json")

@app.route('/hello')
def hello():
    return render_template('index.html', name=name, movies=movies)
    

if __name__ == "__main__":
    app.run(debug = True)