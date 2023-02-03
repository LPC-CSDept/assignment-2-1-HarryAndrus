def main():
    num_males = int(input('How many Males are there ? '))
    num_females = int(input('How many females are there? '))
    total = (num_males + num_females)
    perc_males = num_males / float(total) * 100
    perc_females = num_females / float(total) * 100
    
    print('The total number of students: \t',total,)
    print('The number of males and females: ',num_males,num_females)
    print('The percentage of males: ', format(perc_males, '.2f') + '%', format(perc_females, '.2f') + '%')



if __name__ == '__main__':
    main()

