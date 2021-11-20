from flask import Flask, render_template

from rbf import getTempData
app = Flask(__name__)


@app.route("/")
def home():
    dataList = getTempData()

    print(dataList)

    return render_template('index.html', data=dataList)
