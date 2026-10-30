#!/usr/bin/env python3.12
# pic —— 图片太大传不上去？拖进来，选个宽度和质量，直接下压缩好的
# 纯前端算，这里只发一个空壳页面
import os

from flask import Flask, render_template

app = Flask(__name__)


@app.get("/")
def index():
    return render_template("page.html")


@app.get("/healthz")
def healthz():
    return "ok"


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=int(os.environ.get("PIC_PORT", "8884")), debug=False)
