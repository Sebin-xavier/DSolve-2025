from app import create_app

app = create_app()
@app.route('/')
def home():
    return "Welcome to DSolve-2025!"
if __name__ == '__main__':
    app.run(debug=True)
