from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/streamlit')
def streamlit_app():
    return redirect('https://documents-compare.onrender.com/')

@app.route('/streamlit1')
def streamlit1_app():
    return redirect('https://extraction-l54k.onrender.com/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
