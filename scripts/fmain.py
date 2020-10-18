import os
import shutil
import PySimpleGUI as sg

source_folder = sg.popup_get_folder('Choose source location:', default_path="Source Directory Path...")
if source_folder == "Source Directory Path...":
    sg.PopupError("Directory path not specified!")
    raise SystemExit()
elif source_folder is None:
    raise SystemExit()
else:
    pass

destination_folder = sg.popup_get_folder(
    'Choose destination folder:', default_path="Destination Directory Path...")

if destination_folder == "Destination Directory Path...":
    sg.PopupError("Directory path not specified!")
    raise SystemExit()
elif destination_folder is None:
    raise SystemExit()
else:
    pass

file_type = []
mode_list = []
sort_list = []

image_list = ['.png', '.jpg', '.jpeg', '.jfif',
              '.heic', '.gif', '.bmp', '.tif', '.psd']
archive_list = ['.zip', '.rar', '.7z', '.deb',
                '.tar', '.pkg', '.tar.gz', '.gz', '.rpm', '.z']
textf_list = ['.txt', '.md', '.pdf', '.doc',
              '.docx', '.xls', '.xlsx', '.csv', '.rtf', '.tex']
video_list = ['.mp4', '.m4v', '.mov', '.wmv',
              '.flv', '.avi', '.mpeg', '.mpg', '.mpe']
audio_list = ['.m4a', '.mp3', '.wav', '.flac',
              '.wma', '.aac', '.aiff', '.aif', '.aifc']


def get_path(src_or_dst):
    folders = {source_folder: destination_folder}
    source = folders.keys()
    destination = folders.values()
    if src_or_dst == 'src':
        return str(*source)
    elif src_or_dst == 'dst':
        return str(*destination)
    else:
        raise SystemError("Parameter has to be 'src' or 'dst'")


class fmGUI:

    def main_window(self):
        layout = [
            [sg.Text("Choose Operation to perform:")],
            [sg.Combo(['Copy', 'Move'], default_value='Move', key='OPERATION'),
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
                    "Audio ('.mp3', '.wav'...)"
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
            elif event in 'Ok':
                if values['FILETYPE'] not in file_type:
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

        else:
            pass


def append_mode(mode):
    mode_list.append(mode)
    if mode in mode_list:
        return mode


def detect_mode():
    return mode_list[0]


def append_file_type(value):
    if len(file_type) == 1:
        file_type.clear()
    else:
        pass
    file_type.append(value)
    translate_filetype()
    return value


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

source = get_path('src')
destination = get_path('dst')


def get_subdir():
    if os.path.exists(str(destination) + '/' + 'Images'):
        return True

    elif os.path.exists(str(destination) + '/' + 'Archives'):
        return True

    elif os.path.exists(str(destination) + '/' + 'Text Files'):
        return True

    elif os.path.exists(str(destination) + '/' + 'Videos'):
        return True

    elif os.path.exists(str(destination) + '/' + 'Audio'):
        return True

    else:
        return False


class SortCriteria():

    def sortbytype(self, ftype):
        type_list = [ftype]

        # For image files
        for type in type_list:
            if type in image_list:  # '.png' or '.jpg' or '.jpeg' or '.gif':
                if os.path.exists(str(destination) + '/' + 'Images'):
                    return str(os.path.join(str(destination) + '/' + 'Images'))
                else:
                    os.mkdir(str(destination) + '/' + 'Images')
                    return str(os.path.join(str(destination) + '/' + 'Images'))

        # For archive files
            elif type in archive_list:
                if os.path.exists(str(destination) + '/' + 'Archives'):
                    return str(os.path.join(str(destination) + '/' + 'Archives'))
                else:
                    os.mkdir(str(destination) + '/' + 'Archives')
                    return str(os.path.join(str(destination) + '/' + 'Archives'))

        # For text files
            elif type in textf_list:
                if os.path.exists(str(destination) + '/' + 'Text Files'):
                    return str(os.path.join(str(destination) + '/' + 'Text Files'))
                else:
                    os.mkdir(str(destination) + '/' + 'Text Files')
                    return str(os.path.join(str(destination) + '/' + 'Text Files'))

        # For video files
            elif type in video_list:
                if os.path.exists(str(destination) + '/' + 'Videos'):
                    return str(os.path.join(str(destination) + '/' + 'Videos'))
                else:
                    os.mkdir(str(destination) + '/' + 'Videos')
                    return str(os.path.join(str(destination) + '/' + 'Videos'))

        # For audio files
            elif type in audio_list:
                if os.path.exists(str(destination) + '/' + 'Audio'):
                    return str(os.path.join(str(destination) + '/' + 'Audio'))
                else:
                    os.mkdir(str(destination) + '/' + 'Audio')
                    return str(os.path.join(str(destination) + '/' + 'Audio'))

            else:
                sg.PopupError("File type not found!")
                raise SystemExit()


main_gui = fmGUI()
main_gui.main_window()
