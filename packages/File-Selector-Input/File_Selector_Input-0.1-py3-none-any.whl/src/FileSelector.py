def FileMover():
    import os
    import tkinter.dialog
    from tkinter.ttk import FileSelectBox, DirSelectBox
    
    print('Choose Source File:')
    source_file = tkinter.dialog
    
    print('Choose Destination Folder:')
    destination_file = tkinter.dialog

    # Move the file (replacing existing file if necessary)
    os.replace(source_file, destination_file)
    
    return