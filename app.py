from flask import Flask

PORT = 8080 

app = Flask(__name__)

@app.route('/')
def hello_world():
    # A szövegeket egyetlen strigként (vagy f-stringként) adjuk vissza
    return f"""
        <h1>Hello DevOps World!</h1>
        <p>A Python (Flask) alkalmazás fut a {PORT} porton, és HTTP-n elérhető.</p>
        <hr>
        <h1>Tallodi Imre Zsolt - NK: WLMURK DEVOPS beadandó</h1>
    """

if __name__ == '__main__':
        app.run(host='0.0.0.0', port=PORT)