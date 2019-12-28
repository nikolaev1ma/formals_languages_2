from Earley import Earley

def initialization_ks_grammar():
    n = int(input()) # колво правил
    grammar = {}
    for i in range(n):
        input_str = input().split()
        if len(input_str) != 2:
            raise Exception
        variable = input_str[0]
        expression = input_str[1]
        if len(variable) != 1:
            raise Exception
        if grammar.get(variable) is None:
            grammar[variable] = {expression}
        else:
            grammar[variable].add(expression)
    if grammar.get('S') is None:
        raise Exception
    grammar['S0'] = {'S'}
    return grammar


if __name__ == '__main__':
    grammer = initialization_ks_grammar()
    pattern = input()
    my_class = Earley(pattern, grammer)
    print(my_class.earley())


