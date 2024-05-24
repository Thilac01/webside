from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/gallery')
def gallery():
    image_files = os.listdir('static/images')
    video_files = os.listdir('static/videos')
    return render_template('gallery.html', image_files=image_files, video_files=video_files)

if __name__ == '__main__':
    app.run(debug=True)
