import unittest
from Earley import Earley


def construct(rules):
    grammar = {}
    rules = rules.split("\n")
    for input_str in rules:
        input_str = input_str.split()
        if len(input_str) != 2:
            raise Exception("Wrong arguments count")
        variable = input_str[0]
        expression = input_str[1]
        if len(variable) != 1:
            raise Exception("Wrong variable name")
        if grammar.get(variable) is None:
            grammar[variable] = {expression}
        else:
            grammar[variable].add(expression)
    if grammar.get('S') is None:
        raise Exception("Haven't got S")
    grammar['S0'] = {'S'}
    return grammar


def earley(rules, pattern):
    grammer = construct(rules)
    my_class = Earley(pattern, grammer)
    return my_class.earley()


class MyTestCase(unittest.TestCase):
    def test1(self):
        self.assertEqual(earley("S Sa\n"
                                "D cD\n"
                                "S SSb\n"
                                "S C\n"
                                "C Dd\n"
                                "D 0",
                                "cccdcdb"),
                         "YES")

    def test2(self):
        self.assertEqual(earley("S Sa\n"
                                "D cD\n"
                                "S SSb\n"
                                "S C\n"
                                "C Dd\n"
                                "D 0",
                                "cdacdab"),
                         "YES")

    def test3(self):
        self.assertEqual(earley("S Sa\n"
                                "D cD\n"
                                "S SSb\n"
                                "S C\n"
                                "C Dd\n"
                                "D 0",
                                "ccccccccaaaa"),
                         "NO")

    def test4(self):
        self.assertEqual(earley("S 0\n"
                                "S S(S)",
                                "(())(()())()"),
                         "YES")

    def test5(self):
        self.assertEqual(earley("S 0\n"
                                "S S(S)",
                                "(())))))(()())))))"),
                         "NO")

    def test6(self):
        self.assertEqual(earley("S a\n"
                                "S b\n"
                                "S S+S\n"
                                "S S*\n"
                                "S (S)\n"
                                "S 0",
                                "a+a+b+(a+b)*"),
                         "YES")

    def test7(self):
        self.assertEqual(earley("S a\n"
                                "S b\n"
                                "S S+S\n"
                                "S S*\n"
                                "S (S)\n"
                                "S 0",
                                "a+a+ba+(a++*+b)*"),
                         "NO")

    def test8(self):
        self.assertEqual(earley("S 0\n"
                                "S a\n"
                                "S b\n"
                                "S aSa\n"
                                "S bSb",
                                "aabbaa"),
                         "YES")

    def test9(self):
        self.assertEqual(earley("S 0\n"
                                "S a\n"
                                "S b\n"
                                "S aSa\n"
                                "S bSb",
                                "aaaaaaabbaa"),
                         "NO")

    def test10(self):
        with self.assertRaises(Exception) as context:
            earley("A 0\n"
                   "B abc", "dzfg")
        self.assertEqual("Haven't got S", str(context.exception))

    def test11(self):
        with self.assertRaises(Exception) as context:
            earley("HELLO\n"
                   "B abc", "dzfg")
        self.assertEqual("Wrong arguments count", str(context.exception))

    def test12(self):
        with self.assertRaises(Exception) as context:
            earley("AOAOA q\n"
                   "S 0", "dzfg")
        self.assertEqual("Wrong variable name", str(context.exception))


if __name__ == '__main__':
    unittest.main()
