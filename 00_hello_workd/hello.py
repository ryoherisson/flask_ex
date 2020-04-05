# from flask import Flask

# app = Flask(__name__)

# @app.route('/')
# def hello_world():
#     return "Hellow World!"

# if __name__ == "__main__":
#     # docker run時に、-p 外部からアクセスされるポート番号:コンテナ側のポート番号を指定
#     # 今回の場合は、8008:5000
#     # localからlocalhost:8008でアクセス
#     app.run(host='0.0.0.0', port=5000, debug=True)