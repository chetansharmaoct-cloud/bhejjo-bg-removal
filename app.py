from flask import Flask, request, send_file
from flask_cors import CORS
from rembg import remove
from PIL import Image
import io
import os

app = Flask(__name__)
CORS(app)  # Enable CORS for Flutter app

@app.route('/')
def home():
    return '''
    <h1>Background Removal API</h1>
    <p>POST to /remove-background with an image file</p>
    <p>Status: Running ✓</p>
    '''

@app.route('/remove-background', methods=['POST'])
def remove_background():
    try:
        # Check if image file is present
        if 'image_file' not in request.files:
            return {'error': 'No image file provided'}, 400
        
        file = request.files['image_file']
        
        if file.filename == '':
            return {'error': 'No file selected'}, 400
        
        # Read image
        input_image = Image.open(file.stream)
        
        # Remove background
        output_image = remove(input_image)
        
        # Convert to bytes
        img_io = io.BytesIO()
        output_image.save(img_io, 'PNG')
        img_io.seek(0)
        
        return send_file(
            img_io,
            mimetype='image/png',
            as_attachment=True,
            download_name='removed_bg.png'
        )
    
    except Exception as e:
        return {'error': str(e)}, 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
