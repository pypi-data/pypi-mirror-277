from .data_structures import *
from  .search_algorythms import *

data1 = text1.split('abracadabrabibidi')
data_structures_dict = dict([(x.split('\n')[1].replace("# ",''),x) for x in data1])
data2 = text2.split('abracadabrabibidi')
search_algorythms_dict = dict([(x.split('\n')[1].replace("# ",''),x) for x in data1])

themes = {
        'Структуры данных': list(data_structures_dict.keys()),
        'Алгоритмы сортировки': list(search_algorythms_dict.keys())
              }

def description(dict_to_show = themes, show_only_keys:bool = True):
    if dict_to_show == themes:
        show_only_keys = False
    text = ""
    for key in dict_to_show.keys():
        text += f'{key}'
        if not show_only_keys:
            text +=': '
            for f in dict_to_show[key]:
                text += f'{f}; '
        text += '\n'
    if dict_to_show == themes:
        print(text)
    else:
        return text

def enable_ppc():
    return '''    import pyperclip

    #Делаем функцию которая принимает переменную text
    def write(name):
        pyperclip.copy(name) #Копирует в буфер обмена информацию
        pyperclip.paste()'''

def data_structures(key=None):
    if key == None:
        print(description(data_structures_dict))
    else:
        try:
            return data_structures_dict[key]
        except:
            print('Ошибка поиска. Структура данных должна быть среди этих:\n')
            print(description(data_structures_dict))
            
def search_algorythms(key=None):
    if key == None:
        print(description(search_algorythms_dict))
    else:
        try:
            return search_algorythms_dict[key]
        except:
            print('Ошибка поиска. Алгоритм поиска должен быть среди этих:\n')
            print(description(search_algorythms_dict))
description()