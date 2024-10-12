# TODO Найдите количество книг, которое можно разместить на дискете
V_disk = 1.44 # объем дискеты в Мб
st_in_book = 100 # страниц в книге
st_na_str = 50 # строк на странице
sim_v_stroke = 25 # символов в строке
bt_v_sim =4 # 1 символ в байтах
bt_v_Mb = 1048576 # байт в мегабайте
V_knigi = st_in_book * st_na_str * sim_v_stroke * bt_v_sim
num_books = int((V_disk * bt_v_Mb // V_knigi))
print("Количество книг, помещающихся на дискету:", num_books)


