class Earley:
    def __init__(self, pattern, grammar):
        self.pattern = pattern  # слова, которое мы проверяем на пренадлежность грамматике
        self.grammar = grammar  # грамматику будем хранить, как словарь сетов, где ключ словаря это переменная,
                                # а значение - сет множество правил для данной переменной

        self.D = []   # массив множеств Di
                      # элемент Dj это ситуации [A, α.β,i, point] в j-м списке ситуаций Dj равносильно тому, что
                      # ∃δ∈Σ∪N:((S′⇒∗w0…wi−1Aδ)∧A⇒∗wi…wj−1),
                      # point - место, где стоит точка в "α.β".

    # способ считать следующую букву
    # j - норер Dj, flag - проверка, что Dj обновился
    def scan(self, j, flag):
        if j == 0:
            flag = True
            return flag
        for situation in self.D[j - 1]:
            point_position = situation[3]
            if point_position < len(situation[1]) - 1:
                next_symbol = situation[1][point_position + 1]
                if next_symbol == self.pattern[j - 1]:
                    # нашли букву wi из слова
                    flag = True
                    # меняем местами wi и .
                    a = ''
                    if point_position != 0:
                        a = situation[1][:point_position]
                    b = ''
                    if point_position != len(situation[1]) - 2:
                        b = situation[1][point_position + 2:]
                    new_str = a + next_symbol + '.' + b
                    self.D[j].append([situation[0], new_str, situation[2], situation[3] + 1])
        return flag

    # тоже самое, что и scan, только идет переход не из Di в Di + 1, а Di в Di
    def zero_processing(self, j, flag):
        for situation in self.D[j]:
            point_position = situation[3]  # положение точки
            if point_position < len(situation[1]) - 1:
                next_symbol = situation[1][point_position + 1]
                if next_symbol == '0':
                    a = ''
                    if point_position != 0:
                        a = situation[1][:point_position]
                    b = ''
                    if point_position != len(situation[1]) - 2:
                        b = situation[1][point_position + 2:]
                    new_str = a + next_symbol + '.' + b
                    value = [situation[0], new_str, situation[2], situation[3] + 1]
                    if self.D[j].count(value) == 0:
                        self.D[j].append(value)
                        flag = True
        return flag

    # способ перейти вверх по дереву вывода
    # аналогично опеределены j и flag
    def complete(self, j, flag):
        for situation_j in self.D[j]:
            point_position_j = situation_j[3]  # положение точки
            if point_position_j == len(situation_j[1]) - 1:
                i = situation_j[2]
                for situation_i in self.D[i]:
                    # проходимся по Di и ищем подходящую нам ситуацию
                    point_position_i = situation_i[3]
                    if point_position_i < len(situation_i[1]) - 1:
                        next_symbol = situation_i[1][point_position_i + 1]
                        if next_symbol == situation_j[0]:
                            a = ''
                            if point_position_i != 0:
                                a = situation_i[1][:point_position_i]
                            b = ''
                            if point_position_i != len(situation_i[1]) - 2:
                                b = situation_i[1][point_position_i + 2:]
                            new_str = a + next_symbol + '.' + b
                            value = [situation_i[0], new_str, situation_i[2], situation_i[3] + 1]
                            # проверка, что у нас не повторяется ситуация
                            if self.D[j].count(value) == 0:
                                self.D[j].append(value)
                                flag = True
        return flag

    # способ перейти вниз по дереву вывода
    # аналогично опеределены j и flag
    def predict(self, j, flag):
        for situation in self.D[j]:
            point_position = situation[3]  # положение точки
            if point_position < len(situation[1]) - 1:
                next_symbol = situation[1][point_position + 1]
                # проходимся по правилам грамматики и смотрим нужное нам правило вывода
                if self.grammar.get(next_symbol) is not None:
                    for expression in self.grammar[next_symbol]:
                        value = [next_symbol, '.' + expression, j, 0]
                        if self.D[j].count(value) == 0:
                            flag = True
                            self.D[j].append([next_symbol, '.' + expression, j, 0])
        return flag

    # сам алгоритм
    def earley(self):
        # инициализируем
        for i in range(len(self.pattern) + 1):
            self.D.append([])
        # в D0 добавляем нужное первое правило
        self.D[0] = ([['S0', '.S', 0, 0]])
        # строим посдедовательно Di
        for i in range(len(self.pattern) + 1):
            flag = False
            flag = self.scan(i, flag)
            if flag is False:
                # мы ненашли следующую букву, тоесть Di теперь бует польностью пустым - слово не выводимо
                return "NO"
            while True:
                # делаем операции прохода по дереву, пока Di как-то изменяется
                flag = False
                flag = self.complete(i, flag)
                flag = self.predict(i, flag)
                flag = self.zero_processing(i, flag)
                if flag is False:
                    break
        # ищем финальное правило S' -> S. , 0
        for situation in self.D[len(self.pattern)]:
            if situation[0] == 'S0' and situation[1] == 'S.' and situation[2] == 0:
                return "YES"
        return "NO"
