PythonProjects - OpenCv 

###########################################################################################################################################
#**PROJECT - 1**
# 🧠 Face Attendance System | OpenCV + Face Recognition

A Python-based **Face Attendance System** that utilizes real-time webcam input to recognize faces and mark attendance automatically. Built using `OpenCV`, `face_recognition`, and `dlib`, this project logs attendance details with accurate timestamps into a CSV file.

---

## 🚀 Features

- 🔍 **Real-time Face Detection**  
  Uses `face_recognition` for highly accurate face recognition via webcam.

- 🗂️ **Automatic Attendance Logging**  
  Logs names and timestamps into `Attendance.csv` when a face is detected.

- 👥 **Multi-person Support**  
  Easily add new faces to the `Images/` folder for scalable recognition.

---

## 🧰 Libraries Used

| Library             | Purpose                                           |
|---------------------|---------------------------------------------------|
| `numpy`             | For efficient numerical operations.               |
| `opencv-python`     | Accesses webcam and handles image processing.     |
| `face_recognition`  | Performs face detection and matching.             |
| `dlib`              | Provides ML algorithms for face recognition.      |

---

## 📂 Project Structure

faceAttendanceProject/
├── Images/
│   ├── John.jpg
│   └── Jane.jpg
├── faceAttendance.py
└── Attendance.csv (auto-generated)
## ▶️ How to Run the Project

1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/faceAttendanceProject.git
   cd faceAttendanceProject

pip install numpy opencv-python face_recognition dlib
Add Images

Place clear, front-facing images of people in the Images/ folder.

Rename the files with the person's name (e.g., Alice.jpg, Bob.png).

Run the Script


Edit
python faceAttendance.py

##############################################################################################################################################
PROJECT - 2
