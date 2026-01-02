from flask import Blueprint, abort, send_from_directory, request, render_template, current_app
from rich.console import Console
from rich.markdown import Markdown as RichMarkdown
from app import utility
import markdown
import io
import os

content_bp = Blueprint('content', __name__)

def render_rich_ansi(filepath):
    """Renders Markdown to ANSI string for CLI tools."""
    try:
        with open(filepath, 'r') as f:
            content = f.read()
            
        string_io = io.StringIO()
        console = Console(file=string_io, force_terminal=True)
        console.print(RichMarkdown(content))
        return string_io.getvalue()
    except Exception as e:
        return f"Error rendering content: {str(e)}"



def render_html_for_browser(filepath):
    """Renders Markdown to HTML for Browsers."""
    try:
        with open(filepath, 'r') as f:
            md_content = f.read()
        
        html_content = markdown.markdown(md_content, extensions=['fenced_code', 'tables'])
        
        return render_template('content.html', content=html_content)
    except Exception as e:
        abort(500, description=f"Error rendering HTML: {str(e)}")



def is_cli_client():
    """Detects if the request is coming from a CLI tool."""
    user_agent = request.user_agent.string.lower()
    return 'curl' in user_agent or 'wget' in user_agent or 'httpie' in user_agent



@content_bp.route('/<tier>/<chapter>')
def serve_chapter(tier, chapter):
    result = utility.get_chapter_file(tier, chapter)
    
    if not result:
        abort(404)
        
    directory, filename = result
    full_path = os.path.join(directory, filename)

    if filename.endswith('.md'):
        if is_cli_client():
            return render_rich_ansi(full_path)
        else:
            return render_html_for_browser(full_path)

    return send_from_directory(directory, filename)



@content_bp.route('/<file_key>')
def serve_static_file(file_key):
    result = utility.get_static_file(file_key)
    
    if not result:
        abort(404)
        
    directory, filename = result
    full_path = os.path.join(directory, filename)

    if filename.endswith('.md'):
        if is_cli_client():
            return render_rich_ansi(full_path)
        else:
            return render_html_for_browser(full_path)

    return send_from_directory(directory, filename)