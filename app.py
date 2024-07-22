from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/streamlit')
def streamlit_app():
    return redirect('http://192.168.29.175:8501')  # Use the correct local IP address

@app.route('/streamlit1')
def streamlit1_app():
    return redirect('http://192.168.29.175:8502')  # Use the correct local IP address

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
