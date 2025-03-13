# File Sharing App

A simple file sharing web application built with **Flask**. This app allows users to upload files, set expiration conditions (based on date or number of downloads), and retrieve download links. The app ensures that files are automatically removed or links are invalidated based on user-defined expiration rules.

---

## Features
- Upload files and generate unique download links.
- Expire files based on:
  - A number of downloads.
  - A specific expiration date.
- Prevent access to expired or invalid download links.
- Error handling for missing or corrupted files.
- Clean and responsive UI for uploading files and feedback.

---

## Technologies Used
- **Backend**:
  - [Flask](https://flask.palletsprojects.com/) — A lightweight WSGI web application framework.
  - [SQLAlchemy](https://www.sqlalchemy.org/) — For database integration and link/file management.
- **Frontend**:
  - HTML5, CSS3 — For the user interface.
- **Database**:
  - SQLite (default) or any SQLAlchemy-supported database.
- **Other Libraries**:
  - `datetime` — For expiration date handling.
  - `os` — For file system operations.

---

## Installation

### Prerequisites
Ensure you have the following installed:
- Python 3.8 or higher
- pip (Python package manager)
- Virtual environment support (optional but recommended)

### Steps
1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-username/file-sharing-app.git
   cd file-sharing-app
   ```

2. **Create and Activate Virtual Environment**
   ```bash
   python -m venv venv
   source venv/bin/activate    # On Linux/macOS
   venv\Scripts\activate       # On Windows
   ```

3. **Install Dependencies**
   Install the required Python dependencies using `pip`:
   ```bash
   pip install -r requirements.txt
   ```

4. **Setup the Database**
   Initialize the SQLite database (or your database of choice) by running:
   ```bash
   flask db init
   flask db migrate
   flask db upgrade
   ```
   This will create the necessary tables for the app.

5. **Start the Application**
   Run the Flask development server:
   ```bash
   flask run
   ```
   The application will be available at `http://127.0.0.1:5000`.

---

## Usage

### 1. **Upload a File**
- Open the app in your browser.
- Use the file upload form to select a file.
- Optionally, set:
  - An expiration date (Expire after a certain number of days).
  - A download limit (Expire after a specific number of downloads).
- Click the **Upload File** button.

### 2. **Get Download Link**
- After submitting the file, a success message will display:
  - A download URL.
  - Expiration details (if any).
- Share this URL with others for downloading the file.

### 3. **File Expiration Behavior**
- If the link is accessed after its expiration date or download limit, it will show an error message saying "Link expired" or "Download limit reached."

---

## Project Structure

file-sharing-app/
│
├── app.py               # Main Flask application file with routes and app configuration
├── models.py            # Database models for File and DownloadLink management
├── templates/           # Folder for HTML templates (UI)
│   └── index.html       # Single-page template for file uploads and messages
├── static/              # Static assets like CSS, JavaScript, or images
│   └── style.css        # Custom styles for the application (optional)
├── migrations/          # Database migration files (managed by Flask-Migrate)
├── uploads/             # Uploaded files directory (automatically created by the app)
├── requirements.txt     # List of Python dependencies to install with pip
├── README.md            # Project documentation
└── LICENSE              # License information for the project
---

## Contributing
Contributions are welcome! If you’d like to contribute, please follow these steps:
1. Fork the repository.
2. Create a new feature branch:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes and push to your forked repository.
4. Submit a pull request with a detailed description of your changes.

---

## License
This project is licensed under the **MIT License**. See the `LICENSE` file for more details.

---

## Acknowledgements
- [Flask Documentation](https://flask.palletsprojects.com/)
- [SQLAlchemy Documentation](https://docs.sqlalchemy.org/)
- Open-source inspiration from the developer community.
