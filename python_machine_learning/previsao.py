# pip install sklearn scipy

from sklearn import tree

clf = tree.DecisionTreeClassifier()

# Dados : Altura, peso, numero sapato
x = [
    [181, 80, 44], [177, 70, 43], [160, 60, 38], [154, 54, 37],
    [166, 65, 40], [198, 90, 47], [175, 64, 39], [177, 70, 30],
    [159, 55, 37], [171, 75, 42], [181, 85, 43], [180, 105, 40]
]
# Resultado
y = [
    'Homem', 'Mulher', 'Mulher', 'Mulher',
    'Homem', 'Homem', 'Mulher', 'Mulher',
    'Homem', 'Homem', 'Homem', 'Mulher',
]
clf = clf.fit(x, y)
previsao = clf.predict([[156, 50, 32]])
print(previsao)
