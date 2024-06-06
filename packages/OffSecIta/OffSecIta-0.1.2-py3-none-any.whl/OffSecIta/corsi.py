class Corso:

	def __init__(self, nome, durata, link):
		self.nome = nome
		self.durata = durata
		self.link = link


	def __repr__(self):
		return f"{self.nome} [{self.durata} ORE] ({self.link})"

corsi = [
	
	Corso("Corso Hacking Etico", 60, "https://www.youtube.com/watch?v=io5heKn6VwU&list=PLKZZXjqZrqQtKGgJuAYhzYczf1KIdswvO"),
	Corso("Corso Linux", 15, "https://www.youtube.com/watch?v=qcX89gkdlYs&list=PLKZZXjqZrqQvfAhgY7Nit5ynpK3kN_3tx"),
	Corso("Corso Personalizzazione Linux", 3, "https://www.youtube.com/watch?v=zYgN2Ty16RA&list=PLKZZXjqZrqQslOV4EyEl40ZPxo7bpFHQE"),
	Corso("Corso Python Offensive", 50, "https://www.youtube.com/watch?v=Q6OCBq2nyzs&list=PLKZZXjqZrqQu7qZkgSsdU3lRpR7oISMXh")
]


def lista_corsi():
	for corso in corsi:
		print(corso)

	
def cerca_corso_by_nome(nome):
	for corso in corsi:
		if corso.nome == nome:
			return corso

	return None		
