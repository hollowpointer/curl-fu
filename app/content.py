from flask import Blueprint, abort, render_template
from app import utility
import os
import markdown


content_bp = Blueprint('content', __name__)

@content_bp.route('/<tier>/<chapter>')
def serve_markdown(tier, chapter):
    file_name = utility.get_file_from_registry(tier, chapter)

    if file_name is None:
        abort(404)

    file_path = os.path.join(os.getcwd(), 'content', tier, file_name)

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            text = f.read()
        html_content = markdown.markdown(text)
        return render_template("content.html", content=html_content)
    
    except FileNotFoundError:
        return f"File missing at: {file_path}", 404