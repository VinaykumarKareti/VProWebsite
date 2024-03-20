# from flask import Flask, render_template, request, redirect, url_for
# from pytube import YouTube

# app = Flask(__name__)

# @app.route('/',methods=["GET"])
# def index():
#     return render_template('index.html')

# @app.route('/download', methods=['POST'])
# def download():
#     video_url = request.form['video_url']
#     resolution = request.form['resolution']

#     try:
#         yt = YouTube(video_url)
#         stream = yt.streams.filter(res=resolution).first()
#         stream.download()
#         return redirect(url_for('index'))
#     except Exception as e:
#         return render_template('error.html', error=str(e))

from flask import Flask, render_template, request, redirect, url_for, send_file
from pytube import YouTube
import os

app = Flask(__name__)

@app.route('/', methods=["GET"])
def index():
    return render_template('index.html')

@app.route('/download', methods=['POST'])
def download():
    video_url = request.form['video_url']
    resolution = request.form['resolution']

    try:
        yt = YouTube(video_url)
        stream = yt.streams.filter(res=resolution).first()
        video_filename = f"{yt.title}.{stream.subtype}"
        stream.download(filename=video_filename)
        
        # Construct the path to the downloaded video file
        video_path = os.path.join(os.getcwd(), video_filename)

        # Send the file as an attachment
        return send_file(video_path, as_attachment=True)

    except Exception as e:
        return render_template('error.html', error=str(e))

if __name__ == "__main__":
    app.run(debug=True)
