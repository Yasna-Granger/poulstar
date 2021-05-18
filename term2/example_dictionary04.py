Contacs = {
    'Yasna' : '09020027993',
    'Setia' : '09112342131'
}

number = int(input('what do you want to do?  1)add a number  2)delete a number  3)change sth : '))

#add

if number == 1:
    name  = input('Enter the name of the person you want to add :')
    phone = input('Enter the number of the person you want to add :')
    Contacs[name] = phone
    print(Contacs)

#delete

if number == 2:
    print(Contacs)
    deleting = input('which of the contacts above you want to delete? : ')
    Contacs.pop(deleting)
    print(Contacs)

#change

if number == 3:
    change = input('which of the contacts you want to delete? : ')
    phone_num = input('what is the numer? : ')
    Contacs[change] = phone_num
    print(Contacs)