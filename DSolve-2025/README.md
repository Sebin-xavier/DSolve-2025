# DSolve-2025

DSolve-2025 is a Flask-based web application that provides a simple API for user authentication and a login interface.

## Project Structure

```
DSolve-2025
├── backend
│   ├── app.py               # Main application file for the Flask backend
│   ├── templates
│   │   └── login.html       # HTML structure for the login page
│   └── static
│       └── styles.css       # CSS styles for the application
└── README.md                # Documentation for the project
```

## Setup Instructions

1. **Clone the repository:**
   ```
   git clone <repository-url>
   cd DSolve-2025
   ```

2. **Create a virtual environment:**
   ```
   python -m venv venv
   ```

3. **Activate the virtual environment:**
   - On Windows:
     ```
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```
     source venv/bin/activate
     ```

4. **Install the required packages:**
   ```
   pip install Flask Flask-CORS
   ```

## Usage

1. **Run the application:**
   ```
   python backend/app.py
   ```

2. **Access the application:**
   Open your web browser and navigate to `http://127.0.0.1:5001/` to access the home page.

3. **Login:**
   Navigate to the login page at `http://127.0.0.1:5001/login` and enter the credentials:
   - Username: `admin`
   - Password: `password`

## License

This project is licensed under the MIT License.