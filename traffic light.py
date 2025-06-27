import cv2
import pytesseract
import csv
from tkinter import filedialog, Tk, Button, Label
from ultralytics import YOLO
from datetime import datetime

# Set the path to Tesseract executable (update this path if needed)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Load YOLOv11 model (make sure the model 'best (7).pt' is available in your working directory)
MODEL_PATH = "best (7).pt"
model = YOLO(MODEL_PATH)

# GUI Setup
root = Tk()
root.title("Traffic Light Violation Detection")
root.geometry("300x200")

label = Label(root, text="Select Image or Video for Detection", font=("Arial", 12))
label.pack(pady=10)

# OCR Function to extract text from vehicle number plate
def extract_plate_text(cropped_img):
    gray = cv2.cvtColor(cropped_img, cv2.COLOR_BGR2GRAY)
    text = pytesseract.image_to_string(gray, config='--psm 7')
    return text.strip()

# Image Detection and OCR to CSV
def detect_image():
    file_path = filedialog.askopenfilename(title="Select Image", filetypes=[("Image Files", "*.jpg *.png *.jpeg")])
    if not file_path:
        return

    results = model(file_path)
    img = cv2.imread(file_path)

    with open("number_plate_text_image.csv", mode="w", newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Class", "Detected Number", "Confidence", "X", "Y", "Width", "Height"])

        for r in results:
            for box in r.boxes:
                cls_id = int(box.cls[0])
                cls_name = r.names[cls_id]

                # Check if the detected object is a vehicle number plate
                if "plate" in cls_name.lower():  # Adjust based on how 'plate' is labeled in the model
                    conf = float(box.conf[0])
                    x1, y1, x2, y2 = map(int, box.xyxy[0])
                    crop = img[y1:y2, x1:x2]  # Crop the number plate area
                    text = extract_plate_text(crop)  # Use OCR to read the plate number
                    width = x2 - x1
                    height = y2 - y1
                    writer.writerow([cls_name, text, f"{conf:.2f}", x1, y1, width, height])

    results[0].save(filename="output_image.jpg")
    cv2.imshow("Detection Result", cv2.imread("output_image.jpg"))
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    print("✅ Vehicle number plate texts saved to: number_plate_text_image.csv")

# Video Detection and OCR to CSV
def detect_video():
    file_path = filedialog.askopenfilename(title="Select Video", filetypes=[("Video Files", "*.mp4 *.avi *.mov")])
    if not file_path:
        return

    cap = cv2.VideoCapture(file_path)
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = int(cap.get(cv2.CAP_PROP_FPS))

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_path = f"output_detected_{timestamp}.mp4"
    csv_path = f"number_plate_detections_video_{timestamp}.csv"

    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

    csv_file = open(csv_path, mode="w", newline='')
    writer = csv.writer(csv_file)
    writer.writerow(["Frame", "Class", "Detected Number", "Confidence", "X", "Y", "Width", "Height"])

    frame_count = 0
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        results = model(frame)
        annotated_frame = results[0].plot()
        out.write(annotated_frame)

        for r in results:
            for box in r.boxes:
                cls_id = int(box.cls[0])
                cls_name = r.names[cls_id]

                if "plate" in cls_name.lower():  # Only process number plates
                    conf = float(box.conf[0])
                    x1, y1, x2, y2 = map(int, box.xyxy[0])
                    crop = frame[y1:y2, x1:x2]  # Crop number plate region
                    text = extract_plate_text(crop)  # OCR to read number plate text
                    width = x2 - x1
                    height = y2 - y1
                    writer.writerow([frame_count, cls_name, text, f"{conf:.2f}", x1, y1, width, height])

        frame_count += 1
        cv2.imshow("Detection - Press Q to Quit", annotated_frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    out.release()
    csv_file.close()
    cv2.destroyAllWindows()
    print(f"✅ Video output saved to: {output_path}")
    print(f"✅ Vehicle number plate detections saved to: {csv_path}")

# GUI Buttons for image and video detection
btn1 = Button(root, text="Detect on Image", command=detect_image, width=20)
btn1.pack(pady=10)

btn2 = Button(root, text="Detect on Video", command=detect_video, width=20)
btn2.pack(pady=10)

# Run the GUI
root.mainloop()
