from pathlib import Path
import re

def third():
    folder = Path(input("Путь к папке: "))
    list_file = input("Файл со списком: ")
    
    songs = {}
    
    # читаем список песен
    with open(list_file, "r", encoding="utf-8") as f:
        for line in f:
            m = re.search(r"(\d+)\.\s*(.+)", line)
            if m:
                num = m.group(1)
                name = m.group(2).strip().lower()
                songs[name] = num
    
    # переименование файлов
    for file in folder.iterdir():
        if file.is_file():
            name = file.stem.lower()
    
            if name in songs:
                new_name = f"{songs[name]}. {file.stem}{file.suffix}"
                new_path = folder / new_name
                file.rename(new_path)
                print(f"{file.name} -> {new_name}")
