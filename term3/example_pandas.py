import pandas

df = pandas.DataFrame(columns=['Name', 'Family', 'Age', 'E-mail'])

df.loc[0] = ['Yasna', 'Kamran', 14, 'yangelixx85@yahoo.com']
df.loc[1] = ['Setia', 'Kamran', 7, 'setiakamran@gmail.com']
df.loc[2] = ['Sana', 'Mirbark-kar', 14, 'SanaMirbark-Kar@yahoo.com']

df['Age'] =(df['Age']) + 1
df['Full_Name'] = df['Name'] + " " + df['Family']

print(df)