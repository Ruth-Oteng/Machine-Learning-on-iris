from flask import Flask
import sqlite3
import numpy as np
import pandas as pd
#from sklearn.linear_model import LinearRegression

app = Flask(__name__) 

#@app.route('/') 
#def landingpage(): 
   
 # return render_template('base.html')

if __name__ == '__main__': 
  app.run()