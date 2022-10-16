src = not False and True or False and not True

'''
result = True and True or False and False - избавились от отрицаний not
result = True or False - избавились от логического "И"
result = True - конечный результат после избавления от логического "ИЛИ"
'''
# result = False or True or False

result = True  # TODO подставить результат выражения

print(src == result)
