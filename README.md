# formals_languages_2

### Запуск:

*тесты* : `python3 test.py`

*проверка через консоль:* `python3 main.py`

При запуске сначала указывается количество правил n, на следующих n строчках идет описание КС-грамматики. В каждой из этих строк должно быть 2 слова через пробел: однобуквенная переменная и правило. Все переменные должны быть однобуквенными. Множество переменных и букв из языка должны не пересекаться. Итоговая KC-грамматика, обозначается, как `S`. Если она не будет использованна, то выведется ошибка. Пустой символ обознается, как `0`. Пробел не должен использьзоваться внутри грамматики.

Далее после n строк обозначения грамматики, n + 1 строкой идет паттерн, который проверяется на пренадлежность грамматики. На выходе будет `YES`, если паттерн пренадлежит грамматики. `NO` - в противном случае.
	
### Алгоритм:

Подробное описание алгоритма я опустил. Общая идея - строим итеративно списки ситуаций `Di`. На каждой итерации обновляем множество ситуаций посредством операции predict(спускании по дереву вывода) и опирации complete(движению вверх по дереву вывода), и обрабатывания пустого символа. Переход между `Di` происходит посредством операции scan(она проверяет, что по ситуации возжно перейти в другую ситуацию по букве паттерна.

### Тесты:

Я проверил на пренадлежность грамматики из 2 варианта из задания, скобочных последовательностей, арифметические выражения и палиндромы. Также сделал проверку на правильность ввода. 

*Тесты* в `test.py`
