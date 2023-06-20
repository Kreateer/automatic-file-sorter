import os
import shutil
import PySimpleGUI as sg

SOURCE_FOLDER_KEY = 'SRC'
DESTINATION_FOLDER_KEY = 'DST'


source_folder = None


destination_folder = None


"""List Section

General Lists

'file_type' holds the current file type(s) being moved or copied
'mode_list' holds the selected operation - Move or Copy
'sort_list' holds the selected sorting option ('Sort by Type'...)

'File Type' Lists

These are actually self-explanatory, but descriptions have been added anyway for consistency's sake

'image_list' holds image file types
'archive_list' holds archive file types
'textf_list' holds text file types
'video_list' holds video file types
'audio_list' holds audio file types
'code_list' holds code file types
'present_list' holds presentation file types

"""

file_type = []
mode_list = []
sort_list = []

image_list = ['.png', '.jpg', '.jpeg', '.jfif',
              '.heic', '.gif', '.bmp', '.tif', '.psd']
archive_list = ['.zip', '.rar', '.7z', '.deb',
                '.tar', '.pkg', '.tar.gz', '.gz',
                '.rpm', '.z', 'tar.xz', 'xz']
textf_list = ['.txt', '.md', '.pdf', '.doc',
              '.docx', '.xls', '.xlsx', '.csv',
              '.rtf', '.tex', '.json', '.xml']
video_list = ['.mp4', '.m4v', '.mov', '.wmv',
              '.flv', '.avi', '.mpeg', '.mpg', '.mpe']
audio_list = ['.m4a', '.mp3', '.wav', '.flac',
              '.wma', '.aac', '.aiff', '.aif', '.aifc']
code_list = ['.c', '.cgi', '.pl', '.class',
              '.cpp', '.cs', '.h', '.hpp',
              '.java', '.php', '.py', '.pyc',
               '.sh', '.swift', '.vb']
present_list = ['pptx', 'pptm', 'ppt', 'potx',
                'pot', 'potm', 'ppsx', 'pps']


"""PySimpleGUI Main Window

The 'fmGUI' class holds the main GUI window for the program.
Any changes or additions to the GUI should go here.

Refer to https://pysimplegui.readthedocs.io/en/latest/ for info. on PySimpleGUI elements

"""


class fmGUI:

    def main_window(self):
        folder_select_layout = [
            [
                sg.Text('Select source folder', size=(20,1)),
                sg.In(key='SRC', enable_events=True),
                sg.FolderBrowse()
            ],
            [
                sg.Text('Select destination folder', size=(20,1)),
                sg.In(key='DST', enable_events=True),
                sg.FolderBrowse()
            ],
        ]
        layout = [
            [sg.Frame(
                'Choose source and destination folders',
                layout=folder_select_layout,
            )],
            [sg.Text("Choose Operation to perform:")],
            [sg.Combo(['Copy', 'Move'], default_value='Move', key='OPERATION', size=(10, 1)),
             sg.CBox(
                 "Overwrite files",
                 tooltip="Incoming files will replace files of the same names in the destination",
                 key="OVERWRITE"
            )],
            [sg.Frame(layout=[
                [sg.Text("Sort by Type")],
                [sg.Radio("Enabled", "RADIO1", default=False, key='SBYTE', enable_events=True),
                 sg.Radio("Disabled", "RADIO1", default=True, key='SBYTD', enable_events=True)]
            ], title='Sorting Options', title_color='red', relief=sg.RELIEF_SUNKEN)],
            [sg.Text("Choose filetype:")],
            [sg.Combo(  # Options for type of file
                [
                    "Archive ('.zip', '.rar'...)",
                    "Image ('.png', '.jpg'...)",
                    "Text ('.txt', '.docx'...)",
                    "Video ('.mp4', '.mov'...)",
                    "Audio ('.mp3', '.wav'...)",
                    "Code ('.cpp', '.py'...)",
                    "Presentation ('.pptx', '.pptm'...)"
                ],
                key='FILETYPE', enable_events=True
            )],
            [sg.Ok(), sg.Cancel()]]

        window = sg.Window('Choose filetype to move', layout,
                           default_element_size=(40, 1))

        while True:
            event, values = window.read()
            if event in (sg.WIN_CLOSED, 'Cancel'):
                break
            elif event in ['SRC', 'DST']:
                set_path(event, values[event])
            elif event in 'Ok':
                if not get_path('src') or not get_path('dst'):
                    missing_fields = None
                    if not get_path('src') and not get_path('dst'):
                        missing_fields = "source and destination folders"
                    elif not get_path('src'):
                        missing_fields = "source folder"
                    else:
                        missing_fields = "destination folder"
                    sg.PopupOK("Oops! You didn't select the {}".format(missing_fields))
                elif values['FILETYPE'] not in file_type:
                    append_file_type(values['FILETYPE'])
                    run_fmover = FileMover()
                    append_mode(values['OPERATION'])
                    if len(sort_list) == 1:
                        for value in sort_list:
                            if value == 'Sort by Type':
                                run_fmover.filemover(
                                    values['OPERATION'], value, values['OVERWRITE'])
                            else:
                                run_fmover.filemover(
                                    values['OPERATION'], None, values['OVERWRITE'])
                    else:
                        run_fmover.filemover(
                            values['OPERATION'], None, values['OVERWRITE'])

                else:
                    run_fmover = FileMover()
                    append_mode(values['OPERATION'])
                    if len(sort_list) == 1:
                        for value in sort_list:
                            if value == 'Sort by Type':
                                run_fmover.filemover(
                                    values['OPERATION'], value, values['OVERWRITE'])
                            else:
                                run_fmover.filemover(
                                    values['OPERATION'], None, values['OVERWRITE'])
                    else:
                        run_fmover.filemover(
                            values['OPERATION'], None, values['OVERWRITE'])

            elif event in 'SBYTE':
                if values['SBYTE'] is True:
                    sort_list.append('Sort by Type')
                else:
                    pass

            elif event in 'SBYTD':
                if values['SBYTD'] is True:
                    sort_list.clear()
                else:
                    pass
            else:
                pass

        window.close()


