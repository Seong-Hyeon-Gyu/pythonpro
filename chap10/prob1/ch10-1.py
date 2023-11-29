class Player:
	def blast(self, enemy):
		print("\nThe player blasts an enemy.\n\nThe alien gasps and says, 'Oh, this is it. This is the big one.\nYes, it's getting dark now. Tell my 1.6 million larvae that I loved them...")
		enemy.die()
class Alien:
	def die(self):
		print("Good-bye, cruel universe.'")
print("\t\tDeath of an Alien")
hero = Player()
invader = Alien()
hero.blast(invader)
