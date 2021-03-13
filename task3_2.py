def person(**kwargs):
    return kwargs

print(person(
    name=input('Имя - '),
    lname=input('Фамилия - '),
    bday=input('дата рождения - '),
    city=input('город - '),
    email=input('эл.почта - '),
    phone=input('телефон - ')
))

#на проверку