import os
import io
import markdown
from flask import Blueprint, abort, render_template, request, Response
from rich.console import Console
from rich.markdown import Markdown
from app import utility

content_bp = Blueprint('content', __name__)

@content_bp.route('/<tier>/<chapter>')
def serve_markdown(tier, chapter):
    file_name = utility.get_file_from_registry(tier, chapter)
    if not file_name:
        abort(404)

    file_path = os.path.join(os.getcwd(), 'content', tier, file_name)

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            text = f.read()

        ua = request.user_agent.string.lower()
        # Terminal Clients
        if any(tool in ua for tool in ['curl', 'wget', 'httpie']):
            with io.StringIO() as string_io:
                console = Console(file=string_io, force_terminal=True, width=80)
                console.print(Markdown(text))
                return Response(string_io.getvalue(), mimetype='text/plain')

        # Web Browser
        content = markdown.markdown(text, extensions=['fenced_code', 'tables'])
        return render_template("content.html", content=content)
    
    except FileNotFoundError:
        return f"File missing at: {file_path}", 404