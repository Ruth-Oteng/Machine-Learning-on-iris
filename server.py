from flask import *
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
app=Flask(__name__)


@app.route('/') 
def home(): 
   
 return render_template('newindex.html')

@app.route('/ml') 
def run():
  url='https://raw.githubusercontent.com/sarwansingh/Python/master/ClassExamples/data/student-pass-fail-data.csv'
  df=pd.read_csv(url)
  df1=df.values
  
  X=df1[:,0:2]
  Y= df1[:,2]
  model=LinearRegression()
  model.fit(X,Y)
  var=model.predict([[7,27]])
  
  return "The prdeicted result is " + str(var[0]* 100) + "%"


#app.route('/r')
#def index():
  
  #return render_template('index.html')

if __name__=='__main__':
  app.run()