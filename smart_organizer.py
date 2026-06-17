# ============================================================
# SECTION 1: Import Modules
# ============================================================
import os      # We import 'os' because it lets us read folders and check file paths.
import shutil  # We import 'shutil' because it provides the tool to physically move files.

# ============================================================
# SECTION 2: Define File Categories (Extension → Folder Map)
# ============================================================
# We use a dictionary to map folder names to a list of file extensions.
# All extensions are lowercase because it makes matching them easier later.
FILE_CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx"],
    "Music": [".mp3", ".wav", ".flac"],
    "Videos": [".mp4", ".mov", ".mkv", ".avi"]
}

# ============================================================
# SECTION 3: Function — find_category(filename)
# Returns which folder a file belongs to
# ============================================================
def find_category(file_name):
    # We convert the file name to lowercase so that '.PNG' correctly matches '.png'.
    lower_name = file_name.lower()
    
    # We loop through each category name and its associated list of extensions.
    for category_name, extensions in FILE_CATEGORIES.items():
        
        # We loop through every extension inside the current category list.
        for ext in extensions:
            
            # We check if our lowercased file name ends with the current extension.
            if lower_name.endswith(ext):
                
                # If it matches, we immediately return the correct category folder name.
                return category_name
                
    # If the loop finishes and no extension matched, we return our fallback folder.
    return "Others"

# ============================================================
# SECTION 4: Function — organize_folder(folder_path)
# Main logic: reads, checks, creates, moves
# ============================================================
def organize_folder(folder_path):
    # We create a tracker variable starting at 0 to count how many files we move.
    moved_count = 0
    
    # We use os.listdir() to get a list of everything inside the target folder.
    # Note: adding a check to ensure folder exists
    if not os.path.exists(folder_path):
        print(f"❌ Error: The folder '{folder_path}' does not exist.")
        return

    all_items = os.listdir(folder_path)
    
    # We start a loop to go through each item (could be a file or a folder) we found.
    for item_name in all_items:
        
        # We use os.path.join() to safely combine the folder path and the item name.
        item_path = os.path.join(folder_path, item_name)
        
        # We check if the item is actually a file because we want to skip moving folders.
        if os.path.isfile(item_path):
            
            # We call our helper function to find out which category folder this file belongs in.
            category_name = find_category(item_name)
            
            # We safely create the full path for the new destination folder.
            category_folder_path = os.path.join(folder_path, category_name)
            
            # We create the category folder if it doesn't exist yet.
            # exist_ok=True is crucial because it prevents the program from crashing if the folder is already there.
            os.makedirs(category_folder_path, exist_ok=True)
            
            # We safely create the full final path where the file will end up.
            new_file_path = os.path.join(category_folder_path, item_name)
            
            # We physically move the file from its old path to the new path.
            shutil.move(item_path, new_file_path)
            
            # We add 1 to our tracker because we successfully organized a file.
            moved_count = moved_count + 1
            
            # We print a friendly message showing exactly what was moved and where.
            print(f"✅ Moved: {item_name: <15} -> {category_name}/")
            
        else:
            # If the item was not a file (it was a folder), we print a warning that we skipped it.
            print(f"⚠️  Skipped: {item_name: <13}/ (it's a folder, not a file)")
            
    # We print a visual separator line for a clean terminal output.
    print("──────────────────────────")
    # We print the final summary showing the total number of files organized.
    print(f"✅ Done! {moved_count} files organized.")

# ============================================================
# SECTION 5: Run The Program
# Ask user for path, call the function
# ============================================================
if __name__ == "__main__":
    # We ask the user to type in the path of the folder they want to organize.
    print("⚠️  WARNING: This script MOVES files (not copies).")
    print("    Always test on a DUMMY folder with fake files first.")
    print("    Never run on: Desktop, Documents, System folders.\n")

    user_folder_path = input("Enter folder path (e.g., TestOrganizer): ")

    # We tell the user the program is starting its work.
    print("📂 Scanning folder...")

    # We call our main function and pass in the folder path the user provided.
    organize_folder(user_folder_path)
