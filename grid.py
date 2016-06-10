# Grid
# prints the grid
# H@cker 9June2016


def print_row(r):
    print(('+', '-'*4) * r)

def print_column():
    print('|', ' '*4, '|', ' '*4, '|')
def print_height():
    print_column()
    print_column()
    print_column()
    print_column()

print_row()
print_height()
print_row()
print_height()
print_row()
