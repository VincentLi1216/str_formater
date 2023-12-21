import pyperclip

replace_from = " "
replace_to = "_"


print("welcome to the auto format app")
print(f'The system will replace the input text from \"{replace_from}\" to \"{replace_to}\"\n')


_input = None

while _input != "q":
    _input = input("Please Enter the string or press \"q\" to quit: ")
    _input = _input.replace(replace_from, replace_to)
    print(_input)
    pyperclip.copy(_input)


