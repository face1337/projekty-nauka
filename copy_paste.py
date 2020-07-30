import pyperclip

print('Please enter what you want to copy to your clipboard')
copy_this = input()

pyperclip.copy(copy_this)

copied_value = pyperclip.paste()
print('The value copied to the clipboard is :' + str(copied_value))
