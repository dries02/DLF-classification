# DLF-segmentation

Hi there, fellow forester!

Here is how to use the API:

(0) You might need to install some packages to run the API. Unfortunately I don't know how to use Docker.

(1) Run api.py, which will load the serialized model and start up a local server. Visit http://localhost:8080/docs.

(2) Click on post/ predict to open a tab.

(3) Click on try it out.

(4) Browse to the image of your favorite image of a leaf and lean back while the model classifies it! See the API for more documentation.

Some limitations have already been outlined in the report. The biggest limitation is that it can only predict 15 Swedish leaf species, and most of the users are not Swedish. Of course, can still use the API with your own, custom model.
