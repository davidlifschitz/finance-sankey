from pathlib import Path

def prefix_filenames_pathlib(directory_path, prefix="capitalone_"):
    """
    Adds a specified prefix to the beginning of every file 
    (not directories) in the given directory path using pathlib.
    
    Args:
        directory_path (str or Path): The path to the target directory.
        prefix (str): The prefix string to add (default is "capitalone_").
    """
    
    # 1. Convert the input string path to a Path object
    target_dir = Path(directory_path)

    # 2. Check if the directory exists
    if not target_dir.is_dir():
        print(f"Error: Directory not found or is not a directory: {target_dir}")
        return

    print(f"--- Renaming files in: {target_dir.resolve()} ---")
    
    # 3. Iterate over all entries in the directory
    # Use glob('*') and filter with is_file() to target only files
    for old_path in target_dir.iterdir():
        if old_path.is_file():
            
            # Construct the new filename using the Path object's name property
            # The new filename is just the prefix + the old filename
            new_filename = prefix + old_path.name
            
            # Construct the new Path object for the destination file
            # parent is the directory, / is the Path join operator
            new_path = old_path.parent / new_filename
            
            # Print the action for verification
            print(f"Renaming: '{old_path.name}' -> '{new_filename}'")
            
            # 4. Perform the actual rename operation
            old_path.rename(new_path)

    print("\nFile renaming complete.")

# --- Example Usage ---
# ⚠️ IMPORTANT: Change this to the actual path of your directory
# and ensure you run it on a test directory first!
target_directory = "data/imports" 
prefix_filenames_pathlib(target_directory)