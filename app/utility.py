import os
import yaml
from flask import current_app

def get_chapter_file(tier, chapter_id):
    """
    Looks for: app/content/<tier>/registry.yaml
    Returns full path to the markdown file if found.
    """
    # 1. Locate the registry inside app/content/<tier>
    tier_dir = os.path.join(current_app.root_path, 'content', tier)
    registry_path = os.path.join(tier_dir, 'registry.yaml')

    if not os.path.exists(registry_path):
        return None

    # 2. Parse Registry
    try:
        with open(registry_path, 'r') as f:
            data = yaml.safe_load(f)
    except yaml.YAMLError:
        return None

    # 3. Find filename
    chapters = data.get('chapters', {})
    filename = chapters.get(chapter_id) # e.g., '01' -> '01_introduction.md'

    if not filename:
        return None

    # 4. Return full path and filename
    return tier_dir, filename


def get_static_file(file_key):
    """
    Looks for: app/static/registry.yaml
    Returns full path to the static file if found.
    """
    # 1. Locate registry inside app/static
    static_dir = os.path.join(current_app.root_path, 'static')
    registry_path = os.path.join(static_dir, 'registry.yaml')

    if not os.path.exists(registry_path):
        return None

    # 2. Parse Registry
    try:
        with open(registry_path, 'r') as f:
            data = yaml.safe_load(f)
    except yaml.YAMLError:
        return None

    # 3. Find filename
    # Assuming registry looks like: { files: { "headers.txt": "headers.txt" } }
    files = data.get('files', {})
    filename = files.get(file_key) 

    if not filename:
        return None

    return static_dir, filename