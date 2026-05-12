import pandas as pd

def run():
    # ---------------- Загрузка данных ----------------
    url = "https://raw.githubusercontent.com/mledoze/countries/master/dist/countries.csv"
    df = pd.read_csv(url)

    print(df.columns)

    # ---------------- Предобработка ----------------
    df['area'] = pd.to_numeric(df['area'], errors='coerce')
    df['lat'] = df['latlng'].str.strip('[]').str.split(',').apply(lambda x: float(x[0]) if len(x)==2 else None)
    df['lng'] = df['latlng'].str.strip('[]').str.split(',').apply(lambda x: float(x[1]) if len(x)==2 else None)
    df['first_letter'] = df['name.common'].str[0]

    # ---------------- 1) 10 самых маленьких и больших стран по территории ----------------
    print("10 самых маленьких стран по территории:")
    print(df.nsmallest(10, 'area')[['name.common', 'area']])
    print("\n10 самых больших стран по территории:")
    print(df.nlargest(10, 'area')[['name.common', 'area']])

    """ ---------------- 2) 10 самых маленьких и больших стран по населению ----------------
    print("\n10 стран с наименьшим населением:")
    print(df.nsmallest(10, 'population')[['name.common', 'population']])
    print("\n10 стран с наибольшим населением:")
    print(df.nlargest(10, 'population')[['name.common', 'population']])"""

    # ---------------- 3) Франкоязычные страны ----------------
    fr_countries = df[df['languages'].str.contains("'fra'", na=False)]
    print("\nФранкоязычные страны:")
    print(fr_countries['name.common'].tolist())

    # ---------------- 4) Только островные государства ----------------
    island_countries = df[df['landlocked'] == False]
    print("\nОстровные государства:")
    print(island_countries['name.common'].tolist())

    # ---------------- 5) Страны в южном полушарии ----------------
    south_countries = df[df['lat'] < 0]
    print("\nСтраны в южном полушарии:")
    print(south_countries['name.common'].tolist())

    # ---------------- Группировка ----------------
    group_letter = df.groupby('first_letter').size()
    print("\nКоличество стран по первой букве:", group_letter)

    """population_bins = [0, 1e6, 1e7, 1e8, 1e9]
    df['population_group'] = pd.cut(df['population'], population_bins)
    group_population = df.groupby('population_group').size()
    print("\nКоличество стран по населению:", group_population)"""

    area_bins = [0, 1000, 10000, 100000, 1e7]
    df['area_group'] = pd.cut(df['area'], area_bins)
    group_area = df.groupby('area_group').size()
    print("\nКоличество стран по территории:", group_area)

    # ---------------- Сохранение выборочной информации ----------------
    columns_to_save = ['name.common', 'capital', 'area', 'currencies', 'lat', 'lng']
    df[columns_to_save].to_excel("countries_info.xlsx", index=False)
    print("\nВыборочная информация сохранена в файл countries_info.xlsx")

if __name__ == "__main__":
    run()