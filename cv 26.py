
import cv2

video = cv2.VideoCapture("C:/Users/krith/Downloads/vedio.cv PM.mp4")
frames = []

# Read all frames
while True:
    ret, frame = video.read()
    if not ret:
        break
    frames.append(frame)

video.release()

if not frames:
    print("Video not found or empty")
else:
    frames.reverse()
    height, width, layers = frames[0].shape

    # Create reversed video
    output = cv2.VideoWriter(
        "reverse_video.mp4",
        cv2.VideoWriter_fourcc(*"mp4v"),
        30, (width, height)
    )

    for frame in frames:
        output.write(frame)

    output.release()

    # Play reversed video
    cap = cv2.VideoCapture("reverse_video.mp4")

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        cv2.imshow("Reverse Video", frame)

        if cv2.waitKey(30) & 0xFF == 27:
            break

    cap.release()
    cv2.destroyAllWindows()
