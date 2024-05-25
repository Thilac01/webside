from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/gallery_Mus')
def gallery_Mus():
    image_files = os.listdir('static/MUSIC')
    video_files = os.listdir('static/videos')
    return render_template('music.html', image_files=image_files, video_files=video_files)

@app.route('/gallery_Dan')
def gallery_Dan():
    image_files = os.listdir('static/DANCE')
    video_files = os.listdir('static/videos')
    return render_template('dance.html', image_files=image_files, video_files=video_files)

@app.route('/gallery_Dra')
def gallery_Dra():
    image_files = os.listdir('static/DRAMA')
    video_files = os.listdir('static/videos')
    return render_template('drama.html', image_files=image_files, video_files=video_files)





if __name__ == '__main__':
    app.run(debug=True)
