from pathlib import Path
import shutil
import time

def run():
    source = input("Путь к папке: ")
    days = int(input("для папки archive - на сколько дней отличается: "))
    size = int(input("для папки small - на сколько < (байт): "))

    source_path = Path(source)
    now = time.time()

    archive_created = False
    small_created = False

    for file in source_path.iterdir():
        if file.name in ["Archive", "Small"]:
            continue
    
        if file.is_file():
            try:
                stat = file.stat()
                file_age_days = (now - stat.st_mtime) / 86400
                file_size = stat.st_size
                if file_age_days > days:
                    archive_dir = source_path / "Archive"
                    if not archive_created:
                        archive_dir.mkdir(exist_ok=True)
                        archive_created = True
                    print(f"[ARCHIVE] {file} -> {archive_dir}")
                    shutil.move(str(file), archive_dir / file.name)
                elif file_size < size:
                    small_dir = source_path / "Small"
                    if not small_created:
                        small_dir.mkdir(exist_ok=True)
                        small_created = True
    
                    print(f"[SMALL] {file} -> {small_dir}")
                    shutil.move(str(file), small_dir / file.name)
    
            except Exception as e:
                print(f"Ошибка с файлом {file}: {e}")

    print("Готово.")