import os

from PIL import Image
from PIL.ExifTags import TAGS


def start(pathToFile: str):
    image = Image.open(pathToFile)
    exifdata = image.getexif()

    if len(exifdata) == 0:
        print("Данных нет.")
    else:
        print(f'\n* Метаданные фото: {os.path.split(pathToFile)[1]:27}\n')

    for tag_id in exifdata:
        tag = TAGS.get(tag_id, tag_id)
        data = exifdata.get(tag_id)
        try:
            if isinstance(data, bytes):
                data = data.decode()
        except Exception:
            print(f"{tag:27}: Ошибка чтения данных")
            continue
        # if tag == "GPSInfo":
        #     print(f'{"GPSInfo":27}: lat {data[2]} {data[1]} - long {data[4]} {data[3]}')
        #     continue
        print(f"{tag:27}: {data}")

    info_dict = {
        "Имя файла": os.path.split(pathToFile)[1],
        "Разрешение изображения": image.size,
        "Высота изображения": image.height,
        "Ширина изображения": image.width,
        "Формат изображения": image.format_description,
        "Режим изображения": image.mode,
        "Анимированное изображение": getattr(image, "is_animated", False),
        "Кадров в изображении": getattr(image, "n_frames", 1)
    }
    print(f'\n* Информация о фото: {os.path.split(pathToFile)[1]:27}\n')
    for key, value in info_dict.items():
        print(f"{key:27}: {value}")

    return
