"""http://127.0.0.1:5000/training"""


from wsgiref import simple_server
from flask import Flask, Response, request, render_template
from flask_cors import CORS, cross_origin


app = Flask(__name__)
CORS(app)

@app.route('/training', methods=["POST"])
@cross_origin()
def training_route_client():
    try:
        return Response("Training successful!")
    except Exception as e:
        return Response(f"Training failed! {e}")


if __name__ == "__main__":
    # app.run()
    host = "0.0.0.0"
    port = 5000
    httpd = simple_server.make_server(host, port, app)
    httpd.serve_forever()
