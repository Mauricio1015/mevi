# Mevi 🤖
The code is an AI assistant that can be used to perform various tasks such as playing music, searching the web, setting alarms, and opening applications. It is written in Python and uses the following libraries:

* Speech Recognition: This library is used to recognize speech input from the user.
* subprocess: This library is used to run system commands.
* pyttsx3: This library is used to synthesize speech output.
* wikipedia: This library is used to access the Wikipedia API.
* pywhatkit: This library is used to play YouTube videos and search the web.
* datetime: This library is used to get the current time.
* keyboard: This library is used to read keyboard input.
* cam: This library is used to capture images.
* reconocimientofacial: This library is used to recognize faces.

The code is divided into two functions: listen() and run_mevi(). The listen() function listens for speech input from the user and returns the recognized text. The run_mevi() function continuously runs until the user says "adios". It then executes the commands that are given by the user.

Here is an example of how the code can be used:

* User: "Play music"
* Assistant: "What song would you like to play?"
* User: "Play Despacito"
* Assistant: "Playing Despacito"

The assistant can also be used to search the web, set alarms, open applications, and more. For a full list of commands, please see the documentation for the individual libraries that are used.

To run the code, first install the required libraries. Then, open the code in a text editor and save it as mevi.py. Finally, run the code by typing the following command in the terminal:

```
python mevi.py
```
# Cam 📷
The code you provided is for a program that captures video from a webcam and detects objects of different colors. The program uses the OpenCV library to perform the color detection.

The first step is to import the necessary libraries. The `cv2` library provides the functions for capturing video and performing color detection. The `mevi` library provides the function for drawing contours around objects. The `numpy` library provides the function for creating arrays.

The next step is to define the functions for drawing contours and checking if an object is red. The `draw` function takes a mask, a color, and a frame as input and draws the contours of the objects in the mask on the frame. The `check_red` function takes a color as input and returns a boolean value indicating whether the color is red.

The `capture` function is the main function of the program. It captures video from the webcam and performs color detection. The function first creates a VideoCapture object and sets the input device to 0, which is the webcam. The function then defines the lower and upper bounds for the colors to be detected. The function then loops over the frames from the webcam. For each frame, the function converts the frame to HSV color space and creates masks for each of the colors to be detected. The function then draws the contours of the objects in the masks on the frame. The function finally checks if the user has pressed the 's' key. If the user has pressed the 's' key, the function breaks out of the loop and releases the webcam and destroys all of the windows.

Here is a step-by-step explanation of the code:

1. The `cv2` library is imported.
2. The `mevi` library is imported.
3. The `numpy` library is imported.
4. The `draw` function is defined.
5. The `check_red` function is defined.
6. The `capture` function is defined.
7. The `main` function is called.

I hope this helps!
# face recognition 📹
The code you provided is for face recognition. It uses the face_recognition library to detect and compare faces.

The first step is to import the cv2 and face_recognition libraries.

```
import cv2
import face_recognition
```

Next, we need to load the image of the person we want to recognize.

```
image = cv2.imread("IMG/YO.jpg")
```

We can then use the face_recognition.face_locations() function to find the location of the faces in the image.

```
face_log = face_recognition.face_locations(image)[0]
```

The output of this function will be a list of tuples, each of which contains the coordinates of the four corners of a face.

We can then use the face_recognition.face_encodings() function to get a unique encoding for each face.

```
face_image_encoding = face_recognition.face_encodings(image, known_face_locations=[face_log])[0]
```

The output of this function will be a numpy array that contains the facial features of the face.

We can now use the face_recognition.compare_faces() function to compare the encoding of the face in the image to the encoding of the face we want to recognize.

```
result = face_recognition.compare_faces([face_image_encoding], face_frame_encodings)
```

The output of this function will be a list of boolean values, one for each face in the image. The value will be True if the face matches the face we want to recognize, and False if it does not.

We can then use the results of the face comparison to draw a bounding box around the face and display a text message indicating whether or not the face was recognized.

```
if result[0] == True:
    text = "Reconocido"
    color = (125, 220, 0)
else:
    text = "Desconocido"
    color = (50, 50, 255)
cv2.rectangle(frame, (face_location[3], face_location[2]), (face_location[1], face_location[2] + 30), color, -1)
cv2.
```
# windows installation 🪟
This is a .bat file that installs the necessary libraries for the program to run.

To run it, open a command prompt and navigate to the folder where the file is located. Then, type the following command:

```
InstaladorDeLibrerias.bat
```

The file will then download and install the necessary libraries.

Here are the steps on how to install the libraries manually:

1. Open a command prompt and navigate to the folder where the file is located.
2. Type the following command:

```
pip install SpeechRecognition
```

This will install the SpeechRecognition library.

3. Type the following command:

```
pip install pyttsx3
```

This will install the pyttsx3 library.

4. Type the following command:

```
pip install pyAudio
```

This will install the pyAudio library.

5. (Optional) If you get an error message saying that pyAudio could not be installed, you can try the following command:

```
pip install pyAudio --install-option="--no-warn-deprecated-pip"
```

6. Type the following command:

```
pip install pywhatkit
```

This will install the pywhatkit library.

7. Type the following command:

```
pip install pygame
```

This will install the pygame library.

8. Type the following command:

```
pip install keyboard
```

This will install the keyboard library.

9. Type the following command:

```
pip install numpy
```

This will install the numpy library.

10. Type the following command:

```
pip install opencv-contrib-python
```

This will install the opencv-contrib-python library.

11. Type the following command:

```
pip install wikipedia
```

This will install the wikipedia library.

12. Type the following command:

```
pip install cmake
```

This will install the cmake library.

13. Type the following command:

```
pip install dlib
```

This will install the dlib library.

14. Type the following command:

```
pip install face_recognition
```
# installation on linux 🐧
This is a bash script that installs the necessary Python libraries for the AsistenteVirtual project.

To install the script, run the following command:

```
bash InstaladorDeLibrerias.bash
```

The script will install the following libraries:

* Python 3-pyaudio
* SpeechRecognition
* pyttsx3
* pyAudio
* pywhatkit
* pygame
* keyboard
* numpy
* opencv-contrib-python
* wikipedia
* cmake
* dlib
* face_recognition

Here are the steps involved in the script:

1. The script first checks if Python 3 is installed. If it is not installed, the script will install it.
2. The script then checks if the pip package manager is installed. If it is not installed, the script will install it.
3. The script then installs the following libraries:

    * Python 3-pyaudio
    * SpeechRecognition
    * pyttsx3
    * pyAudio
    * pywhatkit
    * pygame
    * keyboard
    * numpy
    * opencv-contrib-python
    * wikipedia
    * cmake
    * dlib
    * face_recognition

4. The script finally prints a message to confirm that the libraries have been installed.

I hope this helps!