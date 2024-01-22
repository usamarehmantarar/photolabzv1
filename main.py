from flask import Flask, render_template, request, send_file
from PIL import Image, ImageEnhance, ImageFilter
import requests
from io import BytesIO
from rembg import remove
import os
import io

app = Flask(__name__)

def transparent(image):
    image = Image.open(image)
    response=remove(image)
    return response

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/apply_filter', methods=['POST'])
def apply_filter():
    try:
        key=request.form['key']
        if key=='alphabravocharlie1998':
            # Get uploaded image and filter
            uploaded_image = request.files['image']
            img_url = request.form.get('img_url')
            response = requests.get(img_url)
            response.raise_for_status()
            image_data = BytesIO(response.content)
            filter_image = Image.open(image_data)
            # filter_image = Image.open(img_url)
            uploaded_image= transparent(uploaded_image)
            # Resize filter image to match the size of the uploaded image
            filter_image = filter_image.resize(uploaded_image.size)
            # Convert images to RGBA mode
            uploaded_image = uploaded_image.convert('RGBA')
            filter_image = filter_image.convert('RGBA')
            # Apply the filter to the uploaded image
            result_image = Image.alpha_composite(filter_image,uploaded_image)
           # Prepare the image data to be returned as a response
            img_io = BytesIO()
            result_image.save(img_io, format='PNG')
            img_io.seek(0)

            # Send the image data as a response
            return send_file(img_io, mimetype='image/png', as_attachment=True, download_name='output.png')
        else:
            return 'Error occured: key not matched'
    except Exception as e:
        return f'Error occurred: {str(e)}'
@app.route('/image_bg', methods=['POST'])
def image_bg():
    try:
        key = request.form['key']
        if key == 'alphabravocharlie1998':
            # Get uploaded image and background image index
            uploaded_image = request.files['image']
            uploaded_image = transparent(uploaded_image)
            bg_img_index = request.form['img_bg_index']

            # Load the background image from the Backgrounds folder using the index
            backgrounds_folder = 'Backgrounds'
            bg_image_name = f'{bg_img_index}.png'  # Assuming the images are named as 'image_1.png', 'image_2.png', etc.
            bg_img_path = os.path.join(backgrounds_folder, bg_image_name)
            filter_image = Image.open(bg_img_path)

            # Convert images to RGBA mode
            uploaded_image = uploaded_image.convert('RGBA')
            filter_image = filter_image.convert('RGBA')         

            # Resize filter image to match the size of the uploaded image
            filter_image = filter_image.resize(uploaded_image.size)

            # Apply the filter to the uploaded image
            result_image = Image.alpha_composite(filter_image, uploaded_image)

            # Prepare the image data to be returned as a response
            img_io = BytesIO()
            result_image.save(img_io, format='PNG')
            img_io.seek(0)

            # Send the image data as a response
            return send_file(img_io, mimetype='image/png', as_attachment=True, download_name='output.png')
        else:
            return 'Error occurred: key not matched'
    except Exception as e:
        return f'Error occurred: {str(e)}'

@app.route('/enhance', methods=['POST'])
def enhance():
    if request.method == 'POST':
        try:
            key = request.form['key']
            if key != 'alphabravocharlie1998':
                return 'Key not matched, 403'
            # Get the uploaded image file from the request
            image_file = request.files['image']
            if image_file:
                # Load the image using Pillow
                img = Image.open(image_file)
                new_width = img.width * 2
                new_height = img.height * 2
                resized_img = img.resize((new_width, new_height), Image.BICUBIC)
                # Enhance the image quality
                enhancer = ImageEnhance.Sharpness(resized_img)
                sharpened_img = enhancer.enhance(2.0)  # Increase sharpness (adjust the factor as needed)
                enhancer = ImageEnhance.Contrast(sharpened_img)
                enhanced_img = enhancer.enhance(1.2)  # Increase contrast (adjust the factor as needed)
                # Create an in-memory file to store the enhanced image
                buffered = io.BytesIO()
                # Save the enhanced image as PNG to the in-memory file
                enhanced_img.save(buffered, format='PNG')
                buffered.seek(0)
                # Return the processed image as a response object
                return send_file(buffered, mimetype='image/png')
            return "Error: No image file provided"
        except KeyError:
            return 'Invalid request data', 400
        except Exception as e:
            return f'Error occurred: {str(e)}', 500

if __name__ == '__main__':
    app.run(debug=True)
