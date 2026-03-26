import cv2
import tkinter as tk
from datetime import datetime
import os

# -------------------------
# Login System
# -------------------------
def validate_user(username, password):
    """Check if username/password exists in users.txt"""
    if not os.path.exists("users.txt"):
        return False

    with open("users.txt") as f:
        for line in f:
            u, p = line.strip().split(",")
            if u == username and p == password:
                return True
    return False


def login():
    """Simple login GUI"""
    user = ""

    def submit():
        nonlocal user
        u = user_entry.get().strip()
        p = pass_entry.get().strip()

        if validate_user(u, p):
            user = u
            root.destroy()
        else:
            error_label.config(text="Invalid credentials")

    root = tk.Tk()
    root.title("Login")
    root.geometry("300x200")

    tk.Label(root, text="Username").pack()
    user_entry = tk.Entry(root)
    user_entry.pack()

    tk.Label(root, text="Password").pack()
    pass_entry = tk.Entry(root, show="*")
    pass_entry.pack()

    error_label = tk.Label(root, text="", fg="red")
    error_label.pack()

    tk.Button(root, text="Login", command=submit).pack(pady=10)

    root.mainloop()
    return user


# -------------------------
# Attendance System
# -------------------------
def already_recorded(name):
    """Check if user already recorded today"""
    if not os.path.exists("attendance.csv"):
        return False

    today = datetime.now().strftime("%Y-%m-%d")

    with open("attendance.csv") as f:
        for line in f:
            parts = line.strip().split(",")

            if len(parts) == 3:
                n, date, _ = parts
                if n == name and date == today:
                    return True
    return False


def mark_attendance(name):
    """Save attendance with date + time"""
    with open("attendance.csv", "a") as f:
        date = datetime.now().strftime("%Y-%m-%d")
        time = datetime.now().strftime("%H:%M:%S")
        f.write(f"{name},{date},{time}\n")


def save_image(frame, name):
    """Save image in user-specific folder"""
    folder = f"captures/{name}"

    if not os.path.exists(folder):
        os.makedirs(folder)

    filename = f"{folder}/{datetime.now().strftime('%H%M%S')}.jpg"
    cv2.imwrite(filename, frame)


# -------------------------
# Dashboard
# -------------------------
def show_dashboard():
    """Display attendance records"""
    if not os.path.exists("attendance.csv"):
        return

    root = tk.Tk()
    root.title("Attendance Dashboard")
    root.geometry("400x300")

    text = tk.Text(root)
    text.pack(fill="both", expand=True)

    with open("attendance.csv") as f:
        text.insert("end", f.read())

    root.mainloop()


# -------------------------
# Camera System
# -------------------------
def run_system(name):
    """Main camera + detection loop"""
    cap = cv2.VideoCapture(0)

    face_cascade = cv2.CascadeClassifier(
        cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
    )

    recorded = False
    status = ""

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Mirror effect
        frame = cv2.flip(frame, 1)

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        # Draw face box
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

        # Attendance logic
        if len(faces) > 0 and not recorded:
            if already_recorded(name):
                status = "Already Checked Today"
            else:
                mark_attendance(name)
                save_image(frame, name)
                status = "Attendance Saved"

            recorded = True

        # UI Display
        cv2.putText(frame, f"User: {name}", (20, 40),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 0), 2)

        cv2.putText(frame, f"Status: {status}", (20, 80),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 255), 2)

        cv2.putText(frame, f"People: {len(faces)}", (20, 120),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

        cv2.putText(frame, "Press ESC to Exit | Press R to Reset", (20, 160),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (200, 200, 200), 1)

        cv2.imshow("Smart Attendance System", frame)

        # Controls
        key = cv2.waitKey(1)

        if key == 27:  # ESC
            break
        elif key == ord('r'):  # Reset
            recorded = False
            status = "Reset Done"

    cap.release()
    cv2.destroyAllWindows()


# -------------------------
# Main App
# -------------------------
def main():
    user = login()

    if user:
        run_system(user)
        show_dashboard()


if __name__ == "__main__":
    main()