from flask import Flask

PORT = 8080 

app = Flask(__name__)

@app.route('/')
def hello_world():
    return f"<h1>Hello DevOps World!</h1><p>A Python (Flask) alkalmazás fut a {PORT} porton, és HTTP-n elérhető.</p>"

if __name__ == '__main__':
    # EZ KULCSFONTOSSÁGÚ: 
    # A host='0.0.0.0' nélkül a konténerben nem működne, és a helyi gép is problémázhat.
    app.run(host='0.0.0.0', port=PORT)