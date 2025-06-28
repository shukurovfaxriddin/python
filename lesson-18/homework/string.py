df = pd.read_csv(r'D:\IT\Maab\python\stackoverflow_qa.csv', quotechar='"')
# 1
a=df['creationdate'] < '2014-01-01'
df[a]
# 2
a=df['score'] > 50
df[a]
# 3
df[(df['score'] > 50) & (df['score'] < 100)]
# 4
df[df['ans_name'] == 'Scott Boston']
# 5
users=['Demitri','Mike Pennington','Jubbles','Jim','DSM']
df[df['ans_name'].isin(users)]
# 6
a=((df['creationdate'] > '2014-3-01') & (df['creationdate'] <  '2014-10-31'))
b=((df['ans_name']=='Unutbu')&(df['score'] < 5))
df[a&b]
# 7
a=((df['score'] > 5) & (df['score'] <  10))
b=df['ans_rep']>10000
df[a&b]
# 8

df[df['ans_name']== 'Scott Boston']
df = pd.read_csv(r'D:\IT\Maab\python\titanic.csv', quotechar='"')
# 1
df[(df['Sex'] == 'female')&( df['Pclass'] == 1) & ((df['Age']>20) &(df['Age']<30))]
# 2
df[df['Fare'] > 100]
# 3
df[(df['Survived'] == 1)&(df['SibSp']==0)&(df['Parch']==0)]
# 4
df[(df['Embarked'] == 'C')&(df['Fare']>50)]
# 5
df[(df['SibSp']==0)&(df['Parch']==0)]
# 6

df[(df['Survived'] == 0)&(df['Age']<=15)]
# 7
df[df['Cabin'].notna() & (df['Fare'] > 200)]
# 8
a=df['PassengerId'].min()
b=df['PassengerId'].max()
list1=[]
for i in range(a,b+1):     
    if i % 2 != 0:
        list1.append(i)

df[df['PassengerId'].isin(list1)]
# 9
unique_tickets = df['Ticket'].value_counts()
unique_tickets = unique_tickets[unique_tickets == 1].index

df[df['Ticket'].isin(unique_tickets)]
# 10
df[df['Name'].str.contains('Miss') & (df['Pclass'] == 1)]
