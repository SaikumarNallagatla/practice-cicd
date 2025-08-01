import zipfile

files_to_zip = ["main.py", "requirements.txt", "test_main.py"]

with zipfile.ZipFile("app.zip", "w") as zipf:
    for file in files_to_zip:
        zipf.write(file)
