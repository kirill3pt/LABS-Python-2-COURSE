from pathlib import Path

def second():
    folder = input("Введите путь к директории: ")
    files_data = {}
    for path in Path(folder).rglob("*"):
        if path.is_file():
            try:
                content = path.read_bytes()
    
                if content in files_data:
                    files_data[content].append(str(path))
                else:
                    files_data[content] = [str(path)]
            except:
                pass
    
    print("Найденные дубликаты:\n")
    for paths in files_data.values():
        if len(paths) > 1:
            print("Группа:")
            for p in paths:
                print(p)
            print()