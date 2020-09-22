from matplotlib import pyplot as plt
from collections import Counter

users = [1, 2, 3, 4, 5, 6, 7, 8]
friends = [5, 10]

plt.bar([2013, 2014], users, 0.2)
plt.xticks(friends)
plt.ylabel('#amigos')
plt.axis([5, 10, 5, 8])
plt.show()


salario = [910, 1000, 2300, 800, 600]
exp = lambda grade: grade // 6 * 10

histogram = Counter (exp(salario) for salario in salarios)

plt.bar([
    totals for totals in histogram.keys()
], histogram.values(), 10)

plt.axis([-10, 200,0, 8])
plt.xticks('# Salario total')
plt.show()


pagantes = ['Clayton', 'José', 'Mariana', 'Celso', 'Soarez']

nao_pagantes = [1, 3, 4, 5]
xs = [i for i, _ in enumerate(pagantes)]

plt.bar(xs, nao_pagantes)
plt.xlabel('não pagantes')
plt.ylabel('Pagantes')
plt.xticks([i for i, _ in enumerate(pagantes)], pagantes)
plt.show()
