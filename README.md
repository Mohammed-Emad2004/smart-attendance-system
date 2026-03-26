# 🎯 Smart Attendance System

A real-time smart attendance system built using Python and OpenCV.
The system detects human faces through a webcam and automatically records attendance with time and user identification.

---

## 🚀 Features

* Real-time face detection using OpenCV
* Simple login system for user authentication
* Automatic attendance recording with timestamp
* Prevents duplicate attendance within a short period (cooldown system)
* Displays number of detected people in real-time
* Saves attendance records in a CSV file
* Auto-creates required files if not found
* Clean and simple interface

---

## 🛠️ Technologies Used

* Python
* OpenCV
* CSV (for data storage)
* OS & Datetime modules

---

## 📦 Installation

Clone the repository:

```bash
git clone https://github.com/Mohammed-Emad2004/smart-attendance-system.git
cd smart-attendance-system
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ How to Run

```bash
python main.py
```

---

## 🎮 Controls

* Press **Q** → Exit the application
* Press **R** → Reset attendance

---

## 📁 Project Structure

```text
main.py              # Main application
requirements.txt     # Dependencies
users.txt            # User login data
attendance.csv       # Attendance records
screenshot.png       # Project preview
```

---

## 📸 Preview

![App Screenshot](screenshot.png)

---

## ⚠️ Notes

* The system detects faces (not full recognition of identities)
* Attendance is marked once per session unless reset
* Make sure your camera is working before running the project

---

## 👨‍💻 Author

Mohammed Emad

---

## ⭐ If you like the project, don't forget to star the repo!
