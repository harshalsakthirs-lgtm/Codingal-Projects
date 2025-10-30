import cv2

image = cv2.imread("example/example.jpg")

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

resized_image = cv2.resize(gray_image, (224, 224))

cv2.imshow("Processed Image", resized_image)
key = cv2.waitKey(0)

if key == ord('s'):
    cv2.imwrite("example/example.jpg", resized_image)
    print("Image Saved as grayscale_with_opencv.jpg")
else:
    print("Image not Saved")

cv2.destroyAllWindows()

print(f"Processed Image dimension: {resized_image.shape}")