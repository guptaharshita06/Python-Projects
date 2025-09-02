import pyautogui
import time
import pyperclip

# Small delay to give you time to switch to the screen
time.sleep(2)

# Step 1: Click on the icon
pyautogui.click(1430, 1053)
time.sleep(1)

# Step 2: Drag to select text
pyautogui.moveTo(1361, 157)
pyautogui.dragTo(1883, 652, duration=1, button='left')
time.sleep(1)

# Step 3: Copy (CTRL+C)
pyautogui.hotkey('ctrl', 'c')
time.sleep(0.5)

# Step 4: Get text from clipboard
text = pyperclip.paste()

print("Extracted Text:")
print(text)
