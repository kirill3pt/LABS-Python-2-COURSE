from pathlib import Path
import subprocess

def run():
    source = input("Путь к папке с треками: ")
    count_input = input("Количество файлов в нарезке (Enter — все файлы): ")
    frame_input = input("Количество секунд на каждый файл (Enter — 10 секунд): ")
    log_input = input("Выводить лог? (y/n): ")
    extended_input = input("Использовать fade in/out? (y/n): ")
    destination_input = input("Имя выходного файла (Enter — mix.mp3): ")

    source_path = Path(source)

    if not destination_input:
        dest = source_path / "mix.mp3"
    else:
        dest = source_path / destination_input

    frame = int(frame_input) if frame_input else 10
    count = int(count_input) if count_input else None
    log = log_input.lower() == "y"
    extended = extended_input.lower() == "y"

    files = list(source_path.glob("*.mp3"))

    if count:
        files = files[:count]

    temp_files = []

    for i, file in enumerate(files, 1):
        temp_name = source_path / f"temp_{i}.mp3"
        temp_files.append(temp_name)

        if log:
            print(f"--- processing file {i}: {file.name}")

        cmd = [
            "ffmpeg",
            "-y",
            "-i", str(file),
            "-t", str(frame)
        ]

        if extended:
            cmd += ["-af", f"afade=t=in:ss=0:d=1,afade=t=out:st={frame-1}:d=1"]

        cmd.append(str(temp_name))

        subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    # создаём список для склейки
    list_file = source_path / "list.txt"
    with open(list_file, "w", encoding="utf-8") as f:
        for t in temp_files:
            f.write(f"file '{t.name}'\n")

    # объединяем фрагменты
    cmd = [
        "ffmpeg",
        "-y",
        "-f", "concat",
        "-safe", "0",
        "-i", str(list_file),
        "-c", "copy",
        str(dest)
    ]

    subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    # удаляем временные файлы
    for t in temp_files:
        t.unlink()
    list_file.unlink()

    if log:
        print("--- done!")
