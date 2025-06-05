# Setup Instructions for AI Chatbot

## Prerequisites
- Python 3.8+
- `pip` package manager
- Internet connection for API access

---

## Backend Setup

1. **Clone or download the project repository**

2. **Navigate to the backend folder (if applicable)**
   ```bash
   cd backend
Install required Python packages

bash
Copy
Edit
pip install fastapi uvicorn requests
Set your OpenRouter API key

Open app.py

Replace the placeholder OPENROUTER_API_KEY with your actual API key:

python
Copy
Edit
OPENROUTER_API_KEY = "your_actual_api_key_here"
Run the FastAPI backend server

bash
Copy
Edit
uvicorn app:app --reload
The backend server will be running at: http://127.0.0.1:8000

Frontend Setup
Navigate to the frontend folder

bash
Copy
Edit
cd ../frontend
Serve the frontend files using a simple HTTP server

Using Python’s built-in HTTP server:

bash
Copy
Edit
python -m http.server 3000
This serves the frontend at http://localhost:3000

Open your browser

Go to http://localhost:3000

You should see the AI Chatbot interface

