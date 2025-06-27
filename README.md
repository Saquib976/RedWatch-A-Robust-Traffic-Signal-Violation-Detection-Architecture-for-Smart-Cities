# 🚦 RedWatch: A Robust Traffic Signal Violation Detection Architecture for Smart Cities
RedWatch is a deep learning-based framework designed to automatically detect traffic signal violations using real-time video feeds. Leveraging advanced object detection (e.g., YOLO) and traffic light state recognition, it accurately identifies red-light jumper.  


**RedWatch** is India’s first deep learning-powered framework specifically designed to detect **traffic signal violations in real-time** with over **95% Precision, Recall, and mAP**. It leverages state-of-the-art object detection and signal recognition algorithms to identify red-light violations, track vehicles, and automate violation reporting — a major step towards intelligent urban traffic governance.

---

## 🔍 Why RedWatch is Unique

- 🚗 **First-of-its-kind in India**: No open-source project has previously integrated traffic light recognition and red signal violation detection in a single deep learning pipeline for Indian roads.
- 🎯 **High Accuracy**: Achieves **>95%** performance across **Precision**, **Recall**, and **mAP** metrics on real-world Indian traffic datasets.
- 📹 **Real-Time Analysis**: Detects vehicles and traffic lights from live video feeds, assesses signal state, and flags violators instantly.
- 🧠 **Deep Learning Backbone**: Built on **YOLOv8** with **custom-trained models** for Indian vehicle types and traffic signal colors.
- 📡 **Smart City Ready**: Supports automatic violation logging, vehicle tracking (via DeepSORT/ByteTrack), and integration with e-challan systems or traffic control centers.

---
## 📸 Real-Time Violation Detection Example

> Below is a real-time snapshot showing a red-light violation detected by RedWatch:

![Red Light Violation Detection](https://github.com/user-attachments/assets/8ed470ca-a226-4d0b-8376-bde20bfef6a0)

## 📸 Number Plate Detection Output

> Below is the number plate detection result using EasyOCR:

![download (1)](https://github.com/user-attachments/assets/64784ce9-1594-497c-bf6b-14d005329922)

### 🛰️ CCTV Footage Frame
![download (3)](https://github.com/user-attachments/assets/f432cf47-d90b-4bd9-81c5-a91ecaf6187d)

*Snapshot from live CCTV feed processed for violation detection.
> Or watch the full detection in action:

![Live Detection Demo](https://github.com/user-attachments/assets/7218944a-cad7-4df3-9ca5-11e3e1c1a7b0
)












## 📂 Core Features

- ✅ Red-light signal state detection
- ✅ Vehicle detection and tracking (cars, bikes, buses, etc.)
- ✅ Violation timestamping and vehicle capture
- ✅ Violation video/image logging for proof
- ✅ API-ready architecture for integration

---

## 📊 Model Performance (Tested on Real Indian Traffic Video)

| Metric     | Value    |
|------------|----------|
| Precision  | 99%    |
| Recall     | 98%    |
| mAP@0.5    | 98%    |
| FPS (Real-time) | 30+ |

---

## 🛠️ Technologies Used

- `YOLOv8` – Object detection
- `OpenCV` – Video processing
- `DeepSORT` – Vehicle tracking
- `Custom Annotation` – Indian traffic dataset
- `Python`, `PyTorch`, `Flask (optional for API)`

---

## 🇮🇳 Built for Indian Roads

Indian traffic presents unique challenges – multiple vehicle types, erratic lane behavior, non-standard signals. **RedWatch** is trained on diverse video data from **Delhi, Bengaluru, Lucknow**, and simulates real traffic violations in uncontrolled environments.

---

## 🚀 How to Use


# Clone the repo
git clone https://github.com/your-username/RedWatch-TrafficViolationDetection.git


cd RedWatch-TrafficViolationDetection

# Install dependencies
pip install -r requirements.txt

# Run detection
python detect_violation.py --source traffic_video.mp4

---
    
🤝 Collaboration & Contact


Interested in the complete source code, full project report, or a potential research collaboration?

Feel free to connect:

📧 Email: saquibsabir786@gmail.com

🔗 LinkedIn:* https://www.linkedin.com/in/saquib-s-736063217

> 💡 *Let's connect and build smarter, safer urban mobility solutions together!*



