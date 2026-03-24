from pathlib import Path
import hashlib

def second():
    folder = input("Введите путь к директории: ")
    files_data = {}

    for path in Path(folder).rglob("*"):
        if path.is_file():
            try:
                md5 = hashlib.md5()

                with open(path, "rb") as f:
                    while chunk := f.read(4096):
                        md5.update(chunk)

                file_hash = md5.hexdigest()

                if file_hash in files_data:
                    files_data[file_hash].append(str(path))
                else:
                    files_data[file_hash] = [str(path)]

            except Exception as e:
                print(f"Ошибка с файлом {path}: {e}")

    print("Найденные дубликаты:\n")

    for paths in files_data.values():
        if len(paths) > 1:
            print("Группа:")
            for p in paths:
                print(p)
            print()