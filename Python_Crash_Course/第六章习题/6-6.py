#调查
name = ['Tom', 'Tack', 'Roma', 'Ruty', 'Pater']
name_dictionary = {'Tom': 'accpet', 'Tack': 'accpt'}
for name in name:
    if name in name_dictionary:
        print('Thank you.')
    else:
        print('Please particpate in the survey')