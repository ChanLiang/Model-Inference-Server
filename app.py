import base64
import json
import time
from gevent import monkey
from bottle import run, post, route, request

monkey.patch_all()


def get_algo_result(input):
    return "good!"

@route("/")
def hello():
    """ default """
    return "Hello World!"

@route("/v1/req", method="POST")
def title_service():
    """ 请求服务 """
    startTime = time.time()
    data = json.loads(request.body.read())
    text = base64.b64decode(data["data"])

    algorithmResult = get_algo_result(data["data"])
    res = algorithmResult.replace("\n", "")

    endTime = time.time()
    executionTime = int(1000 * (endTime - startTime))

    return generateReturnJson(res, executionTime, 200)
    
def generateReturnJson(result, executeTime, retCode, errMsg=""):
    """ 返回Json格式 """
    
    return {
        "format": "json",
        "retCode": retCode,
        "err_msg": errMsg,
        "result": result,
        "classify_ms": executeTime,
    }    


if __name__ == "__main__":        # on running python app.py
    # initiate your model here!
    run(host='0.0.0.0', port=2002, server='gevent')
