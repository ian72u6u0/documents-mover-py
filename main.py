from pathlib import Path
import os
import shutil

folder_name = "pyoslib"
downloads_dir = Path.home() / "Downloads"
documents_dir = Path.home() / "Desktop" / "Documents"
curr_dir = os.getcwd()

documents_dir.mkdir(parents=True, exist_ok=True)

for root, dirs, files in os.walk(downloads_dir):
    for file in files:
        if file.endswith(".pdf"):
            src_file = os.path.join(root, file)
            if os.path.exists(src_file):
                try:
                    shutil.move(src_file, documents_dir)
                    print(f"Moved: {file}")
                except shutil.Error as e:
                    print(f"Skipped {file} (File might already exist in destination)")
