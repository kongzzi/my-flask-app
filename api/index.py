from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>🚀 Hello, CI/CD!</h1>
    <p>Flask + Vercel 배포 실습</p>
    <a href="/about">About 페이지</a>
    """

@app.route("/about")
def about():
    return """
    <h1>About</h1>
    <p>이 앱은 CI/CD 파이프라인 실습용 Flask 앱입니다.</p>
    <a href="/">홈으로</a>
    """