import cv2
import numpy as np
import os
import pytesseract
import webbrowser
import subprocess
import pyttsx3
import time

# ✅ Path to your Tesseract installation
pytesseract.pytesseract.tesseract_cmd = r"C:/Program Files/Tesseract-OCR/tesseract.exe"

# ---------- Speech feedback ----------
tts = pyttsx3.init()
def speak(text):
    try:
        tts.say(text)
        tts.runAndWait()
    except Exception:
        pass

# ---------- App mapping ----------
APP_MAP = {
    'A': {'type': 'url', 'cmd': 'https://agentgpt.reworkd.ai/'},
    'B': {'type': 'url', 'cmd': 'https://www.browse.ai/'},
    'C': {'type': 'url', 'cmd': 'https://chatgpt.com'},
    'D': {'type': 'url', 'cmd': 'https://durable.co/'},
    'E': {'type': 'url', 'cmd': 'https://app.formulabot.com/excel-ai'},
    'F': {'type': 'url', 'cmd': 'https://www.fathom.ai/'},
    'G': {'type': 'url', 'cmd': 'https://github.com/login'},
    'H': {'type': 'url', 'cmd': 'https://www.hypotenuse.ai/'},
    'I': {'type': 'url', 'cmd': 'https://www.ibm.com/products/watsonx-ai'},
    'J': {'type': 'url', 'cmd': 'https://jupyter.org/try'},
    'K': {'type': 'url', 'cmd': 'https://www.kaggle.com/'},
    'L': {'type': 'url', 'cmd': 'https://www.looria.com/'},
    'M': {'type': 'url', 'cmd': 'https://www.make.com/en/register'},
    'N': {'type': 'url', 'cmd': 'https://www.notion.com/product/ai'},
    'O': {'type': 'url', 'cmd': 'https://obsidian.md/'},
    'P': {'type': 'url', 'cmd': 'https://www.perplexity.ai/'},
    'Q': {'type': 'url', 'cmd': 'https://www.quora.com'},
    'R': {'type': 'url', 'cmd': 'https://replit.com/learn/intro-to-ghostwriter'},
    'S': {'type': 'url', 'cmd': 'https://stablediffusionweb.com/'},
    'T': {'type': 'url', 'cmd': 'https://www.taskade.com/'},
    'U': {'type': 'url', 'cmd': 'https://uizard.io/'},
    'V': {'type': 'url', 'cmd': 'https://vercel.com/ai'},
    'W': {'type': 'url', 'cmd': 'https://whisperai.com/'},
    'X': {'type': 'url', 'cmd': 'https://xmind.com/ai'},
    'Y': {'type': 'url', 'cmd': 'https://www.youtube.com'},
    'Z': {'type': 'url', 'cmd': 'https://easywithai.com/ai-website-builders/zyro-website-builder/'}
}

# ---------- Launch function ----------
def open_app_for_letter(letter):
    letter = letter.upper()
    if letter not in APP_MAP:
        speak(f"No mapping for {letter}")
        print(f"[Launcher] No mapping for {letter}")
        return
    mapping = APP_MAP[letter]
    cmd_type = mapping['type']
    cmd = os.path.expandvars(mapping['cmd'])
    try:
        if cmd_type == 'url':
            webbrowser.open(cmd)
        elif cmd_type == 'exe':
            os.startfile(cmd)
        elif cmd_type == 'cmd':
            subprocess.Popen(cmd, shell=True)
        speak(f"Opening {letter}")
        print(f"[Launcher] Launched {letter}: {cmd}")
    except Exception as e:
        print("[Launcher] Failed to open:", e)
        speak("Failed to open application")

# ---------- Whiteboard Drawing ----------
def draw_whiteboard():
    board = np.ones((400, 400, 3), np.uint8) * 255
    drawing = False
    ix, iy = -1, -1

    def draw(event, x, y, flags, param):
        nonlocal drawing, ix, iy
        if event == cv2.EVENT_LBUTTONDOWN:
            drawing = True
            ix, iy = x, y
        elif event == cv2.EVENT_MOUSEMOVE and drawing:
            cv2.line(board, (ix, iy), (x, y), (0, 0, 0), 8)
            ix, iy = x, y
        elif event == cv2.EVENT_LBUTTONUP:
            drawing = False
            cv2.line(board, (ix, iy), (x, y), (0, 0, 0), 8)

    cv2.namedWindow("Whiteboard")
    cv2.setMouseCallback("Whiteboard", draw)
    return board

# ---------- OCR recognition ----------
def recognize_letter(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = cv2.bitwise_not(gray)
    _, thresh = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)
    config = '--psm 10 -c tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    text = pytesseract.image_to_string(thresh, config=config).strip()
    if text:
        return text[0].upper()
    return None

# ---------- Main ----------
def main():
    print("🧩 Draw a letter on the whiteboard.")
    print("🔍 Press 'r' to recognize and open the mapped app.")
    print("🧹 Press 'c' to clear.")
    print("❌ Press 'q' to quit.\n")

    board = draw_whiteboard()
    while True:
        cv2.imshow("Whiteboard", board)
        key = cv2.waitKey(1) & 0xFF

        if key == ord('r'):
            print("\n🔍 Recognizing letter...")
            letter = recognize_letter(board)
            if letter:
                print(f"✅ Detected: {letter}")
                open_app_for_letter(letter)
            else:
                print("⚠️ Could not detect a clear letter.")

        elif key == ord('c'):
            board[:] = 255
            print("🧹 Cleared whiteboard.")

        elif key == ord('q'):
            print("👋 Exiting...")
            break

    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
