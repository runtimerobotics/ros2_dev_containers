import cv2

def main():
    # Open default webcam
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Cannot open camera")
        return

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Can't receive frame (stream end?). Exiting ...")
            break

        # Convert to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Draw a rectangle
        cv2.rectangle(gray, (50, 50), (250, 250), (0, 0, 0), 2)

        # Put some text
        cv2.putText(gray, 'OpenCV Test', (60, 45), cv2.FONT_HERSHEY_SIMPLEX,
                    0.8, (255, 255, 255), 2)

        # Display the resulting frame
        cv2.imshow('Webcam Grayscale', gray)

        if cv2.waitKey(1) == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
