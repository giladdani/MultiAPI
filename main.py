from consts import PORT
from flask import Flask, redirect, render_template, request, abort

app = Flask(__name__)

import movies

if __name__ == '__main__':
    app.run(port=PORT, debug=True)

