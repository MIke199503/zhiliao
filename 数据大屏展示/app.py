#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2020/8/26 14:48
# @Author : way
# @Site :
# @Describe:

from flask import Flask, render_template
from data import *

flag = 0 
app = Flask(__name__)

def test():
    global flag 
    flag += 1 
    import test
    return test.adda(flag)




@app.route('/')
def index():
    a = test()
    print(a)
    data = SourceData()
    return render_template('index.html', form=data, title=data.title)


@app.route('/corp')
def corp():
    data = CorpData()
    return render_template('index.html', form=data, title=data.title)


@app.route('/job')
def job():
    data = JobData()
    return render_template('index.html', form=data, title=data.title)

@app.route('/ele')
def ele():
    data = EleData()
    return render_template('index.html',form = data ,title = data.title)

    
if __name__ == "__main__":
    app.run(host='127.0.0.1', debug=False)
