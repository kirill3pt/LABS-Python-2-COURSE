def practise():
    addresses = ["www.avito.ru", "dl.donnu.ru", "www.ozon.ru", "metanit.com"]
    prom_addresses = [
        "http://" + adress if adress.startswith("www") 
        else adress for adress in addresses] #проверяем - добавляем http:// 
                                             #если адрес начинается с... иначе - оставляем 
    final_addresses = [
        adress if adress.endswith(".com") 
        else adress + ".com" for adress in prom_addresses] #проверяем - добавляем .com если 
                                                           #заканчивается не на .com, иначе - оставляем
    print("list: {}".format(final_addresses))
    #prom_addresses - промежуточный список, где адреса проверяются первый раз на www
    #final_addresses - финальный список, где адреса соотв. 1 условию и проверяются на 2