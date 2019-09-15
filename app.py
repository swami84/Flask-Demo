from flask import Flask, render_template, request, redirect
import pandas as pd

from bokeh.io import output_notebook
from bokeh.layouts import gridplot
from bokeh.plotting import figure, show,output_file,save
import quandl
from bokeh.resources import CDN
from bokeh.embed import file_html


app = Flask(__name__)
app.vars = {}


@app.route('/',methods = ['POST', 'GET'])
def index():
  if request.method == 'GET':
    return redirect ('/homepage')
    
  else:
    return redirect ('/homepage')
  

@app.route('/homepage', methods = ['POST', 'GET'])
def homepage():
  
  if request.method == 'GET':
    return render_template('homepage.html')
    
  else:
    app.vars['ticker'] = request.form['ticker']
    return redirect ('/display')
    
#@app.route('/display', methods = ['GET'])
##def generateoutput(ticker):
##    ALPHA_VANTAGE_API_KEY = 'IU2OUWVANSPF10UV'
##    ts = TimeSeries(key=ALPHA_VANTAGE_API_KEY, output_format='pandas')
##    df, data_info = ts.get_monthly(ticker)
##    data = df.copy()
##    data = data.reset_index()
##    data['Avg Price'] = (data['2. high'] + data ['3. low'])/2
##
##  
##    p1 = figure(x_axis_type="datetime", title=ticker +  " Stock Price")
##    p1.grid.grid_line_alpha=0.6
##    p1.xaxis.axis_label = 'Date'
##    p1.yaxis.axis_label = 'Price'
##    p1.line((datetime(data['date'])), data['Avg Price'], color='#1729CB',line_width = 4, legend='Avg Price')
##    p1.circle((datetime(data['date'])), data['1. open'], size=6, legend='Opening Price',color='green', alpha=0.5)
##    p1.circle((datetime(data['date'])), data['4. close'], size=6, legend='Closing Price',color='red', alpha=0.5)
##    p1.legend.location = "top_left"
##    
##
##    output_file("\templates\stocks.html", title="Stock Chart")
##    #return render_template('display.html')
##    return redirect('/display')
@app.route('/display', methods = ['GET', 'POST'])
def  display():
    tick = "WIKI/"+app.vars['ticker']
    data = quandl.get(tick, start_date="2016-01-01", end_date="2018-01-01", api_key='zmP39qUBxQLhWwMVN9Ra')

    data = data.reset_index()
    data['Avg Price'] = (data['High'] + data ['Low'])/2

    p1 = figure(x_axis_type="datetime", title= tick + " Stock Price")
    p1.grid.grid_line_alpha=0.6
    p1.xaxis.axis_label = 'Date'
    p1.yaxis.axis_label = 'Price'

    p1.line(data['Date'], data['Avg Price'], color='#1729CB',line_width = 4, legend='Avg Price')
    p1.circle(data['Date'], data['Open'], size=6, legend='Opening Price',color='green', alpha=0.5)
    p1.circle(data['Date'], data['Close'], size=6, legend='Closing Price',color='red', alpha=0.5)
    p1.legend.location = "top_left"

    output_file("templates/display.html", title="Stock Chart")
    #from shutil import copyfile
    #copyfile("stock.html", "templates/stock.html")
    #show(p1)
    #save(p1, filename = "\templates\stocks1.html")
    
    
    
    return render_template('display.html')
##    
if __name__ == '__main__':
  app.run(debug=True)
# THis is a comment

