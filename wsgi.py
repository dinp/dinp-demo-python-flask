# -*- coding: utf-8 -*-
import sys
sys.path.insert(0, "./dinp/")

import time
from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    sys.stdout.write('----------------stdout at: %s\n' % time.strftime('%Y-%m-%d %H:%M:%S'))
    sys.stderr.write('----------------stderr at: %s\n' % time.strftime('%Y-%m-%d %H:%M:%S'))
    return "hello, dinp"

# export for paas
application = app

if __name__ == '__main__':
    application.run()
