def FileMover():
    import os

    source_file = input("Input the Source File Location: path/to/current/file.foo")
    destination_file = input("Input the destination file location: path/to/new/destination/for/file.foo")

    # Move the file (replacing existing file if necessary)
    os.replace(source_file, destination_file)
    
    return