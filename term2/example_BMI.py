from turtle import Turtle, done, Screen, textinput

#variables
t = Turtle()
s = Screen()
#design
s.bgpic('term2/Images/BMI.gif')

weight = int(textinput('What is your weight?', 'My weight is : '))
height = int(textinput('What is your height?', 'My height is : '))

height02 = height / 100
height03 = height02 * height02
bmi = weight / height03

if bmi >= 25 :
    s.bgpic('term2/Images/fat-guy.gif')
elif bmi <= 18.5 :
    s.bgpic('term2/Images/thin-guy.gif')
else:
    s.bgpic('term2/Images/normal-guy.gif')

done()