import codecs
import json

f = codecs.open("data_structures.ipynb", 'r',encoding='UTF-8')
source = f.read()
y = json.loads(source)
data_structures_dict = dict([((x['source'][1]).replace("\n",'').replace("# ",''),("".join([x2 for x2 in x['source']])).replace("\'\'\'",'')) for x in y['cells']])
f = codecs.open("search_algorythms.ipynb", 'r',encoding='UTF-8')
source = f.read()
y = json.loads(source)
search_algorythms_dict = dict([((x['source'][1]).replace("\n",'').replace("# ",''),("".join([x2 for x2 in x['source']])).replace("\'\'\'",'')) for x in y['cells']])


def description(dict_to_show, show_only_keys:bool = True):
    text = ""
    for key in dict_to_show.keys():
        text += f'{key}'
        if not show_only_keys:
            text +=': '
            for f in dict_to_show[key]:
                text += f'{f}; '
        text += '\n'
    return text


def data_structures(key=None):
    if key == None:
        print(description(data_structures_dict))
    else:
        try:
            print(data_structures_dict[key])
        except:
            print('Ошибка поиска. Структура данных должна быть среди этих:\n')
            print(description(search_algorythms_dict))
            
def search_algorythms(key=None):
    if key == None:
        print(description(search_algorythms_dict))
    else:
        try:
            print(search_algorythms_dict[key])
        except:
            print('Ошибка поиска. Алгоритм поиска должен быть среди этих:\n')
            print(description(search_algorythms_dict))