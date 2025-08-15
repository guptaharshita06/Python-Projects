# Importing the os module to work with the file system
import os

def list_contents(path='.'):
    """
    List and print entries in the given directory (default: current).
    
    :param path: Directory to list
    """
    try:
        # Get a list of all entries (files and subdirectories) in the given path
        entries = os.listdir(path)
        
        # Print the directory name
        print(f"Contents of '{path}':")
        
        # Loop through the entries and print each one
        for name in entries:
            print(name)

    # Handle the case where the directory doesn't exist
    except FileNotFoundError:
        print(f"Error: The directory '{path}' does not exist.")
    
    # Handle the case where the given path is not a directory
    except NotADirectoryError:
        print(f"Error: The path '{path}' is not a directory.")
    
    # Handle the case where the program doesn't have permission to access the path
    except PermissionError:
        print(f"Error: Permission denied to access '{path}'.")
    
    # Catch any other OS-related errors
    except OSError as e:
        print(f"Error: {e}")

# Main section of the program
if __name__ == "__main__":
    # Ask the user for a directory path (leave blank for current directory)
    dir_path = input("Enter directory path (leave blank for current directory): ").strip() or '.'
    
    # Call the function to list contents of the specified directory
    list_contents(dir_path)
