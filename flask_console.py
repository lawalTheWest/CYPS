#!/usr/bin/env python3
from flask import Flask, render_template

app = Flask(__name__)

posts = [
        {
            'author': 'Lawal Tajudeen Ogunsola',
            'title': 'The Importance of Agriculture',
            'contents': 'Agriculture is the bedrock of human civilization, providing sustenance, economic stability, and environmental balance. Its importance cannot be overstated, as it forms the foundation of food security, ensuring that communities have access to nutritious sustenance. Beyond sustenance, agriculture drives economies, providing livelihoods for millions globally. It fosters rural development, supporting local communities and preserving cultural heritage. Moreover, agriculture plays a crucial role in environmental conservation, with sustainable practices promoting soil health, biodiversity, and carbon sequestration. As populations grow and climates change, the significance of agriculture only amplifies, emphasizing the need for innovation and responsible stewardship of our agricultural resources.',
            'date_posted': 'May 4th, 2024'
        },
        {
            'author': 'Ogunsola Oguntoyibo',
            'title': 'The Importance of Agriculture',
            'contents': 'Agriculture is the bedrock of human civilization, providing sustenance, economic stability, and environmental balance. Its importance cannot be overstated, as it forms the foundation of food security, ensuring that communities have access to nutritious sustenance. Beyond sustenance, agriculture drives economies, providing livelihoods for millions globally. It fosters rural development, supporting local communities and preserving cultural heritage. Moreover, agriculture plays a crucial role in environmental conservation, with sustainable practices promoting soil health, biodiversity, and carbon sequestration. As populations grow and climates change, the significance of agriculture only amplifies, emphasizing the need for innovation and responsible stewardship of our agricultural resources.',
            'date_posted': 'May 4th, 1927'
        }
        ]

@app.route("/")
@app.route("/home")
def home():
    return render_template('index.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/login")
def login():
    return render_template('login.html')


if __name__ == '__main__':
    app.run(debug=True)
