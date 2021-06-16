"""
Created on Tue 15 June 2021
@author: Saurabh Singh
"""

from scrapperImage.ScrapperImage import ScrapperImage

class BusinessLayer:

	keyword=""
	fileLoc=""
	image_name=""
	header=""

	def downloadImages(keyWord, header):
		imgScrapper = ScrapperImage
		url = imgScrapper.createImageUrl(keyWord)
		rawHtml = imgScrapper.scrap_html_data(url, header)

		imageURLList = imgScrapper.getimageUrlList(rawHtml)

		masterListofImages = imgScrapper.downloadImagesFromURL(imageURLList,keyWord,header)

		return masterListofImages