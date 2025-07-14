🔐 File Integrity Checker

A simple Python script to monitor changes in files by calculating and comparing SHA-256 hash values.  
Built as part of my internship at **Codetech IT Solutions** 🧑‍💻.

---
📁 Project Structure

```
file_checker/
├── checker.py        # Main Python script
├── README.md         # Project instructions
└── (Create your own 'my_files' folder with sample files)
---
🚀 How to Use

1. **Create a folder** named `my_files` in the same directory as `checker.py`.
2. Add any `.txt` or other files you want to monitor inside that folder.
3. Open Command Prompt or terminal.
4. Navigate to the script folder and run:

```bash
python checker.py
```

✅ What Happens:

- On first run:  
  Saves a **baseline** of file hashes in `hashes.json`.
- On next runs:  
  Compares current files with the baseline and shows:

```
⚠️ Modified file: test1.txt
❌ Deleted file: test2.txt
🆕 New file added: notes.txt
```

---

🛠 Technologies Used

- **Language**: Python 3.10+
- **Libraries**:  
  - `os` – for file and folder operations  
  - `hashlib` – to generate SHA-256 hashes  
  - `json` – to store and load baseline data

---

📌 Features

- Detects **file modifications**, **deletions**, and **new files**
- Lightweight and beginner-friendly
- Easily extendable for folders, logs, or other file types

---

🙋‍♀️ Author

Shivani Sree  
Intern @ Codetech IT Solutions  
GitHub: [github.com/shivanisree7425](https://github.com/shivanisree7425)  
Feel free to connect and explore more!

---

📄 License

This project is open-source and free to use for learning or development purposes.
