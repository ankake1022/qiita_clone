from flask import Flask, render_template
app = Flask(__name__)

login_status = False

@app.route('/')
def home():
    title = "home"
    return render_template("home.html", title=title, login_status=login_status)

@app.route('/search')
def serch():
    title = "search"
    return render_template("search.html", title=title, login_status=login_status)

#PORTがデフォルトだと5000のままなので5500に書き直す
#(・・・外部から読み込んでいるため？)
if __name__ == '__main__':
    app.run(port=5500)