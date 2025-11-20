# 🧠 AI Handwritten Letter App Launcher  
### Draw a letter → OCR detects it → Opens mapped apps automatically!

This project uses **OpenCV**, **Tesseract OCR**, **NumPy**, and **Python automation** to detect a handwritten letter on a whiteboard canvas and automatically open a mapped website or application based on that letter.

---

## 🚀 Features

- ✏️ Draw any letter (A–Z) on a digital whiteboard  
- 🔍 OCR automatically detects the handwritten letter  
- 🌐 Opens corresponding websites  
- 🔊 Voice feedback using pyttsx3  
- 🧹 Clear board, recognize again, or quit with keyboard shortcuts  

---

## 🖥️ How It Works

1. A 400×400 whiteboard opens.  
2. You draw any uppercase or lowercase letter using the mouse.  
3. Press **`r`** → OCR recognizes the letter.  
4. The program checks the **APP_MAP** and opens the mapped URL.  
5. Press **`c`** to clear the whiteboard.  
6. Press **`q`** to exit.  

---

## ⌨️ Controls

| Key | Action |
|-----|--------|
| **r** | Recognize letter & open mapped app |
| **c** | Clear drawing board |
| **q** | Quit |

---

## 📦 Installation

### **1️⃣ Clone the repository**

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
# smart-whiteboard-launcher
