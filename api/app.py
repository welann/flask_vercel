from flask import Flask, Response, request,render_template

from random import choice

app = Flask(__name__)


list=["让人迷茫的原因只有一个，那就是本该拼搏的年纪，想的太多，却做的太少！","你知道吗，你红尘梦醒的那一刻，是我看过的，最美丽的画面。",\
    "跟你在一起的时光都很耀眼,因为天气好,因为天气不好,因为天气刚刚好,每一天，都很美好。","凌晨四点钟，我看见海棠花未眠。总觉得这时，你应该在我身边。",\
    "一个人至少拥有一个梦想，有一个理由去坚强。心若没有栖息的地方，到哪里都是在流浪。","无论靠近还是远离，最后的结果都是难过。","被大雨淋湿时就想想晒干衣服的阳光和彩虹歉意的微笑"]

secon=[
    '让人迷茫的原因只有一个，那就是本该拼搏的年纪，想的太多，却做的太少！',
    '当我决议跟你度过下半辈子时，我盼望我的下半生赶紧开始。',
    '在最美的年华，做最喜欢的事情，别辜负了美好时光。',
    '此生，愿做低眉的女子，揽一蓑烟雨，怀一份诗意，在云水之湄，如莲娉婷。',
    '我们可以沉迷于享受，只是给予的快乐。',
    '内心如此快乐，以至于无法忍受蜂蜜的喜悦。',
    '喜欢喝酒，嘴角也在微笑！',
    '别轻易说爱，诺言就是欠债！',
    '知识是一种幸福，好奇心是知识的发芽。',
    '只有努力减少他人的痛苦，您才会感到快乐。',
    '我喜出望外，我的脚似乎踩在幸福的云上。',
    '他开心地笑了，露出一排洁白的牙齿。',
    '欢乐涌入她的心​​，心在泉水中摇摆。',
    '我的心是甜蜜而悲伤的，我感到从未有过的快乐。',
    '行动不一定带来幸福，但是如果您不行动，一定会带来不幸福。',
]




@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    
    return Response(choice(list), mimetype="text/json")

@app.route('/start')
def index():    
    pic=["https://z3.ax1x.com/2021/10/18/5NSWAs.jpg",
        "https://z3.ax1x.com/2021/10/18/5NSHuF.jpg",
        "https://z3.ax1x.com/2021/10/18/5NSOE9.jpg",
        "https://z3.ax1x.com/2021/10/18/5NSbB4.jpg",
        "https://z3.ax1x.com/2021/10/18/5NSqHJ.jpg"
    
    ]
    return render_template('index.html', words=choice(secon),pic=choice(pic))
    

if __name__ == "__main__":
    app.run(debug = True)


