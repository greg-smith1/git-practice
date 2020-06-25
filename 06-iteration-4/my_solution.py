def print_all(x):
    for i in x:
        if not isinstance(i, list):
            print(i)
        else:
            for a in i:
                if not isinstance(a, list):
                    print(a)
                else:
                    for b in a:
                        print(b)

#print_all([1, 2, ['jeff', 'tom'], [42, ['billy', 'jason']]])