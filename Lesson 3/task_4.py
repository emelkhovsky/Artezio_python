from lxml import etree

def pro_recurtion(a_value, d1, depth_value):
    print(a_value.tag)
    global max_depth
    if depth_value > max_depth:
        max_depth = depth_value
    d1['name'] = a_value.tag
    d1['children'] = []
    if len(a_value) > 0:
        depth_value += 1
        for el in a_value.getchildren():
            d2 = {}
            rez = pro_recurtion(el, d2, depth_value)
            d1['children'].append(rez[0])
    return d1, max_depth


def processing(a):
    new_dict = {}
    depth_value = 0
    a = etree.XML(a)
    return pro_recurtion(a, new_dict, depth_value)

a = '<root><element1 /><element2 /><element3><element4 /></element3></root>'
max_depth = 0
rezult = processing(a)
print('REZULT --- > ', rezult) #({'name': 'root', 'children': [{'name': 'element1', 'children': []}, {'name': 'element2', 'children': []}, {'name': 'element3', 'children': [{'name': 'element4', 'children': []}]}]}, 2)
