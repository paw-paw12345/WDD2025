import cv2
import face_recognition
import pyttsx3

def speak(message):
    """Speak a message using pyttsx3"""
    engine = pyttsx3.init()
    engine.say(message)
    engine.runAndWait()

def load_owner_encoding(image_path):
    """Load and encode the authorized face"""
    image = face_recognition.load_image_file(image_path)
    encodings = face_recognition.face_encodings(image)
    if not encodings:
        raise ValueError("No face found in the loaded image.")
    return encodings[0]

def recognize_face(owner_encoding):
    """Start webcam, detect face, and compare to owner"""
    cap = cv2.VideoCapture(0)

    print("Starting camera. Press 'q' to quit.")
    access_granted = False

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to read from camera.")
            break

        # Resize frame for faster processing
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
        rgb_small_frame = small_frame[:, :, ::-1]

        # Detect face locations and encodings
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

        for face_encoding in face_encodings:
            matches = face_recognition.compare_faces([owner_encoding], face_encoding)
            if True in matches:
                print("[✔] Access granted!")
                speak("Welcome home. Access granted.")
                access_granted = True
                break
            else:
                print("[✘] Intruder alert!")
                speak("Intruder alert. Access denied.")
                access_granted = False
                break

        # Show the video feed
        cv2.imshow("Security Camera", frame)

        # Exit conditions
        if access_granted:
            break
        if cv2.waitKey(1) & 0xFF == ord('q'):
            print("Quitting...")
            break

    cap.release()
    cv2.destroyAllWindows()

# === MAIN ===
if __name__ == "__main__":
    try:
        owner_face = load_owner_encoding("owner.jpg")  # Load your saved face
        recognize_face(owner_face)
    except Exception as e:
        print("Error:", str(e))
        speak("Error with the security system.")
