from flask import Flask, render_template
from mysqlconnection import *
from functions import *

app = Flask(__name__)


@app.route('/')
def index():
  # print(getRow('users', '989HHY'))
  # print(updateField('companies', '456DFG', 'name', 'Google'))
  # print(deleteRow('users', '4566GGF'))
  # print(getMyFavorites('favoriteStudents', '34324'))


  return render_template('index.html')


if __name__ == '__main__':
  app.run(debug=True)