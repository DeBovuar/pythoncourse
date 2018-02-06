passMinutes = int(input())

minutes = passMinutes % 60
hours = passMinutes // 60 % 24

print(hours, minutes)
