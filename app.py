from flask import Flask, render_template, request, redirect, url_for
from pytube import YouTube

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download', methods=['POST'])
def download():
    video_url = request.form['video_url']
    resolution = request.form['resolution']

    yt = YouTube(video_url)
    stream = yt.streams.filter(res=resolution).first()
    stream.download()

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
