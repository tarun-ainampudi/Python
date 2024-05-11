import cv2
import mediapipe as mp
import time

# Initialize Mediapipe Hands module
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()

# OpenCV initialization
cap = cv2.VideoCapture(0)  # You can specify a different video source if needed

# Previous hand position
prev_x, prev_y = 0, 0

# Timestamp for measuring 2-second intervals
start_time = time.time()
no_motion_start_time = time.time()

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Flip the frame horizontally for a later selfie-view display
    frame = cv2.flip(frame, 1)

    # Convert the BGR image to RGB
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Process the image with Mediapipe Hands
    results = hands.process(rgb_frame)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            # Extract x and y coordinates of the hand
            x, y = int(hand_landmarks.landmark[mp_hands.HandLandmark.WRIST].x * frame.shape[1]), \
                   int(hand_landmarks.landmark[mp_hands.HandLandmark.WRIST].y * frame.shape[0])

            # Compare with the previous hand position
            if x > prev_x:
                motion = "Move Right"
            elif x < prev_x:
                motion = "Move Left"
            elif y > prev_y:
                motion = "Move Down"
            elif y < prev_y:
                motion = "Move Up"
            else:
                motion = "No Motion"

            # Update the previous hand position
            prev_x, prev_y = x, y

            # Draw hand landmarks on the frame
            mp.drawing_utils.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

        # Check if 2 seconds have passed
        current_time = time.time()
        if current_time - start_time >= 2:
            print(motion)
            start_time = current_time

        # Check for continuous 3 seconds of no motion
        if motion != "No Motion":
            no_motion_start_time = time.time()

        if current_time - no_motion_start_time >= 3:
            print("No motion detected for 3 seconds. Exiting...")
            break

    cv2.imshow('Hand Motion Detection', frame)

    if cv2.waitKey(1) & 0xFF == 27:  # Press 'Esc' to exit
        break

# Release the capture and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
