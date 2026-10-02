# Stats Dashboard

A small full-stack web app that calculates descriptive statistics from numbers you enter. The Python (Flask) backend does the calculations, and an HTML/JavaScript frontend sends the data and displays the results.

I built this to learn how a frontend and backend communicate, and to practice the statistics fundamentals behind data analysis.

## Features

- Enter a list of numbers in the browser
- Get the **mean, median, mode, variance, and standard deviation**
- Calculations run on a Flask backend, separate from the frontend

## Tech Stack

- **Backend:** Python, Flask
- **Frontend:** HTML, JavaScript
- **Tools:** VS Code, Git, GitHub

## Screenshot

![Stats Dashboard screenshot](screenshot.png)

## Project Structure

```
stats-dashboard/
├── app.py              # Flask backend and statistics logic
├── requirements.txt    # Python dependencies
└── templates/
    └── index.html      # Frontend page
```

## How to Run

1. **Clone the repository**
   ```bash
   git clone https://github.com/ayank4520-wq/stats-dashboard.git
   cd stats-dashboard
   ```

2. **(Optional) Create a virtual environment**
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Start the app**
   ```bash
   python app.py
   ```

5. Open your browser and go to `http://127.0.0.1:5000`

## What I Learned

- Separating frontend and backend, and passing data between them
- Structuring a Flask project (routes, templates, dependencies)
- Implementing core descriptive statistics in Python
- Using Git and GitHub to version and publish a project

## Possible Improvements

- Add charts (histogram, box plot) to visualize the data
- Accept CSV file uploads
- Add input validation and clearer error messages

## Author

**Ayan Khan**
Data Science student, Jaipur, India
GitHub: [ayank4520-wq](https://github.com/ayank4520-wq)
