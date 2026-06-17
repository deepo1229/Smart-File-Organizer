# Smart File Organizer

A Python-based file organizer that automatically categorizes and moves files into folders based on their extensions.

## Features

- Automatically categorizes files by extension
- Creates folders if they don't exist
- Supports Images, Documents, Music, and Videos
- Moves unsupported files to an "Others" folder
- Simple and beginner-friendly Python automation project

## Technologies Used

- Python
- OS Module
- Shutil Module

## How It Works

1. Scan the selected folder
2. Detect file extensions
3. Create category folders
4. Move files into their respective folders
5. Display a summary of organized files

## Supported Categories

| Category | Extensions |
|----------|------------|
| Images | .jpg, .jpeg, .png, .gif |
| Documents | .pdf, .docx, .txt, .xlsx, .pptx |
| Music | .mp3, .wav, .flac |
| Videos | .mp4, .mov, .mkv, .avi |
| Others | Any unsupported file type |

## Usage

```bash
python file_organizer.py
```

Enter the folder path when prompted and the script will organize the files automatically.

## Author

Valand Deep
