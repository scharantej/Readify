
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/<book_summary_name>')
def book_summary(book_summary_name):
    return render_template(f'{book_summary_name}.html')

if __name__ == '__main__':
    app.run(debug=True)
