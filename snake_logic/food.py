import pygame
import random

yellow_color = (255, 255, 0)

class Food_piece(object):
	def __init__(self,pos,color = yellow_color):
		self.loc_x = pos[0]
		self.loc_y = pos[1]
		self.x = self.loc_x * 20
		self.y = self.loc_y * 20
		self.color = color
		self.imgX = int((self.loc_x + 0.5) * 20)
		self.imgY = int((self.loc_y + 0.5) * 20)

	def blit(self,screen):
		pygame.draw.circle(screen, self.color, (self.imgX, self.imgY), 8)

class Food(object):
	def __init__(self):
		self.food = list()

	def random_pos(self,snake):
		run = True

		while run:
			x, y = random.randint(0, 19),random.randint(0, 19)
			while (x * y == 1):
				x, y = random.randint(0, 19) ,random.randint(0, 19)

			run = False
			for i in snake.tail :
				if i.loc_x == x and i.loc_y == y :
					run = True
			if x == snake.x and y == snake.y :
				run = True
			for i in self.food :
				if i.loc_x == x and i.loc_y == y :
					run = True
		return x, y


	def update(self, screen, snake):
		has_ate = False
		if len(self.food) == 0:
			x, y = self.random_pos(snake)
			f_piece = Food_piece((x, y))
			self.food.append(f_piece)

		for f_piece in self.food :
			if f_piece.loc_x == snake.x and f_piece.loc_y == snake.y:
				has_ate = True
				snake.increase_lenght(1, 1)
				self.food.remove(f_piece)
			f_piece.blit(screen)
		return has_ate
