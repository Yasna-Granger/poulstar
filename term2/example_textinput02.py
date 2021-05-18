from turtle import Turtle,done,textinput

t = Turtle()
x = textinput('Enter whether you want ', 'My texts: ')
file = open('C:\\Users\\G.V Shop\\PycharmProjects\\Luna_Lovegood\\term2\\texts\\text03.txt', 'a')
file.write(x)
file.close()
done()