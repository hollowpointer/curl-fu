from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    user_agent = request.user_agent
    if "curl" in user_agent.string:
        return (
            "\n\033[1;32mWelcome to Curl Fu!\033[0m\n"
            "To begin your training, run: \n\n"
            f"    curl {request.host}/start\n\n"
        )

    
    return render_template('index.html', environment = request.host)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)