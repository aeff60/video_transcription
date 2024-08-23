from flask import Flask, request, render_template, redirect, url_for
import openai
import moviepy.editor as mp
import os

app = Flask(__name__)
openai.api_key = 'APIKEY' # ใส่ API Key ของ OpenAI ที่ได้จากเว็บไซต์

UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# สร้างโฟลเดอร์สำหรับเก็บไฟล์ที่อัปโหลด
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# ฟังก์ชันแยกเสียงออกจากวิดีโอ
def extract_audio_from_video(video_file_path, output_audio_path):
    video = mp.VideoFileClip(video_file_path)
    video.audio.write_audiofile(output_audio_path)

# ฟังก์ชันถอดเสียงเป็นข้อความโดยใช้ OpenAI API พร้อม timestamp
def transcribe_audio_with_timestamp(audio_file_path):
    with open(audio_file_path, "rb") as audio_file:
        response = openai.Audio.transcribe("whisper-1", audio_file, response_format="verbose_json")
        return response

# หน้าเว็บหลักสำหรับอัปโหลดวิดีโอ
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # รับไฟล์จากการอัปโหลด
        video_file = request.files['video']
        if video_file:
            video_file_path = os.path.join(app.config['UPLOAD_FOLDER'], video_file.filename)
            video_file.save(video_file_path)

            # แยกเสียงออกจากวิดีโอ
            audio_file_path = video_file_path.replace('.mp4', '.mp3')
            extract_audio_from_video(video_file_path, audio_file_path)

            # ถอดเสียงเป็นข้อความพร้อม timestamp
            transcription_response = transcribe_audio_with_timestamp(audio_file_path)

            # สร้างผลลัพธ์เป็นข้อความพร้อม timestamp
            transcription_result = []
            for segment in transcription_response['segments']:
                start_time = segment['start']
                end_time = segment['end']
                text = segment['text']
                transcription_result.append(f"{start_time:.2f}s - {end_time:.2f}s: {text}")

            return render_template('result.html', transcription_result=transcription_result)

    return render_template('index.html')

# หน้าเว็บสำหรับแสดงผลลัพธ์
@app.route('/result')
def result():
    return render_template('result.html')

if __name__ == '__main__':
    app.run(debug=True)
