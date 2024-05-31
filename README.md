# Urine Strip Color Analyzer

This project is a web application that allows users to upload an image of a urine strip and identifies the colors on the strip. The application analyzes the image and returns the results as a JSON object with 10 colors (RGB values).

## Features

- Upload an image of a urine strip through a web interface.
- Analyze the image and identify the 10 colors on the strip.
- Return the results as a JSON object with 10 colors (RGB values).

## Technologies Used

- Backend: Django, Django REST Framework
- Frontend: Vanilla JavaScript + HTML
- Image Analysis: OpenCV + K-Means Clustering
- Database: SQLite

## API

The application provides an API endpoint for uploading the urine strip image. The image should be sent as a multipart/form-data POST request to the `/analyze` endpoint.

## How to run

1. Set up virtual environment: `python -m venv venv \source venv/bin/activate`
2. Install the requirements: `pip install -r requirements.txt`
3. Apply migrations: `python manage.py migrate`
4. Run the server: `python manage.py runserver`

## Key Components

1. **Image Upload and Storage**:
   - Users upload images via a form in `index.html`.
   - Uploaded images are saved in the `media/` directory.
  
2. **Image Analysis**:

   - The `analyze_image_colors` function in `utils.py` processes the image, extracting RGB values for each test area on the strip.
   - The analysis results are returned as a dictionary with labels like 'URO', 'BIL', etc.

3. **API Endpoint**:

   - `AnalyzeImageView` in `views.py` handles POST requests to `/analyze/`, saves the uploaded image, and returns the color analysis results.

4. **Frontend**:
   - `index.html` provides a simple interface for uploading images.
   - JavaScript handles form submission and displays the results on the page

## License

[MIT](https://choosealicense.com/licenses/mit/)
