# formals_languages_2

Запуск:

тесты:
	
	python3 test.py

проверка через консоль:

	python3 main.py

При запуске сначала указывается колво правил n
на следующих n строчках идет описание кс-грамматики. В каждой из этих строк должно быть 2 строки через пробел: однобуквенная переменная и правило. Множество переменных и буквы из языка должны не пересекаться. Итоговая KC-грамматика, обозначается, как S. Если она не будет использованна, то выведется ошибка. пустой символ обознается, как '0'. Пробел не должен использьзоваться внутри грамматики.

Далее после n строк обозначения грамматики, n + 1 строкой идет паттерн, который проверяется на пренадлежность грамматики. На выходе будет "YES", если паттерн пренадлежит грамматики. "NO" - в противном случае.

Алгоритм:

Подробное описание алгоритма я опустил. Общая идея - строим итеративно списки ситуаций Di. На каждой итерации обновляем множество ситуаций постредством операции predict(спускании по дереву вывода) и опирации complete(движению вверх по дереву вывода) и обрабатывании пустого символа. Переход между Di происходит посредством операции scan(она проверяет, что по ситуации возжно перейти по букве паттерна.

Тесты:

Я проверил на пренадлежность грамматики из 2 варианта из задания, на скобочные последовательности, арифметические выражения и палиндромы. Также сделал проверку на правильность ввода. 
Тесты в test.py
