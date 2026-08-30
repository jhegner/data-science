from matplotlib import pyplot as plt

movies = ["Annie Hall", "Ben-Hur", "Casablanca", "Ghnadi", "West Side Story"]
num_oscars = [5, 11, 3, 8, 10]

# plote as barras com coordenadas x a esquerda [0, 1, 2, 3, 4], alturas [num_oscars]
plt.bar(range(len(movies)), num_oscars)

plt.title("Meus filmes favoritos")
plt.ylabel("# of Academy Awards") # rotulo do eixo y

# rotulo do eixo x com os nomes dos filmes
plt.xticks(range(len(movies)), movies)

plt.show()