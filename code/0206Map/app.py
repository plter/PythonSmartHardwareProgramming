# coding=utf-8
# NameValue KeyValue

m = {'name': '小云', 'age': 5}
m['gender'] = '女'


def get_value_from_map(key, map):
    # if key in map:
    #     return map[key]
    # else:
    #     return None
    return map[key] if key in map else None


print get_value_from_map('name', m)
