def main():
    num_males = int(input('How many Males are there ? '))
    num_females = int(input('How many females are there? '))
    total = (num_males + num_females)
    perc_males = num_males / float(total) * 100
    perc_females = num_females / float(total) * 100
    
    print('There are ',total,'Students:')
    print('Percentage of Males: ', format(perc_males, '.2f',))
    print('Percentage of Females: ', format(perc_females, '.2f'))


if __name__ == '__main__':
    main()

