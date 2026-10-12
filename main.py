# getting data from a text box
from pyscript import display, document 


def get_name(e):
    document.getElementById('div1').innerHTML = ' '
    f_name = document.getElementById('fname').value
    l_name = document.getElementById('lname').value
    book_clubms = ['athena', 'bela', 'lindsay']
    book_clubms1 = ['alfaro', 'allas', 'esguerra']

    name_checker = f_name in book_clubms # true(1) or false(0)
    name_checker = l_name in book_clubms1 # true(1) or false(0)

    display_message = ('Sorry, your name is not in the list', f'{l_name} {f_name} is in the list')
    display(display_message[name_checker], target="div1")