import os

import MetaInfoAV
import MetaInfoImage
import sys


if __name__ == '__main__':
    print("Вывод метаинформации по картинке/аудио/видео.")
    print("/************************************************\\")
    pathToFile = sys.argv[1]
    if not os.path.exists(pathToFile):
        print('* Файл не найден.')
    else:
        strFormat = pathToFile[len(pathToFile) - 4:len(pathToFile)]

        if strFormat == ".jpg":
            MetaInfoImage.start(pathToFile=pathToFile)
        elif strFormat in [".mp4", ".mp3"]:
            MetaInfoAV.start(pathToFile=pathToFile)
    print("\************************************************/")