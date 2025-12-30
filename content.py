from flask import Blueprint, Flask, render_template
import markdown
import os

content_bp = Blueprint('content', __name__)

@content_bp.route('/test')
def serve_markdown():
    file_path = os.path.join(os.path.dirname(__file__), 'README.md')
    
    with open(file_path, 'r', encoding='utf-8') as f:
        text = f.read()
    
    html_content = markdown.markdown(text)

    return render_template("content.html", content=html_content)