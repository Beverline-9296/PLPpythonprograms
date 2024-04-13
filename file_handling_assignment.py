try:
    with open("my-file.text","w") as y:
        y.write("This is the first line\n")
        y.write("012345679\n")
        y.write("the second line ha a text and numbers: 67670\n")
except FileNotFoundError:
    print("This file is not found on your directory")
except PermissionError:
    print("Permission Denied.")
finally:
    print("File creation completed.")
    # File Reading and Display
try:
    with open("my_file.txt", "r") as f:
        print("Contents of my_file.txt:")
        for line in f:
            print(line.strip())
except FileNotFoundError:
    print("File not found.")
except PermissionError:
    print("Permission denied.")
finally:
    print("File reading completed.")

# File Appending
try:
    with open("my_file.txt", "a") as f:
        f.write("Additional line 1\n")
        f.write("Another additional line\n")
        f.write("Line 3 of additional text\n")
except FileNotFoundError:
    print("File not found.")
except PermissionError:
    print("Permission denied.")
finally:
    print("File appending completed.")