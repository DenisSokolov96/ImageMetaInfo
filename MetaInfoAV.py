import ffmpeg
import os.path


def start(pathToFile: str):
    exifdata = []
    try:
        exifdata = ffmpeg.probe(pathToFile)["streams"]
    except ffmpeg._run.Error:
        print('* Неподдерживаемый формат')
    except Exception as e:
        print(f"Ошибка: {e}")

    if len(exifdata) == 0:
        print("Данных нет.")
    else:
        print(f'\n* Метаданные файла: {os.path.split(pathToFile)[-1]}\n')

    for listTag in exifdata:
        for tag_id in listTag:
            data = listTag.get(tag_id)
            try:
                if isinstance(data, bytes):
                    data = data.decode()
            except Exception:
                print(f"{tag_id:25}: Ошибка чтения данных")
                continue
            if type(data) is dict:
                print(f"{tag_id:5} =>")
                for tagInData in data:
                    dataSet = data.get(tagInData)
                    print(f"|___{tagInData:25}: {dataSet}")
                continue
            print(f"{tag_id:25}: {data}")

    return

