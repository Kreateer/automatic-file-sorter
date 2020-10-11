import os
import shutil
import platform
import PySimpleGUI as sg

source_folder = sg.popup_get_folder('Choose source location:', default_path='')
destination_folder = sg.popup_get_folder('Choose destination folder:', default_path='')

#folders = {source_folder: destination_folder}
file_type = []
mode_list = []
sort_list = []
crit_list = []

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
            [sg.Combo(['Copy', 'Move'], default_value='Move' ,key='OPERATION')],
            [sg.Frame(layout=[
                [sg.Text("Sorting options:")],
                [sg.Checkbox('Sort by Name', default=False, key='SBYNAME', enable_events=True)],
                [sg.Frame(layout=[
                    [sg.Radio("Ascending", "RADIO1", default=True, key='asc'),
                     sg.Radio("Descending", "RADIO1", key='dsc')]],
                    title='Sort Order', title_color='red', relief=sg.RELIEF_SUNKEN, visible=False, key='SBYNAMEFRAME')],
                [sg.Checkbox('Sort by Date', default=False, key='SBYDATE', enable_events=True),
                 sg.Checkbox("Sort by Type", default=False, key='SBYTYPE', enable_events=True)]],
                title='Options', title_color='red', relief=sg.RELIEF_SUNKEN)],
            [sg.Text("Choose filetype:")],
            [sg.Combo(['.zip', '.png'], key='FILETYPE', enable_events=True)],
            [sg.Ok(), sg.Cancel()]]
        window = sg.Window('Choose filetype to move', layout, default_element_size=(40, 1))

        while True:
            event, values = window.read()
            if event in (sg.WIN_CLOSED, 'Cancel'):
                break
            elif event in 'Ok':
                if values['FILETYPE'] not in file_type:
                    file_type.append(values['FILETYPE'])
                    run_fmover = FileMover()
                    append_mode(values['OPERATION'])
                    for value in sort_list:
                        if value == 'Sort by Name' or 'Sort by Date' or 'Sort by Type':
                            run_fmover.filemover(values['OPERATION'], value)
                        else:
                            run_fmover.filemover(values['OPERATION'], None)
                    # if values['SBYNAME'] is True:
                    #     run_fmover.filemover(values['OPERATION'], values['SBYNAME'])
                    # elif values['SBYDATE'] is True:
                    #     run_fmover.filemover(values['OPERATION'], values['SBYDATE'])
                    # elif values['SBYTYPE'] is True:
                    #     run_fmover.filemover(values['OPERATION'], values['SBYTYPE'])
                    # else:
                    #     run_fmover.filemover(values['OPERATION'], None)
                else:
                    run_fmover = FileMover()
                    append_mode(values['OPERATION'])
                    for value in sort_list:
                        if value == 'Sort by Name' or 'Sort by Date' or 'Sort by Type':
                            run_fmover.filemover(values['OPERATION'], value)
                        else:
                            run_fmover.filemover(values['OPERATION'], None)

            elif event in 'SBYNAME':
                if values['SBYNAME'] is True:
                    window.Element('SBYNAMEFRAME').update(visible=True)
                    sort_list.append('Sort by Name')
                    if values['asc'] is True:
                        get_sbyname_mode('ascending')
                    elif values['dsc'] is True:
                        get_sbyname_mode('descending')
                    else:
                        crit_list.pop()
                else:
                    window.Element('SBYNAMEFRAME').update(visible=False)
                    sort_list.remove('Sort by Name')

            elif event in 'SBYDATE':
                if values['SBYDATE'] is True:
                    sort_list.append('Sort by Date')
                else:
                    sort_list.remove('Sort by Date')

            elif event in 'SBYTYPE':
                if values['SBYTYPE'] is True:
                    sort_list.append('Sort by Type')
                else:
                    sort_list.remove('Sort by Type')

            else:
                pass

        window.close()


