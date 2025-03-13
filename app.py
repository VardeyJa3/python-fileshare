from flask import Flask, render_template, request, send_file
from werkzeug.utils import secure_filename
from models import db, File, DownloadLink
from config import Config
from utils import delete_file, calculate_expiration_date
import os
from datetime import datetime

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

# Ensure upload folder exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)


@app.route('/')
def index():
    # Renders the file upload page (index.html).
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload_file():
    """
    Handles file upload, generates a shareable link, and sets expiration.
    Shows success or error messages on the index page.
    """
    try:
        # Check if a file is included in the request
        if 'file' not in request.files:
            return render_template('index.html', error='No file part in the request.')

        file = request.files['file']
        if file.filename == '':
            return render_template('index.html', error='No file selected for upload.')

        # Process and save the uploaded file
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)

        # Save the file metadata into the database
        new_file = File(filename=filename, path=file_path)
        db.session.add(new_file)
        db.session.commit()

        # Process expiration settings from the form
        expiration_date = None
        max_downloads = None

        if 'expire_by_date' in request.form and request.form['days']:
            try:
                days = int(request.form['days'])
                expiration_date = calculate_expiration_date(days)
            except ValueError:
                return render_template(
                    'index.html', error='Invalid value for expiration days.')

        if 'expire_by_downloads' in request.form and request.form['downloads']:
            try:
                max_downloads = int(request.form['downloads'])
            except ValueError:
                return render_template(
                    'index.html', error='Invalid value for max downloads.')

        # Create a shareable link with expiration logic
        new_link = DownloadLink(
            file_id=new_file.id,
            expiration_date=expiration_date,
            max_downloads=max_downloads
        )
        db.session.add(new_link)
        db.session.commit()

        # Generate the download URL
        download_url = f"{request.host_url}download/{new_link.id}"

        # Return the updated index page with success message and download URL
        return render_template(
            'index.html',
            success='File successfully uploaded!',
            download_url=download_url,
            expiration_date=new_link.expiration_date,
            max_downloads=new_link.max_downloads
        )

    except Exception as e:
        # Catch and handle any unexpected errors
        return render_template('index.html', error=f'An error occurred: {str(e)}')

@app.route('/download/<link_id>', methods=['GET'])
def download_page(link_id):
    link = DownloadLink.query.get(link_id)

    if not link:
        return render_template('index.html', error="Invalid or expired link!")

    if link.expiration_date and datetime.utcnow() > link.expiration_date:
        db.session.delete(link)
        db.session.commit()
        return render_template('index.html', error="This link has expired!")

    if link.max_downloads is not None and link.current_downloads >= link.max_downloads:
        db.session.delete(link)
        db.session.commit()
        return render_template('index.html', error="Download limit reached!")

    file = File.query.get(link.file_id)
    if not file or not os.path.exists(file.path):
        return render_template('index.html', error="File not found on the server.")

    link.current_downloads += 1
    db.session.commit()

    return send_file(file.path, as_attachment=True, download_name=file.filename)


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
