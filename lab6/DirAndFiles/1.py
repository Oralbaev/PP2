import os
путь = os.getcwd() #сохраняет путь в переменную
print("only directories:", [x for x in os.listdir(путь) if os.path.isdir(x)])
print("only files:", [x for x in os.listdir(путь) if os.path.isfile(x)]) 
print("all dir and files:", os.listdir(путь))