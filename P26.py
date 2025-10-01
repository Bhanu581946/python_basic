questions= ['Name', 'Favorite Color']
answers=['Basil', 'Blue']
for q, a in zip(questions, answers):
    print('What is your {0}?, It is {1}.'.format(q,a))