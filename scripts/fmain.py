import os
import shutil
import PySimpleGUI as sg
#from scripts import fmsort

#sortby = fmsort.SortCriteria()

source_folder = sg.popup_get_folder('Choose source location:', default_path='')
destination_folder = sg.popup_get_folder('Choose destination folder:', default_path='')

#folders = {source_folder: destination_folder}
file_type = []

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


class fmGUI():

    def main_window(self):
        layout = [
            [sg.Text("Choose Operation to perform:")],
            [sg.Combo(['Copy', 'Move'], key='OPERATION')],
            [sg.Text("Choose filetype:")],
            [sg.Combo(['.zip', '.png'], key='FILETYPE', enable_events=True)],
            [sg.Ok(), sg.Cancel()]
        ]
        window = sg.Window('Choose filetype to move', layout, default_element_size=(40, 1))

        while True:
            event, values = window.read()
            if event in (sg.WIN_CLOSED, 'Cancel'):
                break
            elif event in 'Ok':
                if values['FILETYPE'] not in file_type:
                    file_type.append(values['FILETYPE'])
                    run_fmover = FileMover(no_sort=False)
                    run_fmover.filemover(values['OPERATION'])
        window.close()


class FileMover():
    def __init__(self, no_sort):
    #    self.sort1 = sortoption1
    #    self.sort2 = sortoption2
    #    self.sort3 = sortoption3
        self.no_sort = False

    def filemover(self, mode):
        while True:
            self.no_sort = True
            num_files = len(os.listdir(get_path('src')))
            if num_files == 0:
                sg.PopupError("No files in folder!")
                raise SystemExit()
            elif self.no_sort:
                for file in os.listdir(get_path('src')):
                    file_ending = str(file_type)[2:-2]
                    if file.endswith(file_ending):
                        result = None
                        if mode == "Copy":
                            result = shutil.copy(get_path('src') + "/" + file, get_path('dst') + "/" + file)
                        else:
                            result = shutil.move(get_path('src') + "/" + file, get_path('dst') + "/" + file)
                        print(file)
                        is_file_in_curr_dir = os.path.isfile(get_path('dst') + "/" + file)
                        current_dir = os.listdir(get_path('dst'))
                        if file not in current_dir:
                            print(file_type)
                            file_type.pop()
            return sg.PopupOK(f"File transfer successful!\nFile(s) moved to '{get_path('dst')}'")


main_gui = fmGUI()
main_gui.main_window()
