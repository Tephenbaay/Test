from flask import Flask

app = FLask(__name__)

@app.route("/", methods=['GET'])
def home():
    return "<h1>This is a sample App</h1>"

if __name__ == "__main__":
    app.run()