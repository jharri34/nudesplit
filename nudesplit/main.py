import nude
from nude import Nude
import sortphoto
import os
import time
DATA_PATH = "/mnt/d/Pictures"
OUTPUT_PATH = "/mnt/d/Organize_Pictures"

# This script is designed to check if images are nude or not using the Nude library.
# It will iterate through all files in the specified directory and print the results.

def main():
    # Start processing files
    start_time = time.time()
    # file_paths = collect_file_paths(DATA_PATH)
    output_path = os.path.join(os.path.dirname(DATA_PATH), 'organized_folder')

    end_time = time.time()
    print("-" * 50)
    print("Directory tree before organizing:")
    # display_directory_tree(DATA_PATH)
    print("*" * 50)
    # Confirm successful output path
    message = f"Output path successfully set to: {output_path}"
    print("-" * 50)
    message = f"Time taken to load file paths: {end_time - start_time:.2f} seconds"
    print("-" * 50)
    # Define extensions
    image_extensions = ('.png', '.jpg', '.jpeg', '.gif', '.bmp', '.tiff')
    
    # for file_path in file_paths:
    #    # Exclude hidden files (additional safety)
    #     if os.path.basename(file_path).startswith('.'):
    #         continue
    #     # Get the file extension
    #     ext = os.path.splitext(file_path)[1].lower()
    #     if ext in image_extensions:
    #         n = Nude(file_path)
    #         n.parse()
    #         print("{file_path}",n.result, n.message, n.inspect())
    #         # Check if the image is nude
    #         if n.result:
    #             print(f"{file_path} is nude.")
    #         else:
    #             print(f"{file_path} is not nude.")
    
    

if __name__ == "__main__":
    main()