def decrypt_password(grid, password):
    decrypted_password = ''

    # Поворачиваем решетку и получаем символы из окошек
    for _ in range(4):
        for i in range(4):
            for j in range(4):
                # Если символ в решетке равен 'X', добавляем символ из пароля в расшифрованный пароль
                if grid[i][j] == 'X':
                    decrypted_password += password[i][j]

        # Поворачиваем решетку на 90 градусов по часовой стрелке
        grid = rotate_grid(grid)

    return decrypted_password


def rotate_grid(grid):
    rotated_grid = []

    # Создаем пустую решетку
    for _ in range(4):
        row = [''] * 4
        rotated_grid.append(row)

    # Поворачиваем решетку на 90 градусов по часовой стрелке
    for i in range(4):
        for j in range(4):
            rotated_grid[j][3 - i] = grid[i][j]

    return rotated_grid


# Ввод данных
grid = []
print("Введите шифровальную решетку:")
for _ in range(4):
    row = input().split()
    grid.append(row)

password = []
print("Введите зашифрованный пароль:")
for _ in range(4):
    row = list(input())
    password.append(row)

# Расшифровываем пароль
decrypted_password = decrypt_password(grid, password)

# Вывод результата
print("Расшифрованный пароль:", decrypted_password)
print("⢀⢀⢀⢀⢀⢀⢀⢀⢀⡴⠞⠉⢉⣭⣿⣿⠿⣳⣤⠴⠖⠛⣛⣿⣿⡷⠖⣶⣤⡀⢀⢀⢀")
print("⢀⢀⢀⢀⢀⢀⢀⣼⠁⢀⣶⢻⡟⠿⠋⣴⠿⢻⣧⡴⠟⠋⠿⠛⠠⠾⢛⣵⣿⢀⢀⢀⢀")
print("⣼⣿⡿⢶⣄⢀⢀⡇⢀⡿⠁⠈⢀⢀⣀⣉⣀⠘⣿⢀⢀⣀⣀⢀⢀⢀⠛⡹⠋⢀⢀⢀⢀")
print("⣭⣤⡈⢑⣼⣻⣿⣧⡌⠁⢀⢀⣴⠟⠋⠉⠉⠛⣿⣴⠟⠋⠙⠻⣦⡰⣞⠁⢀⣤⣦⣤⢀")
print("⢀⢀⣰⢫⣾⠋⣽⠟⠑⠛⢠⡟⠁⢀⢀⢀⢀⢀⠈⢻⡄⢀⢀⢀⠘⣷⡈⠻⣍⠤⢤⣌⣀")
print("⢀⡞⣡⡌⠁⢀⢀⢀⢀⢀⣿⠁⢀⢀⢀⢀⢀⢀⢀⢀⢿⡀⢀⢀⢀⠸⣇⢀⢾⣷⢤⣬⣉")
print("⡞⣼⣿⣤⣄⢀⢀⢀⢀⢸⡇⢀⢀⢀⢀⢀⢀⢀⢀⢀⢸⡇⢀⢀⢀⢀⣿⢀⠸⣿⣇⠈⠻")
print("⢰⣿⡿⢹⠃⢀⣠⠤⠶⣼⡇⢀⢀⢀⢀⢀⢀⢀⢀⢀⢸⡇⢀⢀⢀⢀⣿⢀⢀⣿⠛⡄⢀")
print("⠈⠉⠁⢀⢀⢀⡟⡀⢀⠈⡗⠲⠶⠦⢤⣤⣤⣄⣀⣀⣸⣧⣤⣤⠤⠤⣿⣀⡀⠉⣼⡇⢀")
print("⣿⣴⣴⡆⢀⢀⠻⣄⢀⢀⠡⢀⢀⢀⠈⠛⠋⢀⢀⢀⡈⢀⠻⠟⢀⢀⠋⠉⠙⢷⡿⡇⢀")
print("⣻⡿⠏⠁⢀⢀⢠⡟⢀⢀⢀⠣⡀⢀⢀⢀⢀⢀⢀⣄⢀⢀⢀⢀⢀⠈⢀⢀⣀⡾⣴⠃⢀")
print("⢿⠛⢀⢀⢀⢀⢸⠁⢀⢀⢀⢀⠈⠢⠄⣀⠠⠼⣁⢀⡱⠤⠤⠐⠁⢀⢀⣸⠋⢻⡟⢀⢀")
print("⠈⢧⣀⣤⣶⡄⠘⣆⢀⢀⢀⢀⢀⢀⢀⢀⣤⠖⠛⠻⣄⢀⢀⢀⢀⣠⡾⠋⢀⡞⢀⢀⢀")
print("⢀⢀⠻⣿⣿⡇⢀⠈⠓⢦⣤⣤⣤⡤⠞⠉⢀⢀⢀⢀⠈⠛⠒⠚⢩⡅⣠⡴⠋⢀⢀⢀⢀")
print("⢀⢀⢀⠈⠻⢧⣀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⠐⣻⠿⠋⢀⢀⢀⢀⢀⢀")
print("⢀⢀⢀⢀⢀⢀⠉⠓⠶⣤⣄⣀⡀⢀⢀⢀⢀⢀⢀⣀⣠⡴⠖⠋⠁⢀⢀⢀⢀⢀⢀⢀⢀⢀")