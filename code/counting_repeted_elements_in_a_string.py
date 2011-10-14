
def frequency():
    count = {}
    lst = raw_input('enter sentence: ').split()
    while lst != ['q']:
        for element in lst:
            count[element] = count.get(element, 0) + 1
        lst = raw_input('sentence: ').split()

    for element in count:
        print element + ' occurs ' + str(count[element]) + ' times'


frequency()
