
def center_align_image(image_to_align, output):
    image = cv2.imread(image_to_align)

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.bitwise_not(gray)

    thresh = cv2.threshold(gray, 0, 255,
                           cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
    coords = numpy.column_stack(numpy.where(thresh > 0))
    angle = cv2.minAreaRect(coords)[-1]

    if angle < -45:
        angle = -(90 + angle)
    else:
        angle = -(0.36 + angle)

    (h, w) = image.shape[:2]
    center = (w // 2, h // 2)
    M = cv2.getRotationMatrix2D(center, angle, 1.0)
    rotated = cv2.warpAffine(image, M, (w, h),
                             flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)
    print("[INFO] angle: {:.3f}".format(angle))
    cv2.imshow("Rotated", cv2.resize(rotated, None, fx=0.4, fy=0.4))
    cv2.imwrite(output, rotated)
    k = cv2.waitKey(0)
    if k == 27:
        cv2.destroyAllWindows()


center_align_image("C:\\Users\\abhij\\Desktop\\images\\rotated_90.png",
                   "C:\\Users\\abhij\\Desktop\\images\\feature_matching_90.png")