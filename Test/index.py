from flask import Flask, render_template
app = Flask(__name__)

user_name="田中　一郎"

#メニューを表示
@app.route("/")
def menu():
    return render_template("index.html", user_name = user_name)

#マイページ
@app.route("/mypage")
def walk():
    menu_name="マイページ"
    info="会員ランク：A"
    return render_template("screen_tran.html", menu_name=menu_name, user_name=user_name, info=info)

#購入履歴
@app.route("/history")
def attack():
    menu_name="購入履歴"
    info="2020.03.08 Windows 120,000"
    return render_template("screen_tran.html", menu_name=menu_name, user_name=user_name, info=info)

