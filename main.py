from flask import Flask, render_template
import datetime

app = Flask(__name__)

@app.route('/')
def home():
  return render_template('index.html')

@app.route('/about')
def about():
  return render_template('about.html')

@app.route('/time')
def time():
  return f"The time is: {datetime.datetime.utcnow}"

if __name__ == '__main__':
  app.run()
