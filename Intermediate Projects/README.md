# Python Intermediate Projects Collection
# Coded by : Nathishwar
This repository contains four intermediate-level Python projects that cover various aspects of web development, data scraping, API integration, and file persistence.

## Projects Included

1. **Basic Blog using Flask**
2. **Simple Web Scraper**
3. **Weather App using API**
4. **Todo Application with File Persistence**
5. **File Organizer**
6. **Basic Data Visualization**
7. **Automate Email Sending**
8. **Simple API Creation (Flask)**
9. **Markdown to HTML Converter**
10. **URL Shortener**
11. **Contact Book with File Storage**
    
## Project Details

### 1. Basic Blog using Flask

A simple blog application built with Flask that includes:
- User authentication (not implemented in basic version)
- Create, read posts
- SQLite database storage
- Bootstrap styling

**Requirements:**
- Flask
- Flask-SQLAlchemy

**Setup:**
```bash
pip install flask flask-sqlalchemy
python app.py
```

### 2. Simple Web Scraper

A web scraper that extracts quotes from http://quotes.toscrape.com and saves them to a CSV file.

**Features:**
- Scrapes multiple pages
- Extracts quote text, author, and tags
- Saves data to CSV
- BeautifulSoup for HTML parsing

**Requirements:**
- requests
- beautifulsoup4

**Setup:**
```bash
pip install requests beautifulsoup4
python scraper.py
```

### 3. Weather App using API

A console application that fetches weather data from OpenWeatherMap API.

**Features:**
- Get current weather by city name
- Displays temperature, humidity, wind speed, etc.
- Saves weather data to JSON files
- Error handling for API requests

**Setup:**
1. Get a free API key from [OpenWeatherMap](https://openweathermap.org/)
2. Replace `YOUR_API_KEY` in `weather_app.py` with your actual key
3. Run:
```bash
python weather_app.py
```

### 4. Todo Application with File Persistence

A console-based todo application with JSON file storage.

**Features:**
- Add, complete, and delete tasks
- Set priorities and due dates
- Persistent storage in JSON format
- Simple console interface

**Setup:**
```bash
python todo_app.py
```

## Common Requirements

All projects require Python 3.6 or higher. It's recommended to use a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

## Project Structure

```
python-intermediate-projects/
│
├── blog-app/
│   ├── app.py
│   ├── templates/
│   │   ├── base.html
│   │   ├── home.html
│   │   ├── post.html
│   │   ├── create.html
│   │   └── about.html
│   └── blog.db
│
├── web-scraper/
│   ├── scraper.py
│   └── quotes.csv
│
├── weather-app/
│   ├── weather_app.py
│   └── [city]_weather.json
│
└── todo-app/
    ├── todo_app.py
    └── todos.json
```
### 5. File Organizer

Organizes files in a directory into subfolders based on file extensions.

**Features:**
- Categorizes files into Images, Documents, Audio, Videos, Archives, Code, and Others
- Handles duplicate filenames
- Can be run from command line with target directory as argument

**Usage:**
```bash
python file_organizer.py [directory_path]
```

### 6. Basic Data Visualization

Creates visualizations from CSV or Excel data files.

**Features:**
- Automatic detection of numeric and categorical columns
- Generates histograms, box plots, bar charts, and correlation heatmaps
- Displays basic statistics and data overview

**Usage:**
```bash
python data_visualization.py [data_file_path]
```

### 7. Automate Email Sending

Sends emails with optional attachments using SMTP.

**Features:**
- Supports Gmail SMTP (can be modified for other providers)
- Handles attachments
- Secure password input

**Usage:**
```bash
python email_sender.py
```
(Follow the interactive prompts)

### 8. Simple API Creation (Flask)

A RESTful API for a library management system.

**Features:**
- User authentication with tokens
- CRUD operations for books
- SQLite database backend
- Proper error handling

**Endpoints:**
- `/user` - User management
- `/book` - Book management
- `/login` - Authentication

**Setup:**
```bash
pip install flask flask-sqlalchemy
python flask_api.py
```

### 9. Markdown to HTML Converter

Converts Markdown files to HTML with basic styling.

**Features:**
- Supports common Markdown syntax
- Generates complete HTML documents
- Preserves original file structure

**Usage:**
```bash
python markdown_to_html.py input.md [output.html]
```

### 10. URL Shortener

A Flask-based URL shortening service.

**Features:**
- Generates unique short codes
- Tracks click statistics
- Persistent storage in SQLite

**Endpoints:**
- `/shorten` - Create short URL (POST)
- `/<short_code>` - Redirect to original URL
- `/stats/<short_code>` - Get URL statistics

**Setup:**
```bash
pip install flask
python url_shortener.py
```

### 11. Contact Book with File Storage

A command-line contact management system.

**Features:**
- JSON file storage
- CRUD operations for contacts
- Search functionality
- Timestamp tracking

**Usage:**
```bash
python contact_book.py
```
(Follow the interactive menu)

## Requirements

- Python 3.6+
- Required packages (install with `pip install -r requirements.txt`):
  ```
  flask
  flask-sqlalchemy
  pandas
  matplotlib
  seaborn
  ```

## How to Use

1. Clone this repository:
```bash
git clone https://github.com/yourusername/python-intermediate-projects.git
cd python-intermediate-projects
```

2. Navigate to each project directory and follow the specific setup instructions.

## License

This project is open-source and available under the MIT License.

## Contributing

Contributions are welcome! Please fork the repository and create a pull request with your improvements.

## Support

For any issues or questions, please open an issue in the repository.
