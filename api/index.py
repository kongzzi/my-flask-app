from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>🚀 Hello, CI/CD!</h1>
    <p>Flask + Vercel 배포 실습</p>
    <a href="/about">About 페이지</a>
    <h1>🎉 자동 배포 성공!</h1>
    <p>코드를 수정하고 push했더니 자동으로 배포되었습니다.</p>
    """

@app.route("/about")
def about():
    return """
    <h1>About</h1>
    <p>이 앱은 CI/CD 파이프라인 실습용 Flask 앱입니다.</p>
    <a href="/">홈으로</a>
    """