# This function pulls and returns source or destination path from dictionary

def get_path(src_or_dst):
    global source_folder
    global destination_folder
    if src_or_dst == 'src' and source_folder is None:
        return None
    if src_or_dst == 'dst' and destination_folder is None:
        return None
    folders = {source_folder: destination_folder}
    source = folders.keys()
    destination = folders.values()
    if src_or_dst == 'src':
        return str(*source)
    elif src_or_dst == 'dst':
        return str(*destination)
    else:
        raise SystemError("Parameter has to be 'src' or 'dst'")


def set_path(folder_type, path):
    """Set the path of source/destination folders selected"""
    global source_folder
    global destination_folder
    valid_keys = [SOURCE_FOLDER_KEY, DESTINATION_FOLDER_KEY]
    if folder_type == SOURCE_FOLDER_KEY:
        source_folder = path
    elif folder_type == DESTINATION_FOLDER_KEY:
        destination_folder = path
    else:
        raise SystemError("Parameter has to be one of {}".format(valid_keys))


# This function matches GUI file type options with appropriate values in file type lists

def translate_filetype():
    for value in file_type:
        if value.startswith("Archive"):
            file_type.clear()
            for arch in archive_list:
                file_type.append(arch)
            return str(file_type)

        elif value.startswith("Image"):
            file_type.clear()
            for img in image_list:
                file_type.append(img)
            return str(file_type)

        elif value.startswith("Text"):
            file_type.clear()
            for txt in textf_list:
                file_type.append(txt)
            return str(file_type)

        elif value.startswith("Video"):
            file_type.clear()
            for vid in video_list:
                file_type.append(vid)
            return str(file_type)

        elif value.startswith("Audio"):
            file_type.clear()
            for aud in audio_list:
                file_type.append(aud)
            return str(file_type)

        elif value.startswith("Code"):
            file_type.clear()
            for cod in code_list:
                file_type.append(cod)
            return str(file_type)

        elif value.startswith("Presentation"):
            file_type.clear()
            for prs in present_list:
                file_type.append(prs)
            return str(file_type)
        else:
            pass


# This function appends the selected mode (Move or Copy) to list

def append_mode(mode):
    mode_list.append(mode)
    if mode in mode_list:
        return mode

# This simply returns the currently selected mode (Move or Copy)

def detect_mode():
    return mode_list[0]


# This function clears the file_type list if not empty and appends new string value from the GUI options

def append_file_type(value):
    if len(file_type) == 1:
        file_type.clear()
    else:
        pass
    file_type.append(value)
    translate_filetype()
    return value


"""Main Program

The 'FileMover' class represents the main section of the program that is
responsible for moving/copying and sorting files.

"""



