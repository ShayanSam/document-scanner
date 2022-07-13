from imutils.perspective import four_point_transform
import cv2


def scan(file_path):
    green = (0, 255, 0)
    image = cv2.imread(file_path)
    orig_image = image.copy()

    # convert the image to gray scale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)  # Add Gaussian blur
    # Apply the Canny algorithm to find the edges
    edged = cv2.Canny(blur, 75, 200)

    contours, _ = cv2.findContours(
        edged, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    contours = sorted(contours, key=cv2.contourArea, reverse=True)

    # go through each contour
    for contour in contours:
        # we approximate the contour
        peri = cv2.arcLength(contour, True)
        approx = cv2.approxPolyDP(contour, 0.05 * peri, True)
        # if we found a countour with 4 points we break the for loop
        # (we can assume that we have found our document)
        if len(approx) == 4:
            doc_cnts = approx
            break

    # We draw the contours on the original image not the modified one
    cv2.drawContours(orig_image, [doc_cnts], -1, green, 3)
    # apply warp perspective to get the top-down view
    warped = four_point_transform(orig_image, doc_cnts.reshape(4, 2))
    # convert the warped image to grayscale
    warped = cv2.cvtColor(warped, cv2.COLOR_BGR2GRAY)
    cv2.destroyAllWindows()
    return warped