def append_mode(mode):
    mode_list.append(mode)
    if mode in mode_list:
        return mode


def detect_mode():
    return mode_list[0]


def get_file_type():
    return str(file_type)[2:-2]


def get_sbyname_mode(criteria):
    if criteria == 'ascending':
        crit_list.append(criteria)
    elif criteria == 'descending':
        crit_list.append(criteria)


def write_sbyname_mode():
    return crit_list[0]


class FileMover():
    #def __init__(self, sortbyname, sortbydate, sortbytype, no_sort):
    #    self.sortbyname = sortby.sortbyname()
    #    self.sortbydate = sortoption2
    #    self.sortbytype = sortoption3
    #    self.no_sort = False

    def filemover(self, operation, sortby):
        while True:
            num_files = len(os.listdir(get_path('src')))
            if num_files == 0:
                sg.PopupError("No files in folder!")
                raise SystemExit()
            elif sortby is None:
                for file in os.listdir(get_path('src')):
                    file_ending = get_file_type()
                    if file.endswith(file_ending):
                        result = None
                        if operation == "Copy":
                            result = shutil.copy(get_path('src') + "/" + file, get_path('dst') + "/" + file)
                        else:
                            result = shutil.move(get_path('src') + "/" + file, get_path('dst') + "/" + file)
                        is_file_in_curr_dir = os.path.isfile(get_path('dst') + "/" + file)
                        current_dir = os.listdir(get_path('dst'))
                        if file not in current_dir:
                            file_type.pop()
            elif sortby == 'Sort by Name':
                for file in os.listdir(get_path('src')):
                    file_ending = get_file_type()
                    if file.endswith(file_ending):
                        result = None
                        if operation == "Copy" and write_sbyname_mode() == 'ascending':
                            result = shutil.copy(get_path('src') + "/" + file, get_path('dst') + "/" + file)
                            sortby.sortbyname(asc=True)

                        elif operation == "Copy" and write_sbyname_mode() == 'descending':
                            result = shutil.copy(get_path('src') + "/" + file, get_path('dst') + "/" + file)
                            sortby.sortbyname(dsc=True)

                        elif operation == 'Move' and write_sbyname_mode() == 'ascending':
                            result = shutil.move(get_path('src') + "/" + file, get_path('dst') + "/" + file)
                            sortby.sortbyname(asc=True)

                        elif operation == 'Move' and write_sbyname_mode() == 'descending':
                            result = shutil.move(get_path('src') + "/" + file, get_path('dst') + "/" + file)
                            sortby.sortbyname(dsc=True)

                        else:
                            result = shutil.move(get_path('src') + "/" + file, get_path('dst') + "/" + file)
                            sortby.sortbyname(asc=True)
                        is_file_in_curr_dir = os.path.isfile(get_path('dst') + "/" + file)
                        current_dir = os.listdir(get_path('dst'))
                        if file not in current_dir:
                            file_type.pop()
            elif sortby == 'Sort by Date':
                sc = SortCriteria()
                for file in os.listdir(get_path('src')):
                    file_ending = get_file_type()
                    if file.endswith(file_ending):
                        result = None
                        if operation == "Copy":
                            result = shutil.copy(get_path('src') + "/" + file, get_path('dst') + "/" + file)
                        else:
                            result = shutil.move(get_path('src') + "/" + file, get_path('dst') + "/" + file)
                        sbd = sc.sortbydate(get_path('dst'))
                        is_file_in_curr_dir = os.path.isfile(get_path('dst') + "/" + file)
                        current_dir = os.listdir(get_path('dst'))
                        if file not in current_dir:
                            file_type.pop()
            return sg.PopupOK(f"File transfer successful!\nFile(s) moved to '{get_path('dst')}'")


fmover = FileMover()

source = get_path('src')
destination = get_path('dst')


