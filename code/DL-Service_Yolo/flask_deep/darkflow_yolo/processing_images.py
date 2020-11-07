import os, sys
import numpy as np
import cv2
from darkflow.net.build import TFNet
from tensorflow.keras.preprocessing.image import save_img
from PIL import Image
#from yolo import YOLO

def boxing(original_img, predictions):
	newImage = np.copy(original_img)
	# colors = [tuple(255 * np.random.rand(3)) for i in range(10)]
	color = (205, 254, 12) #CDFE0C

	# pull out some info from the results
	for result in predictions:
		tl = (result['topleft']['x'], result['topleft']['y'])			# topleft
		br = (result['bottomright']['x'], result['bottomright']['y'])	# bottomright
		
		confidence = result['confidence']
		label = result['label']+" "+str(round(confidence, 2))

		# add the box and label and display it
		if confidence > 0.3:
			newImage = cv2.rectangle(newImage, tl, br, color, 3)
			newImage = cv2.putText(newImage, label, tl, cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 2, cv2.LINE_AA)

	return newImage

def main(user_img_path):
	os.chdir('./flask_deep/darkflow_yolo')
	print('-------------------------------------')
	print(user_img_path)
	user_img_name = user_img_path.split('/')[-1].split('.')[0]
	print('-------------------------------------')

	# define the model options and run
	model_path = './cfg/trained_weights_final.h5'
	class_path = './bin/classes.txt'

	'''
	yolo = YOLO(model_path=model_path, classes_path=class_path)
	'''
	# read the color image and covert to RGB
	img = cv2.imread(user_img_path, cv2.IMREAD_COLOR)
	#img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

	# use YOLO to predict the image
	'''
	result = yolo.detect_image(img)
	detected_img = result
	'''
	#detected_img = boxing(img, result)

	# save
	'''
	detected_img_path = '../static/images/'+str(user_img_name)+'_detected.png'
	save_img(detected_img_path, detected_img)
	'''
	detected_img_path = '../static/images/0017_detected.png'
	#save_img(detected_img_path, detected_img)

	# plt.imshow(detected_img)
	# plt.show()

	return detected_img_path

if __name__ == "__main__":
	main()