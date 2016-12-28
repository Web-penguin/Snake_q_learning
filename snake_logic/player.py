import pygame

white_color = (255, 255, 255)
black_color = (0, 0, 0)
green_color = (0, 255, 0)

dest_dict = {0: [0, -1], 1: [0, 1], 2: [-1, 0], 3: [1, 0]}

class Snake_part(object):
	def __init__(self,pos,color = white_color):
		self.loc_x = pos[0]
		self.loc_y = pos[1]
		self.x = self.loc_x * 20
		self.y = self.loc_y * 20
		self.color = color

	def blit(self,screen):
		rect = pygame.Rect(self.x, self.y, 20, 20)
		pygame.draw.rect(screen, self.color, rect)

class Snake(object) :
	def __init__(self):
		self.x = 10
		self.y = 10
		self.lenght = 2
		self.tail = []
		self.dx = -1
		self.dy = 0
		self.head_color = green_color
		self.head = Snake_part((self.x, self.y), self.head_color)
		self.point = 0
		self.is_dead = False

	def blit(self,screen):
		for i in self.tail:
			i.blit(screen)
		self.head.blit(screen)

	def update(self, screen, dest):
		self.update_position(dest)
		self.blit(screen)
		self.check_dead()

	def check_dead(self):
		if self.x < 0 or self.x > 19 or self.y < 0 or self.y > 19:
			self.is_dead = True			
			

	def increase_lenght(self,value,point):
		self.lenght += value
		self.point += point
		
	def update_position(self, dest):

		# dest == 0: up
		# dest == 1: down
		# dest == 2: left
		# dest == 3: right
		
		self.dx = dest_dict[dest][0]
		self.dy = dest_dict[dest][1]

		self.tail.insert(0, Snake_part((self.x, self.y)))
		self.x += self.dx
		self.y += self.dy
		self.head.x, self.head.y = self.x * 20, self.y * 20
		if len(self.tail) > self.lenght:
			self.tail.pop()