import numpy as np
import cv2
import matplotlib.pyplot as plt

def find_object_sift(query_image, train_image):
    """
    Match features of two images using SIFT algorithm and display the results.
    """
    if query_image is None or train_image is None:
        print("Error: One of the images could not be loaded.")
        return
    
    img1, img2 = query_image.copy(), train_image.copy()
    
    # Create SIFT object
    sift = cv2.SIFT_create()
    
    # Extract keypoints and descriptors
    kp1, des1 = sift.detectAndCompute(img1, None)
    kp2, des2 = sift.detectAndCompute(img2, None)
    
    print("Number of features in the first image:", des1.shape if des1 is not None else "No features")
    print("Number of features in the second image:", des2.shape if des2 is not None else "No features")
    
    # Draw keypoints for the first image
    keypoints_img1 = cv2.drawKeypoints(img1, kp1, None, color=(0, 255, 0), flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
    
    # Draw keypoints for the second image
    keypoints_img2 = cv2.drawKeypoints(img2, kp2, None, color=(0, 255, 0), flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
    
    # Check if descriptors exist
    if des1 is None or des2 is None:
        print("Matching failed due to insufficient features.")
        return
    
    # Create BFMatcher and match features
    bf = cv2.BFMatcher(cv2.NORM_L1, crossCheck=False)
    matches = bf.match(des1, des2)
    matches = sorted(matches, key=lambda x: x.distance)  # Sort by distance
    
    print("Number of matched features:", len(matches))
    
    # Display top 10 matches
    img_matches = cv2.drawMatches(img1, kp1, img2, kp2, matches[:10], None, flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)
    
    # Show images
    plt.figure(figsize=(12, 6))
    plt.subplot(231), plt.imshow(cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)), plt.title("Query Image")
    plt.subplot(232), plt.imshow(cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)), plt.title("Train Image")
    plt.subplot(233), plt.imshow(img_matches), plt.title("Feature Matching")
    plt.subplot(234), plt.imshow(cv2.cvtColor(keypoints_img1, cv2.COLOR_BGR2RGB)), plt.title("Keypoints in Query Image")
    plt.subplot(235), plt.imshow(cv2.cvtColor(keypoints_img2, cv2.COLOR_BGR2RGB)), plt.title("Keypoints in Train Image")
    plt.show()

# Load images
i1 = cv2.imread('img/box.png')
i2 = cv2.imread('img/box_in_scene.png')

if i1 is None or i2 is None:
    print("Error: One of the images was not found. Please check the path.")
else:
    find_object_sift(i1, i2)