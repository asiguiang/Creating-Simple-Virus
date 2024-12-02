# Creating-Simple-Virus

This Python script combines system commands, GUI pop-ups, and web interactions to simulate malicious behavior. Below is a detailed explanation of the code and its technical documentation:

---

### **Code Explanation**

1. **Imports**:
   - **`webbrowser`**: Used to open a web page in the default web browser.
   - **`os`**: Provides a way to interact with the operating system for task and process management.
   - **`platform`**: Determines the current operating system.
   - **`ctypes`**: Enables low-level Windows system calls (not explicitly used here but potentially for further malicious behavior).
   - **`tkinter`**: Creates GUI elements, specifically the pop-up message.

2. **Functions**:
   - **`close_other_browsers()`**:
     - Detects the operating system using `platform.system()`.
     - On Windows:
       - Uses `taskkill` to terminate browsers: Chrome, Firefox, and Edge.
     - On Linux:
       - Uses `pkill` to terminate browser processes.
     - On macOS (Darwin):
       - Uses `pkill` to terminate Safari processes.
     - **Effect**: Disrupts user browsing activity.
   - **`show_popup()`**:
     - Creates a pop-up window using `tkinter`.
     - Displays a threatening message ("YOU HAVE BEEN HACKED, 36 HOURS LEFT! BUY NOW!") in a dialog box.
   - **`open_pup_website()`**:
     - Opens a provided URL in the default browser using `webbrowser.open()`.
     - URL is a link to a supposed antivirus purchase page.

3. **Main Functionality**:
   - Executes the functions sequentially:
     1. Closes browser processes.
     2. Opens the specified website.
     3. Shows the threatening pop-up.

4. **Purpose**:
   - The script simulates ransomware-like behavior by disrupting browsing, coercing a purchase, and presenting an alarming message. It may be designed to force users into purchasing a product or falling victim to a scam.

---

### **Technical Documentation**

#### **1. Overview**
This script is an educational example of how Python can be used for potentially malicious purposes, like disrupting system activity, displaying warnings, and opening URLs. It demonstrates methods to:
- Interact with system processes.
- Create pop-ups with urgent messages.
- Open web links automatically.

#### **2. Dependencies**
- Python 3.x
- Libraries: `webbrowser`, `os`, `platform`, `ctypes`, `tkinter`

#### **3. Functions**

| Function               | Description                                                                                      |
|------------------------|--------------------------------------------------------------------------------------------------|
| `close_other_browsers` | Closes active browser processes based on the operating system.                                   |
| `show_popup`           | Displays a pop-up dialog box with a message using `tkinter`.                                     |
| `open_website`     | Opens a specific URL in the user's default web browser using `webbrowser.open()`.                |

#### **4. Platforms Supported**
- **Windows**
- **Linux**
- **macOS (Darwin)**

#### **5. Security Concerns**
- **Disruption**: Terminates browser processes, which can result in loss of unsaved data.
- **Psychological Impact**: Displays a fear-inducing pop-up.
- **Coercion**: Opens a webpage that might attempt to scam the user.

#### **6. Execution Flow**
1. `close_other_browsers()`:
   - Detect the operating system.
   - Close browser processes.
2. `open_pup_website()`:
   - Open the specified URL.
3. `show_popup()`:
   - Display the threatening message.

#### **7. Legal and Ethical Use**
This script is provided for educational purposes only and should not be used to harm systems or coerce individuals. Misuse of this code could result in legal consequences.

#### **8. Improvements for Educational Value**
- Replace malicious elements with benign actions to teach functionality safely.
  - Example: Use a harmless pop-up message like "System Check Complete."
  - Redirect to a safe webpage instead of a suspicious link.
  - Demonstrate proper browser process handling for managing application resources.

---

### **Disclaimer**
The script simulates malicious activity and should only be used in a controlled environment for learning purposes. Any unauthorized use on third-party systems is unethical and potentially illegal.
