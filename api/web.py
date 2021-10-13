from flask import Flask, Response, request
import json
from flask import jsonify
app = Flask(__name__)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
#     print(request.args)
#     key = request.args.get('key')
    mes={"code":200,"msg":"success","newslist":[{"content":"我不允许你们说自己胖 你们那不叫胖 那叫可爱到膨胀。"}]}
#     data = json.dumps(mes)
    return Response(jsonify(mes), mimetype="text/json")
    
if __name__ == "__main__":
    app.run(debug = True)
