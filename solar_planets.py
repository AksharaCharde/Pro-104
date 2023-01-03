import cv2

#Loading the Image
img = cv2.imread("solar-system.jpg")

cv2.putText(img,
            "Sun",
            (100, 90),
            cv2.FONT_HERSHEY_DUPLEX,
            2,
            (0, 0, 255)
            )

cv2.putText(img,
            "Mercury",
            (120, 180),
            cv2.FONT_HERSHEY_DUPLEX,
            0.5,
            (255, 255, 255)
            )

cv2.putText(img, 
            "Venus",
            (190, 170),
            cv2.FONT_HERSHEY_DUPLEX,
            0.5,
            (255, 255, 255)
            )

cv2.putText(img,
            "Earth",
            (285, 160),
            cv2.FONT_HERSHEY_DUPLEX,
            0.5,
            (255, 255,255)
            )

cv2.putText(img,
            "Mars",
            (385, 160),
            cv2.FONT_HERSHEY_DUPLEX,
            0.5,
            (255, 255,255)
            )

cv2.putText(img,
            "Jupiter",
            (450, 100),
            cv2.FONT_HERSHEY_DUPLEX,
            0.5,
            (255, 255, 255)
            )

cv2.putText(img,
            "Saturn",
            (800, 140),
            cv2.FONT_HERSHEY_DUPLEX,
            0.5,
            (255, 255, 255)
            )

cv2.putText(img,
            "Uranus",
            (965, 140),
            cv2.FONT_HERSHEY_DUPLEX,
            0.5,
            (255, 255, 255)
            )

cv2.putText(img,
            "Neptune",
            (1110, 140),
            cv2.FONT_HERSHEY_DUPLEX,
            0.5,
            (255, 255, 255)
            )

#Displaying the Image
cv2.imshow("Solar System", img)

cv2.waitKey(0)