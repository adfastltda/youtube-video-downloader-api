from flask import Flask, request, jsonify
from utils import is_valid_youtube_url
from youtube_service import YouTubeService

app = Flask(__name__)
youtube_service = YouTubeService()  # Configurar o diretório de download aqui se necessario

@app.route('/download/<resolution>', methods=['POST'])
def download_by_resolution(resolution):
    data = request.get_json()
    url = data.get('url')
    
    if not url:
        return jsonify({"error": "Missing 'url' parameter in the request body.", "error_code": "MissingParameter"}), 400

    if not is_valid_youtube_url(url):
        return jsonify({"error": "Invalid YouTube URL.", "error_code": "InvalidURL"}), 400

    success, error_code, message = youtube_service.download_video(url, resolution)
    
    if success:
        return jsonify({"message": f"Video downloaded successfully.", "file_path": message}), 200
    else:
        return jsonify({"error": message, "error_code": error_code}), 500

@app.route('/video_info', methods=['POST'])
def video_info():
    data = request.get_json()
    url = data.get('url')
    
    if not url:
        return jsonify({"error": "Missing 'url' parameter in the request body.", "error_code": "MissingParameter"}), 400

    if not is_valid_youtube_url(url):
        return jsonify({"error": "Invalid YouTube URL.", "error_code": "InvalidURL"}), 400
    
    video_info, error_message = youtube_service.get_video_info(url)
    
    if video_info:
        return jsonify(video_info), 200
    else:
        return jsonify({"error": error_message, "error_code": "VideoInfoError"}), 500

if __name__ == '__main__':
    app.run(debug=True)