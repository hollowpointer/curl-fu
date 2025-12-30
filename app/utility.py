import os
import yaml

def get_file_from_registry(tier, chapter):
    registry_path = os.path.join(os.getcwd(), 'content', tier, 'registry.yaml')

    if not os.path.exists(registry_path):
        return None
    
    with open(registry_path, 'r') as f:
        data = yaml.load(f, Loader=yaml.SafeLoader)
    
    chapters = data.get('chapters', {})
    filename = chapters.get(chapter)

    return filename