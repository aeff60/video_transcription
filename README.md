### Video Transcription Web App

This project is a web application built with Flask that allows users to upload video files, extract audio from the videos, and transcribe the audio into text with timestamps using the OpenAI API.

#### Features

- Upload video files in MP4 format.
- Extract audio from the uploaded video files.
- Transcribe the extracted audio into text with timestamps using OpenAI's Whisper API.
- Display the transcription results on a web page.

#### Project Structure

- `app.py`
- `static/`
  - `styles.css`
- `templates/`
  - `index.html`
  - `result.html`
- `uploads/`

#### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/videotranscription.git
   cd videotranscription
   ```

2. Create a virtual environment and activate it:

   ```bash
   python -m venv env
   source env/Scripts/activate  # On Windows
   source env/bin/activate      # On Unix or MacOS
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Set your OpenAI API key in `app.py`:

   ```python
   openai.api_key = 'your-openai-api-key'
   ```

#### Usage

1. Run the Flask application:

   ```bash
   python app.py
   ```

2. Open your web browser and navigate to [http://127.0.0.1:5000/](http://127.0.0.1:5000/).

3. Upload a video file in MP4 format.

4. Wait for the audio extraction and transcription process to complete.

5. View the transcription results with timestamps on the result page.

#### File Descriptions

- `app.py`: The main Flask application file that handles routes, file uploads, audio extraction, and transcription.
- `static/styles.css`: The CSS file for styling the web pages.
- `templates/index.html`: The HTML template for the upload page.
- `templates/result.html`: The HTML template for displaying the transcription results.
- `uploads/`: The directory where uploaded video files and extracted audio files are stored.

#### License

This project is licensed under the MIT License. See the LICENSE file for more details.

#### Acknowledgements

- Flask
- OpenAI
- MoviePy
"# videotranscription" 
