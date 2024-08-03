# Face Detection and Eye Blurring with MTCNN

## Overview

This project utilizes an artificial intelligence algorithm for face detection and feature blurring in images using the Multi-task Cascaded Convolutional Networks (MTCNN) model. The algorithm is designed to detect human faces and anonymize them by blurring the eyes, enhancing privacy. It handles various lighting conditions and face orientations by employing several image processing techniques.

## Features

- **Face Detection:** Detects human faces in images using the MTCNN model.
- **Eye Blurring:** Anonymizes faces by blurring the eyes.
- **Image Processing:** Includes preprocessing steps like histogram equalization, grayscale conversion, and Gaussian blurring to improve detection accuracy.

## Requirements

- Python 3.x
- OpenCV
- Numpy
- MTCNN
- TensorFlow

## Sample Images

Below are some sample images processed by the algorithm. The original images are on the left, and the processed images with blurred eyes are on the right.

![Robot Sample](https://github.com/user-attachments/assets/415e3f4a-4dac-4f02-aa03-f4b85c0c2d99)
![Robot Sample 2](https://github.com/user-attachments/assets/d9a5b11f-9224-4b1a-8910-51efbadb55d8)
![Garden Sample](https://github.com/user-attachments/assets/8b2913c8-2301-4bfa-8058-4e7635e1acad)
![Fishing Sample](https://github.com/user-attachments/assets/b7413278-c4b0-4196-882e-203e24875d68)
![Disney Sample](https://github.com/user-attachments/assets/083e3260-2e8b-49a8-8051-968c1770a83a)
![Disney Sample](https://github.com/user-attachments/assets/d9d22106-026f-4116-9245-32920889e2f8)

## Potential Applications

This technology can be used for various privacy protection and security purposes:

- **Public Surveillance:** Enhances privacy by anonymizing individuals in video feeds, making it suitable for use in public places like airports, shopping malls, and streets.
- **Social Media:** Protects personal identity in shared photos, ensuring compliance with data protection regulations.
- **Data Protection:** Useful in legal and compliance scenarios where sensitive facial information needs to be obscured to protect individuals' privacy.
- **Smart Home Devices:** Can be integrated into smart home cameras to anonymize faces before storing or sharing footage.

Feel free to explore the code, modify it, and use it for your own projects. If you encounter any issues or have suggestions, please open an issue or contact me directly.
