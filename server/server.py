from pyheaven import *
from flask import Flask, request, send_file
from werkzeug.utils import secure_filename

from app import Sound2Synth

SERVER_FOLDER = "server/"
UPLOAD_FOLDER = "input/"
DOWNLOAD_FOLDER = "output/"
MODEL_ENSEMBLE = []
with open("./server/ensemble.sh", "r") as f:
    MODEL_ENSEMBLE = [line.strip() for line in f]
ALLOWED_EXTENSIONS = {"test", "wav"}


def ALLOWED(file):
    return Format(file.filename) in ALLOWED_EXTENSIONS


app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = pjoin("./", SERVER_FOLDER, UPLOAD_FOLDER)
app.config["OUTPUT_FOLDER"] = pjoin("./", SERVER_FOLDER, DOWNLOAD_FOLDER)
app.config["DOWNLOAD_FOLDER"] = pjoin("./", DOWNLOAD_FOLDER)
app.config["MODEL_ENSEMBLE"] = MODEL_ENSEMBLE


@app.route("/", methods=["POST"])
def index():
    try:
        # file = request.files["Upload File"]
        # assert file and ALLOWED(file)
        # filename = secure_filename(file.filename)
        # filepath = pjoin(app.config["UPLOAD_FOLDER"], filename)
        # file.save(filepath)
        # preset = Sound2Synth(filepath, app.config["MODEL_ENSEMBLE"])
        # presetpath = AsFormat(pjoin(app.config["OUTPUT_FOLDER"], filename), "json")
        # SaveJson(preset, presetpath)
        # sendpath = AsFormat(pjoin(app.config['DOWNLOAD_FOLDER'], filename), "json")
        # sendpath = "/Users/loopbender/Downloads/AUG31.000009.048000.json"
        # sendpath = "/Users/loopbender/Downloads/RAND21.000204.048000.json"
        sendpath = "/Users/loopbender/Downloads/TEST21.002777.048000.json"
        # sendpath = "/Users/loopbender/Downloads/LARGE23.000328.048000.json"
        return send_file(sendpath, as_attachment=True)
    except Exception as e:
        print("{", e, "}")
        return "404"


if __name__ == "__main__":
    CreateFolder("./server/input/")
    CreateFolder("./server/output/")
    app.run(host="127.0.0.1", port=1234, debug=True)
