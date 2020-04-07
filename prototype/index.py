from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/search')
def serch():
    return render_template("search.html")

#PORTがデフォルトだと5000のままなので5500に書き直す
#(・・・外部から読み込んでいるため？)
if __name__ == '__main__':
    app.run(port=5500)