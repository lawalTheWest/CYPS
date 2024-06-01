# Crop Yield Prediction System (CYPS)

## Overview
The Crop Yield Prediction System (CYPS) is a web application designed to provide detailed information about various crops, including their scientific names, descriptions, uses, nutritional values, and optimal growing conditions. This system allows users to view a list of crops and access detailed information about each crop.

## Features
- List of crops with links to detailed information.
- Detailed crop pages with sections on scientific name, description, uses, nutritional values, and growing conditions.
- User-friendly interface for navigating crop information.

## Technologies Used
- **Python 3**: The core programming language used for backend development.
- **Flask**: A lightweight WSGI web application framework used for building the web application.
- **HTML/CSS**: For structuring and styling the web pages.
- **Jinja2**: For templating in Flask.

## Installation

### Prerequisites
- Python 3.x installed on your machine.
- `pip`, the Python package installer.

### Steps
1. **Clone the repository**:
    ```sh
    git clone https://github.com/lawalTheWest/_CYPS_.git
    cd crop-yield-prediction
    ```

2. **Create and activate a virtual environment** (optional but recommended):
    ```sh
    python3 -m venv venv
    source venv/bin/activate
    ```

3. **Install the required packages**:
    ```sh
    pip install -r requirements.txt
    ```

4. **Run the application**:
    ```sh
    export FLASK_APP=run.py
    export FLASK_ENV=development
    flask run
    ```
    The application should now be running at `http://127.0.0.1:5000/`.

## Project Structure

```

CYPS/
├── app
│   ├── api.py
│   ├── crops.py
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── crops.cpython-310.pyc
│   │   ├── crops.cpython-38.pyc
│   │   ├── __init__.cpython-310.pyc
│   │   ├── __init__.cpython-38.pyc
│   │   ├── routes.cpython-310.pyc
│   │   └── routes.cpython-38.pyc
│   ├── README.md
│   └── routes.py
├── config.py
├── old.py
├── __pycache__
│   ├── app.cpython-38.pyc
│   ├── config.cpython-310.pyc
│   └── config.cpython-38.pyc
├── README.md
├── run.py
├── static
│   ├── css
│   │   ├── about.css
│   │   ├── common.css
│   │   ├── crops.css
│   │   ├── footer.css
│   │   ├── header.css
│   │   ├── index.css
│   │   └── README.md
│   ├── images
│   │   └── lawal.jpg
│   ├── js
│   │   └── script.js
│   └── README.md
└── templates
    ├── 404.html
    ├── about.html
    ├── base.html
    ├── blog.html
    ├── crop_detail.html
    ├── crops.html
    ├── index.html
    ├── layout.html
    ├── README.md
    └── weather.html

```

- **app/**: Contains the application modules and packages.
	- **api.py**: API endpoints for the application.
	- **crops.py**: Contains the crop data.
	- **routes.py**: Contains the Flask routes for handling web requests.
	- **__init__.py**: Initializes the Flask application.
- **config.py**: Configuration settings for the Flask application.
- **old.py**: (Deprecated or old code if not in use).
- **run.py**: The main entry point to run the Flask application.
- **static/**: Contains static files like CSS, JavaScript, and images.
- **templates/**: Contains HTML templates for the web pages.
- **README.md**: Project documentation (this file).

## Usage
- Navigate to `/crops` to see the list of all crops.
- Click on any crop name to view detailed information about that crop.
- advanced features Coming soon...

## Contributing
Contributions are welcome! Please follow these steps to contribute:
1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Commit your changes.
4. Push the branch to your fork.
5. Create a pull request with a detailed description of your changes.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact
For any questions or suggestions, feel free to open an issue or contact me at [lwltjdn@gmail.com](mailto:lwltjdn@gmail.com).
