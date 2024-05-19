# Crop Yield Prediction System

The Crop Yield Prediction System is a web application designed to provide farmers with detailed information about various crops, including optimal growing conditions, storage recommendations, and yield predictions. The system aims to enhance agricultural productivity and sustainability by leveraging data-driven insights.

## Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [Project Structure](#project-structure)
- [Setup and Installation](#setup-and-installation)
- [Running the Application](#running-the-application)
- [Usage](#usage)
- [Future Enhancements](#future-enhancements)
- [Contributing](#contributing)
- [License](#license)

## Features

- **Detailed Crop Information:** Learn about various crops, including their species, types, and optimal growing conditions.
- **Yield Predictions:** Use data-driven insights to predict crop yields and plan accordingly.
- **Storage Recommendations:** Get advice on the best storage practices to maintain crop quality.
- **User-Friendly Interface:** Easy navigation through different pages including Home, About Us, Crops, and Blog.

## Technologies Used

- **Backend:** Python, Flask
- **Frontend:** HTML, CSS (with Jinja2 templating)
- **Styling:** Custom CSS
- **Web Server:** Flask's development server

## Project Structure

crop_yield_prediction/
├── app.py
├── templates/
│ ├── layout.html
│ ├── index.html
│ ├── about.html
│ ├── crops.html
│ ├── crop_detail.html
│ ├── blog.html
├── static/
│ └── styles.css


## Setup and Installation

1. **Clone the Repository**
	```
	git clone https://github.com/yourusername/crop_yield_prediction.git
	cd crop_yield_prediction
	```

2. **Create and Activate a Virtual Environment**
	```
	python3 -m venv venv
	source venv/bin/activate   # On Windows use `venv\Scripts\activate`
	```

3. **Install Dependencies**
	```
	pip install flask
	```
