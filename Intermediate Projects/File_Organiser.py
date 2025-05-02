import os
import shutil
from pathlib import Path

def organize_files(directory):
    """
    Organize files in the given directory into subdirectories based on file extensions.
    """
    # Define file type categories and their extensions
    file_types = {
        "Images": [".jpg", ".jpeg", ".png", ".gif", ".svg"],
        "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx", ".csv"],
        "Audio": [".mp3", ".wav", ".aac"],
        "Videos": [".mp4", ".mov", ".avi"],
        "Archives": [".zip", ".rar", ".tar", ".gz"],
        "Code": [".py", ".js", ".html", ".css", ".cpp", ".java"],
    }
    
    # Create directories if they don't exist
    for folder in file_types.keys():
        folder_path = Path(directory) / folder
        folder_path.mkdir(exist_ok=True)
    
    # Create 'Others' folder for uncategorized files
    others_path = Path(directory) / "Others"
    others_path.mkdir(exist_ok=True)
    
    # Organize files
    for item in Path(directory).iterdir():
        if item.is_file() and item.name != "organize.py":  # Skip the script itself
            file_ext = item.suffix.lower()
            moved = False
            
            for folder, extensions in file_types.items():
                if file_ext in extensions:
                    dest = Path(directory) / folder / item.name
                    if not dest.exists():
                        shutil.move(str(item), str(dest))
                    else:
                        # Handle duplicate files by adding a number to the filename
                        counter = 1
                        while True:
                            new_name = f"{item.stem}_{counter}{item.suffix}"
                            dest = Path(directory) / folder / new_name
                            if not dest.exists():
                                shutil.move(str(item), str(dest))
                                break
                            counter += 1
                    moved = True
                    break
            
            if not moved:
                dest = others_path / item.name
                if not dest.exists():
                    shutil.move(str(item), str(dest))
                else:
                    counter = 1
                    while True:
                        new_name = f"{item.stem}_{counter}{item.suffix}"
                        dest = others_path / new_name
                        if not dest.exists():
                            shutil.move(str(item), str(dest))
                            break
                        counter += 1

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1:
        directory = sys.argv[1]
    else:
        directory = input("Enter the directory path to organize: ")
    
    if not Path(directory).exists():
        print("Error: Directory does not exist.")
    else:
        organize_files(directory)
        print("Files organized successfully!")
