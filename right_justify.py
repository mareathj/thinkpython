# Right Justify
# right justify any string, such that last character is printed on col 70
# H@cker 08Jun2016

your_str = input('Please enter your string: ')
your_spc = int(input('how many spaces to \'right justify\': '))

def right_justify(string,spaces):
    string = ((spaces - len(string))* ' ') + string
    print(string)

right_justify(your_str,your_spc)
