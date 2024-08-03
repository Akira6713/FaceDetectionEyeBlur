#------------------------ MTCNN Model with TensorFlow w/ Processing Color--------------------------------


import os
import cv2
import numpy as np
from mtcnn import MTCNN

# Set environment variable to turn off oneDNN custom operations
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'

# Load MTCNN face detector
detector = MTCNN()


def preprocess_image(image):
    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Histogram Equalization
    gray = cv2.equalizeHist(gray)

    # Convert back to BGR
    processed_image = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)

    return processed_image


def blur_eye(image, eye_center, size=30):
    eye_x, eye_y = eye_center
    eye_x = max(0, eye_x - size // 2)
    eye_y = max(0, eye_y - size // 2)
    eye_w = size
    eye_h = size

    # Ensure the ROI is within image bounds
    if eye_x + eye_w > image.shape[1] or eye_y + eye_h > image.shape[0]:
        print(f"Eye ROI out of bounds: ({eye_x}, {eye_y}, {eye_w}, {eye_h})")
        return image

    eye_roi = image[eye_y:eye_y + eye_h, eye_x:eye_x + eye_w]
    eye_roi = cv2.GaussianBlur(eye_roi, (199, 199), 50)
    image[eye_y:eye_y + eye_h, eye_x:eye_x + eye_w] = eye_roi
    return image


def detect_and_blur_eyes(image_path, output_path):
    # Read the original image
    image = cv2.imread(image_path)
    if image is None:
        print("Error loading image.")
        return

    # Create a copy of the original image for processing
    original_image = image.copy()

    # Preprocess the image
    preprocessed_image = preprocess_image(image)

    # Detect faces and facial landmarks on the preprocessed image
    results = detector.detect_faces(preprocessed_image)
    print(f"Detected {len(results)} faces")

    # Process each detected face
    for result in results:
        try:
            # Get the bounding box for the face
            x, y, w, h = result['box']
            cv2.rectangle(original_image, (x, y), (x + w, y + h), (0, 0, 255), 2)

            # Get the coordinates of the eyes
            keypoints = result['keypoints']
            left_eye = keypoints['left_eye']
            right_eye = keypoints['right_eye']

            # Blur the eyes on the original color image
            original_image = blur_eye(original_image, left_eye)
            original_image = blur_eye(original_image, right_eye)

        except Exception as e:
            print(f"Error during face or eye processing: {e}")
            continue

    # Save the output image
    try:
        cv2.imwrite(output_path, original_image)
    except Exception as e:
        print(f"Error saving output image: {e}")
        return

