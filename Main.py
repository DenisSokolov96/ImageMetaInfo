import os

import PySimpleGUI as sg
import MetaInfoAV
import MetaInfoImage


# Открыть проводник
def set_path():
    ftypes = [('Фото', '*.jpg'), ('Музыка', '*.mp3'), ('Видео', '*.mp4'), ('Все файлы', '*')]
    dlg = sg.filedialog.Open(filetypes=ftypes)
    fl = dlg.show()
    if fl != '':
        return fl
    return ''


def main_wind():
    sg.theme('Light Green')
    menu_def = [["&Меню",'Проверить']]

    layout = [[sg.Menu(menu_def, tearoff=False)],
              [sg.Text("Укажите путь до файла...")],
              [sg.Button("Выбрать файл", key='-load-'), sg.Input(key='-Input-', size=(45, 1), justification='left'),
               sg.Button("Очистить вывод", key='-clear-')],
              [sg.Output(size=(88, 20), key='-out-')]]
    window = sg.Window('Метаинформация', layout)
    while True:
        event, values = window.read()
        if event == 'Проверить' and values['-Input-'] != '':
            pathToFile = values['-Input-']
            print("Вывод метаинформации по картинке/аудио/видео.")
            print("/************************************************\\")
            if not os.path.exists(pathToFile):
                print('* Файл не найден.')
            else:
                strFormat = pathToFile[len(pathToFile) - 4:len(pathToFile)]

                if strFormat == ".jpg":
                    MetaInfoImage.start(pathToFile=pathToFile)
                elif strFormat in [".mp4", ".mp3"]:
                    MetaInfoAV.start(pathToFile=pathToFile)
            print("\************************************************/")

        if event == '-clear-':
            window['-out-'].update("")

        if event == '-load-':
            window['-Input-'].update(set_path())

        if event in (sg.WIN_CLOSED, 'Quit'):
            break
    window.close()


if __name__ == '__main__':
    main_wind()