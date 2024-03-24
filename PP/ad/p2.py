
marker = "*" # символ
thickness = 5 # толщина фигуры

# отображение фигуры
print(" "*(thickness-1) + marker)
for i in range(thickness-2):
    print(" "*(thickness-i-2) + marker + " "*(2*i+1) + marker)
print(marker*(2*thickness-1))
