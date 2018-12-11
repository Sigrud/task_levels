# Вывести последнюю букву в слове
word = 'Архангельск'
last_char = list(word).pop()
print(last_char)

print('==========')

# Вывести количество букв а в слове
word = 'Архангельск'
count_chars = len(list(word))
print(count_chars)

print('==========')

# Вывести количество гласных букв в слове
word = 'Архангельск'
a_list = ['а', 'е', 'о', 'у', 'ы', 'и', 'ё', 'э', 'я', 'ю']
sum_chars = 0
for char in word.lower():
	if char in a_list:
		sum_chars += 1
print(sum_chars)

print('==========')

# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'
words = sentence.split()
print(len(words))

print('==========')

# Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'
words = sentence.split()
i = 0
while i < len(words):
	print(words[i][0])
	i = i + 1

print('==========')

# Вывести усреднённую длину слова.
sentence = 'Мы приехали в гости'
words = sentence.split()
a = (len(words))
c = sentence.replace(" ", "")
print(len(c)/a)