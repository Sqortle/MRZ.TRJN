# Educational Reverse Shell with File Transfer

> ⚠️ This project is for **educational and ethical research purposes only**.  
> Do not deploy or use this code on any system you do not own or have explicit permission to test.  
> The author does **not take responsibility for any misuse** of the code.

## 📚 Description

This is a Python-based client-server application that simulates a basic reverse shell communication over TCP, including file upload/download capability.

- The **Listener** acts as a command-and-control server.
- The **Trojan** connects back to the Listener and executes received commands.
- Supports:
  - Shell command execution
  - File upload & download (Base64 encoded)
  - Changing directories
  - Basic persistence (Windows only, using the registry)

This is a **learning tool** for understanding socket programming, basic command execution, and data encoding over network connections.

---
 
## 🚀 How It Works

1. The **Listener** listens on a specified IP and port.
2. The **Trojan** connects to the Listener.
3. The Listener sends commands; the Trojan processes and returns output.
4. Optional: persistence mechanism using Windows registry (`settle` command).

**All communication is JSON-formatted and encoded using UTF-8.**

---

## 🛠️ Requirements

- Python 3.x
- `simplejson` package (`pip install simplejson`)

---

## 🔧 Setup and Usage

### 1. Install dependencies:

```bash
pip install simplejson
```

### 2. Start the Listener:

```bash
python listener.py
```

By default, it uses `127.0.0.1:8080`. You can change the IP and port inside the script.

### 3. Run the Trojan:

On the **same machine** or another machine in the same LAN:

```bash
python trojan.py
```

---

## 💻 Supported Commands

| Command       | Description                                           |
|---------------|-------------------------------------------------------|
| `exit`        | Terminates the connection                             |
| `cd <path>`   | Changes directory on the Trojan side                  |
| `upload <path>` | Uploads a file from Listener to the Trojan          |
| `download <path>` | Downloads a file from the Trojan to the Listener  |
| `settle <reg_name> <filename>` | Adds Trojan to Windows startup       |
| Any shell command | Executes it on the Trojan's system (e.g., `dir`) |

---

## 📁 File Transfer Notes

- File contents are base64 encoded during transfer.
- Make sure the file path is correct and accessible.
- Downloaded files will be saved to the same directory as `listener.py`.

---

## 🔐 Ethical Considerations & Disclaimer

This project **must not** be used for unauthorized access or real-world exploitation. It is strictly intended to:

- Learn how client-server communication works in Python.
- Understand reverse shell concepts in a controlled environment.
- Study basic Windows persistence for cybersecurity awareness.

By using this code, **you agree** to take full responsibility for any actions involving it. Use it **only in test environments** or with permission.

---

## 📌 Important Notes

- This tool does **not** provide encryption — all data is sent in plain text.
- Tested on localhost. For LAN testing, you must:
  - Replace `127.0.0.1` with your machine’s actual IP.
  - Ensure firewall or antivirus does not block the connection.
- Windows registry edits via `settle` work only if the script is compiled as `.exe` (e.g., with PyInstaller).

---

## 📎 License

This project is released under the [MIT License](LICENSE).