class FileMover():

    def filemover(self, operation, sortby, overwrite):
        while True:
            num_files = len(os.listdir(get_path('src')))
            if num_files == 0:
                sg.PopupError("No files in folder!")
                raise SystemExit()
            elif sortby is None:
                for file in os.listdir(get_path('src')):
                    #file_ending = get_file_type()
                    is_file_in_curr_dir = os.path.isfile(
                        get_path('dst') + "/" + file)
                    for value in file_type:
                        if file.endswith(value):
                            result = None
                            if is_file_in_curr_dir is False or overwrite:
                                if operation == "Copy":
                                    result = shutil.copy(
                                        get_path('src') + "/" + file, get_path('dst') + "/" + file)
                                else:
                                    result = shutil.move(
                                        get_path('src') + "/" + file, get_path('dst') + "/" + file)
                        # if file not in current_dir:
                        #    file_type.pop()

            elif sortby == 'Sort by Type':
                for file in os.listdir(get_path('src')):
                    sc = SortCriteria()
                    is_file_in_dst_dir = os.path.isfile(
                        get_path('dst') + "/" + file)
                    get_subdir()

                    for value in file_type:
                        if file.endswith(value):

                            if (is_file_in_dst_dir is False or overwrite) and get_subdir() is False:
                                result = None
                                if operation == "Copy":
                                    result = shutil.copy(
                                        get_path('src') + "/" + file, sc.sortbytype(value) + "/" + file)
                                else:
                                    result = shutil.move(
                                        get_path('src') + "/" + file, sc.sortbytype(value) + "/" + file)

                            elif (is_file_in_dst_dir is False or overwrite) and get_subdir() is True:
                                result = None
                                if operation == 'Copy':
                                    result = shutil.copy(
                                        get_path('src') + "/" + file, sc.sortbytype(value) + "/" + file)
                                else:
                                    result = shutil.move(
                                        get_path('src') + "/" + file, sc.sortbytype(value) + "/" + file)
                            else:
                                pass

            return sg.PopupOK(f"File transfer successful!\nFile(s) moved to '{get_path('dst')}'")


fmover = FileMover()


# This function checks if a sub directory already exists and returns False if it doesn't.

def get_subdir():
    if os.path.exists(str(get_path('dst')) + '/' + 'Images'):
        return True

    elif os.path.exists(str(get_path('dst')) + '/' + 'Archives'):
        return True

    elif os.path.exists(str(get_path('dst')) + '/' + 'Text Files'):
        return True

    elif os.path.exists(str(get_path('dst')) + '/' + 'Videos'):
        return True

    elif os.path.exists(str(get_path('dst')) + '/' + 'Audio'):
        return True

    elif os.path.exists(str(get_path('dst')) + '/' + 'Code'):
        return True

    elif os.path.exists(str(get_path('dst')) + '/' + 'Presentations'):
        return True
    
    else:
        return False


"""Sorting Options

The 'SortCriteria' class holds file sorting options.

'sortbytype' function sorts files by their file type and creates a sub directory for each file group
within the destination directory.

"""


class SortCriteria():

    def sortbytype(self, ftype):
        type_list = [ftype]

        # For image files
        for type in type_list:
            if type in image_list:
                if os.path.exists(str(get_path('dst')) + '/' + 'Images'):
                    return str(os.path.join(str(get_path('dst')) + '/' + 'Images'))
                else:
                    os.mkdir(str(get_path('dst')) + '/' + 'Images')
                    return str(os.path.join(str(get_path('dst')) + '/' + 'Images'))

        # For archive files
            elif type in archive_list:
                if os.path.exists(str(get_path('dst')) + '/' + 'Archives'):
                    return str(os.path.join(str(get_path('dst')) + '/' + 'Archives'))
                else:
                    os.mkdir(str(get_path('dst')) + '/' + 'Archives')
                    return str(os.path.join(str(get_path('dst')) + '/' + 'Archives'))

        # For text files
            elif type in textf_list:
                    if os.path.exists(str(get_path('dst')) + '/' + 'Text Files'):
                        return str(os.path.join(str(get_path('dst')) + '/' + 'Text Files'))
                    else:
                        os.mkdir(str(get_path('dst')) + '/' + 'Text Files')
                        return str(os.path.join(str(get_path('dst')) + '/' + 'Text Files'))

        # For video files
            elif type in video_list:
                if os.path.exists(str(get_path('dst')) + '/' + 'Videos'):
                    return str(os.path.join(str(get_path('dst')) + '/' + 'Videos'))
                else:
                    os.mkdir(str(get_path('dst')) + '/' + 'Videos')
                    return str(os.path.join(str(get_path('dst')) + '/' + 'Videos'))

        # For audio files
            elif type in audio_list:
                if os.path.exists(str(get_path('dst')) + '/' + 'Audio'):
                    return str(os.path.join(str(get_path('dst')) + '/' + 'Audio'))
                else:
                    os.mkdir(str(get_path('dst')) + '/' + 'Audio')
                    return str(os.path.join(str(get_path('dst')) + '/' + 'Audio'))

        # For code files
            elif type in code_list:
                if os.path.exists(str(get_path('dst')) + '/' + 'Code'):
                    return str(os.path.join(str(get_path('dst')) + '/' + 'Code'))
                else:
                    os.mkdir(str(get_path('dst')) + '/' + 'Code')
                    return str(os.path.join(str(get_path('dst')) + '/' + 'Code'))
                
        # For presentation files
            elif type in present_list:
                if os.path.exists(str(get_path('dst')) + '/' + 'Presentations'):
                    return str(os.path.join(str(get_path('dst')) + '/' + 'Presentations'))
                else:
                    os.mkdir(str(get_path('dst')) + '/' + 'Presentations')
                    return str(os.path.join(str(get_path('dst')) + '/' + 'Presentations'))

            else:
                sg.PopupError("File type not found!")
                raise SystemExit()


main_gui = fmGUI()
main_gui.main_window()
