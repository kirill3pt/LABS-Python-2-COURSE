import os
import struct

GENRE = 17  # номер жанра


def read_tag(filename, track_number, show_dump):
    with open(filename, "rb+") as f:

        # переход к последним 128 байтам
        f.seek(-128, 2)
        tag_data = f.read(128)

        # проверка наличия ID3v1
        if tag_data[:3] != b"TAG":
            print("ID3v1 тег не найден")
            return

        # ID3v1.1
        tag, title, artist, album, year, comment, zero, track, genre = struct.unpack(
            "3s30s30s30s4s28sBBB",
            tag_data
        )

        # декодирование строк
        title = title.decode("cp1251", errors="ignore").strip("\x00 ")
        artist = artist.decode("cp1251", errors="ignore").strip("\x00 ")
        album = album.decode("cp1251", errors="ignore").strip("\x00 ")

        # вывод информации
        print(f"[{artist}] - [{title}] - [{album}]")

        # hex dump
        if show_dump:
            print("\nHEX DUMP:")
            print(tag_data.hex(" "))
            print()

        # --- автоматическая установка номера трека ---
        if track == 0:
            track = track_number

        # --- автоматическая установка жанра ---
        if genre == 255:
            genre = GENRE

        # запись обратно
        new_tag = struct.pack(
            "3s30s30s30s4s28sBBB",
            tag,
            title.encode("cp1251").ljust(30, b"\x00"),
            artist.encode("cp1251").ljust(30, b"\x00"),
            album.encode("cp1251").ljust(30, b"\x00"),
            year,
            comment,
            0,
            track,
            genre
        )

        # возврат к тегу
        f.seek(-128, 2)
        f.write(new_tag)


def run():
    folder = input("Путь к папке: ")
    dump = input("Показать hex dump? (y/n): ").lower() == "y"

    track_number = 1

    for file in os.listdir(folder):

        if file.lower().endswith(".mp3"):

            path = os.path.join(folder, file)

            print(f"\nФайл: {file}")

            try:
                read_tag(path, track_number, dump)
                track_number += 1

            except Exception as e:
                print("Ошибка:", e)