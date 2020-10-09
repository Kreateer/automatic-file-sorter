import os
import shutil
import PySimpleGUI as sg
import platform

sg.theme('DarkGrey2')

source_folder = sg.popup_get_folder('Choose source location:', default_path='')
destination_folder = sg.popup_get_folder('Choose destination folder:', default_path='')

folders = {source_folder: destination_folder}
file_type = []


def fmGUI():
    menu = [['&File', ['&Exit']],
            ['&Help', '&About']]

    layout = [
        [sg.Menu(menu, tearoff=False)],
        [sg.Text("Choose Source Folder:")],
        [sg.InputText(''), sg.FolderBrowse()],
        [sg.Text("Choose Destination Folder:")],
        [sg.InputText(''), sg.FolderBrowse()],
        [sg.Frame(layout=[
        [sg.Text("Choose action:")],
        [sg.Radio("Move", "RADIO1", default=True), sg.Radio("Copy", "RADIO1")],
        [sg.Text("Sorting options:")],
        [sg.Checkbox('Sort by Name', default=False, key='SBYNAME'),
         sg.Checkbox('Sort by Date', default=False, key='SBYDATE'),
         sg.Checkbox("Sort by Type", default=False, key='SBYTYPE')]],
            title='Options',title_color='red', relief=sg.RELIEF_SUNKEN)],
        [sg.Text("Choose filetype:")],
        [sg.Combo(['.zip', '.txt', '.md'], key='FILETYPE', enable_events=True),
         sg.Combo(['.png', '.jpg', '.gif'], key='FILETYPE2', enable_events=True)],
        [sg.Ok(), sg.Cancel()]]

    window = sg.Window('Automatic File Mover v1.0', layout, default_element_size=(40, 1))

    while True:
        event, values = window.read()
        file_val = [values[i] for i in ['FILETYPE', 'FILETYPE2']]
        for value in file_val:
            file_type.append(value)
        if event in (sg.WIN_CLOSED, 'Cancel'):
            break
        elif event in 'Ok':
            if values['SBYNAME'] is True:
                sortbyname()
            elif values['SBYDATE'] is True:
                filemover("sbydate")
            elif values['SBYTYPE'] is True:
                sortbytype()
    window.close()


def filemover(option):
    source = folders.keys()
    destination = folders.values()
    while True:
        num_files = len(os.listdir(*source))
        file_ending = str(file_type)[2:-2]
        if num_files == 0:
            sg.PopupError("No files in folder!")
            raise SystemExit()
        # elif option == namesort:
            # sortbyname()

        elif option is 'sbydate':
            for file in os.listdir(*source):
                if file.endswith(file_ending):
                    result = shutil.move(str(*source) + "/" + file, str(*destination) + "/" + file)
                    sortbydate(*destination)
                    is_file_in_curr_dir = os.path.isfile(file)
                    current_dir = os.listdir(*destination)
                    if is_file_in_curr_dir not in current_dir:
                        file_type.pop()

        else:
            for file in os.listdir(*source):
                if file.endswith(file_ending):
                    result = shutil.move(str(*source) + "/" + file, str(*destination) + "/" + file)
                    is_file_in_curr_dir = os.path.isfile(file)
                    current_dir = os.listdir(*destination)
                    if is_file_in_curr_dir not in current_dir:
                        file_type.pop()
        return sg.PopupOK(f"File transfer successful!\nFile(s) moved to '{str(*destination)}'")


def sortbyname():
    source = folders.keys()
    destination = folders.values()
    index_dir = os.listdir(*destination)

    # Ascending order
    if user_picks_ascending:
        for file in os.listdir(*source):
            file_ending = str(file_type)[2:-2]
            if file.endswith(file_ending):
                result = shutil.move(str(*source) + "/" + file, str(*destination) + "/" + file)
                sorted(index_dir)
                is_file_in_curr_dir = os.path.isfile(file)
                current_dir = os.listdir(*destination)
                if is_file_in_curr_dir not in current_dir:
                    file_type.pop()
    # Descending order
    elif user_picks_descending:
        for file in os.listdir(*source):
            file_ending = str(file_type)[2:-2]
            if file.endswith(file_ending):
                result = shutil.move(str(*source) + "/" + file, str(*destination) + "/" + file)
                sorted(index_dir, reverse=True)
                is_file_in_curr_dir = os.path.isfile(file)
                current_dir = os.listdir(*destination)
                if is_file_in_curr_dir not in current_dir:
                    file_type.pop()
    else:
        sg.PopupError("Something went wrong! Could not sort by name!")
        raise SystemExit()


def sortbydate(dir_path):
    if platform.system() == 'Windows':
        for file in dir_path:
            return os.path.getmtime(file)
    else:
        for file in dir_path:
            stat = os.stat(file)
            try:
                return stat.st_birthtime
            except AttributeError():
                # In case file creation date can't be pulled,
                # the last modification date will be returned instead.
                return stat.st_mtime


def sortbytype(ftype):
    source = folders.keys()
    destination = folders.values()
    file_ending = str(file_type)[2:-2]

    # For '.png' files
    if ftype == '.png' or '.jpg' or '.jpeg' or '.gif':
        if os.path.exists(str(destination) + '/' + 'Images'):
            pass
        else:
            os.mkdir(str(destination) + '/' + 'Images')

        for file in os.listdir(*source):
            if file.endswith(file_ending):
                result = shutil.move(str(*source) + "/" + file, str(*destination) + "/" + "Images" + "/" + file)
                is_file_in_curr_dir = os.path.isfile(file)
                current_dir = os.listdir(*destination)
                if is_file_in_curr_dir not in current_dir:
                    file_type.pop()

    # For '.zip' files
    elif ftype == '.zip':
        if os.path.exists(str(destination) + '/' + 'Archives'):
            pass
        else:
            os.mkdir(str(destination) + '/' + 'Archives')

        for file in os.listdir(*source):
            if file.endswith(file_ending):
                result = shutil.move(str(*source) + "/" + file, str(*destination) + "/" + "Archives" + "/" + file)
                is_file_in_curr_dir = os.path.isfile(file)
                current_dir = os.listdir(*destination)
                if is_file_in_curr_dir not in current_dir:
                    file_type.pop()

    # For '.txt' files
    elif ftype == '.txt':
        if os.path.exists(str(destination) + '/' + 'Text Files'):
            pass
        else:
            os.mkdir(str(destination) + '/' + 'Text Files')

        for file in os.listdir(*source):
            if file.endswith(file_ending):
                result = shutil.move(str(*source) + "/" + file, str(*destination) + "/" + "Text Files" + "/" + file)
                is_file_in_curr_dir = os.path.isfile(file)
                current_dir = os.listdir(*destination)
                if is_file_in_curr_dir not in current_dir:
                    file_type.pop()

    # For '.md' files
    elif ftype == '.md':
        if os.path.exists(str(destination) + '/' + 'Markdown Files'):
            pass
        else:
            os.mkdir(str(destination) + '/' + 'Markdown Files')

        for file in os.listdir(*source):
            if file.endswith(file_ending):
                result = shutil.move(str(*source) + "/" + file, str(*destination) + "/" + "Markdown Files" + "/" + file)
                is_file_in_curr_dir = os.path.isfile(file)
                current_dir = os.listdir(*destination)
                if is_file_in_curr_dir not in current_dir:
                    file_type.pop()

    else:
        sg.PopupError("File type not found!")
        raise SystemExit()


fmGUI()
