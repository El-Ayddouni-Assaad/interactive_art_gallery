from flask import Flask, render_template, request, redirect, url_for
import subprocess
import os
from data_visualization import generate_heatmap, generate_bar_chart
from filters import apply_image_filter, apply_audio_filter

app = Flask(__name__)
UPLOAD_FOLDER = "static/uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/gallery")
def gallery():
    return render_template("gallery.html")

@app.route("/run_art/<art_script>")
def run_art(art_script):
    color = request.args.get("color", "white")  
    shape = request.args.get("shape", "circle")  

    try:
        subprocess.run(["python", f"art/{art_script}.py", color, shape], check=True)
        message = f"Executed {art_script}.py successfully with color {color} and shape {shape}!"
    except Exception as e:
        message = f"Error running {art_script}.py: {str(e)}"
    
    return render_template("gallery.html", message=message)

@app.route("/data", methods=["GET", "POST"])
def show_data_visualization():
    if request.method == "POST":
        chart_type = request.form["chart_type"]
        
        if chart_type == "heatmap":
            generate_heatmap("static/weather_data.csv")
            return render_template("data.html", chart_image="static/heatmap.png", chart_type="Abstract Heatmap")
        elif chart_type == "bar_chart":
            generate_bar_chart("static/weather_data.csv")
            return render_template("data.html", chart_image="static/bar_chart.png", chart_type="Abstract Bar Chart")
    
    return render_template("data.html", chart_image=None)

@app.route("/filters", methods=["GET", "POST"])
def filters():
    if request.method == "POST":
        file = request.files["file"]
        filter_type = request.form["filter"]

        if file:
            file_path = os.path.join("static/uploads", file.filename)
            file.save(file_path)

            file_extension = file.filename.split(".")[-1].lower()
            image_formats = ["png", "jpg", "jpeg"]
            audio_formats = ["wav", "mp3", "ogg", "m4a", "aac", "flac", "wma"]

            if file_extension in image_formats:
                filtered_file = apply_image_filter(file_path, filter_type)
            elif file_extension in audio_formats:
                filtered_file = apply_audio_filter(file_path, filter_type)
            else:
                return render_template("filters.html", error="Unsupported file type.")
            
            return render_template("filters.html", filtered_file=filtered_file)
    
    return render_template("filters.html", filtered_file=None)

if __name__ == "__main__":
    app.run(debug=True)

