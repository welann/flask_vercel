from flask import Flask, Response, request

app = Flask(__name__)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    print(request.args)
    key = request.args.get('key')
    data=json.dumps({"code":200,"msg":"success","newslist":[{"content":"我不允许你们说自己胖 你们那不叫胖 那叫可爱到膨胀。"}]})
    return Response(data, mimetype="text/json")
    
if __name__ == "__main__":
    app.run(debug = True)
