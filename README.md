# JobMate AI Backend
This project contains the backend application for JobMate AI, built with Python.

## Getting Started
Follow these instructions to set up and run the project on your local machine.
## Prerequisites
Make sure you have Python (version 3.8 or higher recommended) and pip (Python Package Installer) installed.
You can verify your installation by running:
'''bash 
python --version
pip --version
'''
### Installation

1. **Clone the repository:**
''' bash
git clone <https://github.com/iwstech3/JobmateAI-Backend.git>
cd "JobMateAI-Backend"
'''

3. **Create a virtual environment (recommended):**

'''bash   
python -m venv Jobmate_env
'''

### Activate the virtual environment:

On Windows:
'''bash
Jobmate_env\Scripts\activate
'''

### Configuration
1. Create a .env file in the Backend directory and add your environment variables:
env# Example environment variables
DATABASE_URL=your_database_url
SECRET_KEY=your_secret_key
API_KEY=your_api_key
2. add the following to your requirements.txt file:
 
### Install dependencies:

'''bash   
pip install -r requirements.txt
'''

### Running the Development Server
To start the development server:
'''bash
python app.py
'''
Or if using FastAPI:
'''bash
uvicorn main:app --reload
```

The backend will typically run on `http://localhost:8000`.

### Available Commands

- `python app.py` - Starts the development server
- `pip install -r requirements.txt` - Installs all dependencies
- `pip freeze > requirements.txt` - Updates the requirements file


Note: Make sure to update the command for running the server based on your actual framework (Flask, FastAPI, Django, etc.) and adjust the port numbers accordingly.

