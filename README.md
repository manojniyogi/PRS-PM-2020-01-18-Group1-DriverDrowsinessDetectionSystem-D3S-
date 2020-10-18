### Driver Drowsiness Detection(D3S)

---

## SECTION 1 : PROJECT TITLE
## Driver Drowsiness Detection(D3S)  - Deep learning model to alarm if driver is drowsy.

---

## SECTION 2 : EXECUTIVE SUMMARY / PAPER ABSTRACT

**Summary**

Researchers estimate that more than 70 million Americans suffer from a sleep disorder. (Institute of Medicine, 2005) One of the most serious consequences of insufficient sleep is traffic accidents due to drowsy driving.

Experts suspect that even these disturbingly high figures underestimate the number of accidents or near-miss accidents due to drowsy driving because of drivers being unaware or not admitting they were drowsy at the time of the accident, or police not acquiring that information.

In spite of education to create awareness among driving community, policy initiatives by the Government to reduce the accidents numbers show no promising decline. In recent years, many of the luxury car companies have already moved in this direction but majority of the solutions are relatively employing complex sensors and devices which are costly and so is the need for simple, effective relatively low cost solutions that can be used by everyone.

Drowsy driving is a prevalent and serious public health issue that requires a simple low cost, fool proof continuous monitoring system that can be used by everyone.

**Objective**

Driver face/eye monitoring – This technique is simple and low-cost model relatively compared to other models and can be used in majority of the vehicles. The only limitation of this model is that the driver should not use dark colored spectacles that obscures the monitoring of eyes. 
This technique monitors the state of eyes and if both the eyes are in a closed state for a defined threshold time, alarm is raised to draw attention of the driver.


**Development Methodology**

The approach follows the CRISP-DM process. It consists of five stages, as listed below:
1)	Understand the Business Requirements
2)	Understanding & Analyzing the Data
3)	Verify / Optimize the model
4)	Analyze the results and reveal the insights
The approach uses pre-trained model and follows technique termed as Transfer Learning. We have picked up the pretrained model from http://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2. 
The adopted approach is algorithmically simple, intuitive, and easy to implement. It is easily portable to different platforms. It is computationally in expensive as the training is done offline and the trained model is picked up for use.

**Technologies Used**

The model developed for the project work uses Python and following open source libraries:

•	Numpy – Statistical and Scientific Computing

•	Cv2 – Computer Vision library

•	Dlib – Predictor and detector library

•	Imutils – Utility library for object landmarks

•	Matplotlib – Graphing library

**Environment Used**

•	PyCharm community edition for interactive computing environment for coding in python.


**Our Approach**

Step 1 – We have used a laptop with web cam facility to capture the images from video stream

Step 2 – Laptop with python and PyCharm editor installed for programming

Step 3 – Download and place extracted pretrained model viz., from Shape Predictor accessible to the program.

Step 4 – Program in python to detect faces from the video stream.

Step 5 – Resize and transform the image captured into gray scale as we are merely interested in capturing the state of eyes and it does not matter if the image is color or gray scale.

Step 6 – Apply facial landmark localization to extract eye regions from the face.

Step 7 – Compute the aspect ratio to determine if the eyes are closed or open.

Step 8 – Trigger alarm if the aspect ratio is below the threshold value for preset duration.

---

## SECTION 3 : CREDITS / PROJECT CONTRIBUTION

| Official Full Name  | Student ID (MTech Applicable)  | Work Items (Who Did What) | Email (Optional) |
| :------------ |:---------------:| :-----| :-----|
| Maradana Vijayakrishna | A0178453W |Overall system design, modelling, use case & algorithm design, system implementation | mvskrishna@yahoo.com |
| Putrevu Manoj Niyogi | A0213557E |Overall system design, modelling, technical architecture design, system implementation | manojniyogi@yahoo.com |
| Sivasankaran Balakrishnan | A0065970X |Overall system design, modelling, technical architecture design, system implementation | bsivaa@gmail.com |

---

## SECTION 4 : VIDEO OF SYSTEM MODELLING & USE CASE DEMO
<div align="center">
  <a href="https://youtu.be/LX3SzWYeCGo">
    <img src="http://i3.ytimg.com/vi/LX3SzWYeCGo/hqdefault.jpg" alt="CHURN Project Video">
  </a>
</div>

---

## SECTION 5 : INSTALLATION & USER GUIDE

`Refer to "Driver Drowsiness Detection(D3S) - Project Insatallation-User Guide.docx" document at Github Folder: ProjectReport`

---

## SECTION 6 : PROJECT REPORT / PAPER

`Refer to "Driver Drowsiness Detection(D3S) - Project Report.docx' document at Github Folder: ProjectReport`

---

## SECTION 7 : MISCELLANEOUS

`Refer to Github Folder: Miscellaneous`

---

