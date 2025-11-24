from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    # Portfolio data - easy to edit
    portfolio_data = {
        'name': 'Kris',
        'role': 'Full Stack Developer',
        'about': 'I build accessible, pixel-perfect, and performant web experiences.',
        'skills': [
            {'name': 'Python', 'icon': 'fab fa-python'},
            {'name': 'Flask', 'icon': 'fas fa-flask'},
            {'name': 'JavaScript', 'icon': 'fab fa-js'},
            {'name': 'React', 'icon': 'fab fa-react'},
            {'name': 'HTML5', 'icon': 'fab fa-html5'},
            {'name': 'CSS3', 'icon': 'fab fa-css3-alt'},
        ],
        'projects': [
            {
                'title': 'E-Commerce Platform',
                'description': 'A full-featured online store with payment integration.',
                'tags': ['Flask', 'Stripe', 'PostgreSQL'],
                'link': '#'
            },
            {
                'title': 'Task Manager',
                'description': 'Real-time collaboration tool for remote teams.',
                'tags': ['React', 'Firebase', 'Tailwind'],
                'link': '#'
            },
            {
                'title': 'AI Dashboard',
                'description': 'Analytics dashboard with predictive modeling.',
                'tags': ['Python', 'D3.js', 'TensorFlow'],
                'link': '#'
            }
        ],
        'socials': [
            {'name': 'GitHub', 'url': 'https://github.com', 'icon': 'fab fa-github'},
            {'name': 'LinkedIn', 'url': 'https://linkedin.com', 'icon': 'fab fa-linkedin'},
            {'name': 'Instagram', 'url': 'https://instagram.com', 'icon': 'fab fa-instagram'},
            {'name': 'Twitter', 'url': 'https://twitter.com', 'icon': 'fab fa-twitter'},
            {'name': 'Email', 'url': 'mailto:hello@example.com', 'icon': 'fas fa-envelope'}
        ]
    }
    return render_template('index.html', data=portfolio_data)

import os

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

