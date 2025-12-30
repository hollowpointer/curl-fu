from flask import Flask, render_template, request, Response
from termcolor import colored
from app.content import content_bp

app = Flask(__name__)
app.register_blueprint(content_bp, url_prefix='/')

@app.route('/')
def index():
    user_agent = request.user_agent
    if 'curl' in user_agent.string:
        welcome = colored('Welcome to Curl Fu!', 'green', attrs=['bold'])
        content = (
            f'\n{welcome}\n'
            'To begin your training, run:\n\n' 
            f'   curl {request.host}/start\n\n'
        )
        return Response(content, mimetype='text/plain')
    
    return render_template('index.html', environment = request.host)

if __name__ == '__main__':
    app.run()