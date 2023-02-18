{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "import cv2\n",
    "import numpy as np\n",
    "import dlib\n",
    "cap = cv2.VideoCapture(0)\n",
    "\n",
    "detector = dlib.get_frontal_face_detector()\n",
    "while True:\n",
    "    ret, frame = cap.read()\n",
    "    frame = cv2.flip(frame, 1)\n",
    "    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)\n",
    "    faces = detector(gray)\n",
    "    i = 0\n",
    "    for face in faces:\n",
    "        x, y = face.left(), face.top()\n",
    "        x1, y1 = face.right(), face.bottom()\n",
    "        cv2.rectangle(frame, (x, y), (x1, y1), (0, 255, 0), 2)\n",
    "        i = i+1\n",
    "        cv2.putText(frame, 'face num'+str(i), (x-10, y-10),cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)\n",
    "        #print(face, i)\n",
    "    cv2.imshow('frame', frame)\n",
    "    if cv2.waitKey(1) & 0xFF == ord('q'):\n",
    "        break\n",
    "cap.release()\n",
    "cv2.destroyAllWindows()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3.10.7 64-bit",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.7"
  },
  "orig_nbformat": 4,
  "vscode": {
   "interpreter": {
    "hash": "63963b3f4c440940f0b94a3100916033a226cb4f45979123153792d60aa56d6a"
   }
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
