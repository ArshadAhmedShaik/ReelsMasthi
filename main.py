from flask import Flask, render_template, request
import uuid
import os
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = 'user_uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/create", methods = ["GET", "POST"])
def create():
    myid = uuid.uuid1()
    if request.method == "POST":
        rec_id = request.form.get("uuid")
        desc = request.form.get("text")
        input_files = []
        for key,value in request.files.items():
                file = request.files[key]
                print(file)
                print(file.filename)
                if file:
                    filename = secure_filename(file.filename)
                    if(not os.path.exists(os.path.join(app.config['UPLOAD_FOLDER'], rec_id))):
                        os.mkdir(os.path.join(app.config['UPLOAD_FOLDER'], rec_id))
                    file.save(os.path.join(app.config['UPLOAD_FOLDER'], rec_id ,filename))
                    input_files.append(filename)
        # capture the description and save it to a file
                with open(os.path.join(app.config['UPLOAD_FOLDER'], rec_id , "desc.txt"), "w") as f:
                     f.write(desc)  
        for f1 in input_files:
              with open(os.path.join(app.config['UPLOAD_FOLDER'], rec_id, "input.txt"), "a") as f:
                   f.write(f"file '{f1}'\n duration 1\n")

    return render_template("create.html", myid=myid)

@app.route("/gallery")
def gallery():
    reels = os.listdir("static/reels")
    print(reels)
    return render_template("gallery.html", reels=reels)

app.run(debug=True)