class SortCriteria():

    def sortbyname(self, asc, dsc):
        index_dir = os.listdir(destination)
        asc = False
        dsc = False

        # Ascending order
        if asc is True and dsc is False:
            sorted(index_dir)
        # Descending order
        elif dsc is True and asc is False:
            sorted(index_dir, reverse=True)
        else:
            sg.PopupError("Something went wrong! Could not sort by name!")
            raise SystemExit()

    def sortbydate(self, dir_path):
        date_dic = {}
        #if platform.system() == 'Windows':
        for file in dir_path: # returns 'F' instead of file name
            import operator
            date_dic.update({file: os.stat(file).st_mtime})
            print(date_dic)
            #dic_list.sort(key=lambda x: os.stat(os.path.join(dir_path, x)).st_mtime)
            return sorted(date_dic.items(), key=operator.itemgetter(1))
            #{value for value in sorted(date_dic.items(), key=lambda item: item[1])}

        else:
            pass
            # for file in dir_path:
            #     stat = os.stat(file)
            #     try:
            #         return stat.st_birthtime
            #     except AttributeError():
            #         # In case file creation date can't be pulled,
            #         # the last modification date will be returned instead.
            #         return stat.st_mtime

    def sortbytype(self, ftype):

        # For '.png' files
        if ftype == '.png' or '.jpg' or '.jpeg' or '.gif':
            if os.path.exists(str(destination) + '/' + 'Images'):
                pass
            else:
                os.mkdir(str(destination) + '/' + 'Images')

            detect_mode()


            # for file in os.listdir(*source):
            #     if file.endswith(file_ending):
            #         result = shutil.move(str(*source) + "/" + file, str(*destination) + "/" + "Images" + "/" + file)
            #         is_file_in_curr_dir = os.path.isfile(file)
            #         current_dir = os.listdir(*destination)
            #         if is_file_in_curr_dir not in current_dir:
            #             file_type.pop()

        # For '.zip' files
        elif ftype == '.zip':
            if os.path.exists(str(destination) + '/' + 'Archives'):
                pass
            else:
                os.mkdir(str(destination) + '/' + 'Archives')

            # for file in os.listdir(*source):
            #     if file.endswith(file_ending):
            #         result = shutil.move(str(*source) + "/" + file, str(*destination) + "/" + "Archives" + "/" + file)
            #         is_file_in_curr_dir = os.path.isfile(file)
            #         current_dir = os.listdir(*destination)
            #         if is_file_in_curr_dir not in current_dir:
            #             file_type.pop()
            detect_mode()

        # For '.txt' files
        elif ftype == '.txt':
            if os.path.exists(str(destination) + '/' + 'Text Files'):
                pass
            else:
                os.mkdir(str(destination) + '/' + 'Text Files')

            # for file in os.listdir(*source):
            #     if file.endswith(file_ending):
            #         result = shutil.move(str(*source) + "/" + file, str(*destination) + "/" + "Text Files" + "/" + file)
            #         is_file_in_curr_dir = os.path.isfile(file)
            #         current_dir = os.listdir(*destination)
            #         if is_file_in_curr_dir not in current_dir:
            #             file_type.pop()
            detect_mode()

        # For '.md' files
        elif ftype == '.md':
            if os.path.exists(str(destination) + '/' + 'Markdown Files'):
                pass
            else:
                os.mkdir(str(destination) + '/' + 'Markdown Files')

            # for file in os.listdir(*source):
            #     if file.endswith(file_ending):
            #         result = shutil.move(str(*source) + "/" + file,
            #                              str(*destination) + "/" + "Markdown Files" + "/" + file)
            #         is_file_in_curr_dir = os.path.isfile(file)
            #         current_dir = os.listdir(*destination)
            #         if is_file_in_curr_dir not in current_dir:
            #             file_type.pop()
            detect_mode()

        else:
            sg.PopupError("File type not found!")
            raise SystemExit()



























main_gui = fmGUI()
main_gui.main_window()
