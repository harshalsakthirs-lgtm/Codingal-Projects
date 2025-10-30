import cv2

image = cv2.imread('example/example.jpg')

def first():
    cv2.namedWindow("Loaded Image", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("Loaded Image", 800, 500)

    cv2.imshow("Loaded Image", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def second():
    image = cv2.imread('example/example.jpg')

    cv2.namedWindow("Loaded Image", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("Loaded Image", 100, 100)

    cv2.imshow("Loaded Image", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def third():
    image = cv2.imread('example/example.jpg')

    cv2.namedWindow("Loaded Image", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("Loaded Image", 500, 900)

    cv2.imshow("Loaded Image", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
print(first())
print(second())
print(third())