def print_row(c):
        for j in range(c):
            print('+','-'*4,end=' ')
            
            
def do_times(f1,f2,n,b,c):
	for i in range(n):
		f1(c)
		f2(b,c)

def print_column(c):
        for j in range(c):
            print('|',end=' '*6)


def column(b,c):
	for j in range(b):
		print_column(c)
		print('')

		
do_times(print_row,column,3,3,3)
print('+','-'*4,end=' ')
