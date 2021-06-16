"""
@author: Saurabh Singh
"""

#Importing necessary libraries
from flask_cors import CORS,cross_origin
from flask import Flask, render_template, request,jsonify
from scrapperImage.ScrapperImage import ScrapperImage
from businesslayer.BusinessLayerUtil import BusinessLayer
import os

#import request
app = Flask(__name__) #initialising the flask app with the name app

#response = 'Welcome'

@app.route('/') #route for redirecting to the home page
@cross_origin()
def home():
	return render_template('index.html')

@app.route('/showImages')
@cross_origin()
def displayImages():
	list_images=os.listdir('static')
	print(list_images)

	try:
		if(len(list_images)>0):
			return render_template('showImage.html',user_images=list_images)
		else:
			return "Images are not present"
	except Exception as e:
		print("No images found",e)
		return "Please try with different search keyword"

@app.route('/searchImages', methods=['Get','POST'])
def searchImage():
	if request.method =='POST':
		search_term=request.form['keyword']  #assigning the value of the input keyword to the variable keyword

	else:
		print("Please enter Something")

	imagescrapperutil = BusinessLayer #Instantiate an object for ScrapperImage class
	imagescrapper = ScrapperImage()
	list_images = os.listdir('static')
	imagescrapper.delete_downloaded_images(list_images) #Delete the old images before search

	image_name = search_term.split()
	image_name = "+".join(image_name)

	#We need to add the header metadata

	header = {'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36'}

	lst_images = imagescrapperutil.downloadImages(search_term,header)

	return displayImages() #redirect the control to the show images method



if __name__== "__main__":
	app.run(host='127.0.0.1',port=8000) #port to run on local machine
	#app.run(debug=True) #to run on cloud 