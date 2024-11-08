from flask import Flask, render_template, redirect

app = Flask(__name__)

@app.route('/')
def index():
  return redirect("https://sntz55website.onrender.com/home")

@app.route('/home')
def home():
  return render_template('home.html')

@app.route('/about')
def about():
  return render_template('about.html')

if __name__ == '__main__':
  app.run()
