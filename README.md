Introduction
The Interactive Generative Art Gallery is a web-based application developed in Python using the Flask framework. The gallery allows users to explore and interact with generative artworks, visualize datasets creatively, and manipulate images and audio in an artistic way.
Installation Instructions
(Before running the project, ensure that you have installed python 3.8+)
1)	Download or clone the project from the repository.
2)	Create and activate a virtual environment.
3)	Install the required libraries.
4)	Run the application.
5)	Copy the localhost url displayed in the terminal.
6)	Paste the url in your browser to access the platform.
Project Structure
1)	art (Python)
art1:drawing many shapes randomly on the terminal.
art2: drawing many shapes in an organized way.
art3: drawing a spiral.
art4: drawing using one shape and one color decided by the user.
2)	static
Images of the heat-map/chart-bar according to the desire of the user.
3)	uploads
Contains the image/audio uploaded by the user and the result after the user chooses the filter.
4)	templates (HTML)
base.html: node connecting the HTML files with the CSS file.
index.html: home page.
data.html: data visualization’s page.
filters.html: image/audio filter’s page.
gallery.html: drawing art’s page.
5)	app.py
Connecting the back-end with the front-end.
6)	data_visualization.py
Gets the dataset and give the heat-map or the chart-bar.
7)	filters.py
Contains the apply_image_filters and apply_audio_filters.
Author
Developed by EL AYDDOUNI ASSAAD and ZENTARI ABDERRAHMAN
