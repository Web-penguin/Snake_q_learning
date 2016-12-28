import pygame
import player
import food
import random

width = 400
height = 400
white_color = (255, 255, 255)
black_color = (0, 0, 0)

class Game_Window(object):
	def __init__(self):
		pygame.init()

		self.clock = pygame.time.Clock()

		food_x, food_y = random.randint(1,18), random.randint(1,18)
		self.screen = pygame.display.set_mode((width, height), 0, 32)
		self.player = player.Snake()
		self.time = 0
		self.start = True
		self.Food = food.Food()
		self.font = pygame.font.SysFont('Comic Sans MS',30)

	def blit_grid(self):
		for x in range(20):
			pygame.draw.aaline(self.screen, black_color, (x * 20,0), (x * 20, height))
		for y in range(20):
			pygame.draw.aaline(self.screen, black_color, (0, y * 20), (width, y * 20))

	def frame_step(self, input_actions):
		# pygame.event.pump()

		self.clock.tick(32)

		# for event in pygame.event.get():
		# 	if event.type == pygame.QUIT:
		# 		exit()

		if self.start:
			self.Food.update(self.screen, self.player)
			self.start = False

		self.screen.fill(black_color)

		has_ate = False
		reward = 0
		terminal = False
		self.time += 1

		if sum(input_actions) != 1:
			raise ValueError('Multiple input actions!')

		if self.time > 250:
			reward = -0.02

		# input_actions[0] == 1: up
		# input_actions[1] == 1: down
		# input_actions[2] == 1: left
		# input_actions[3] == 1: right

		for i in range(len(input_actions)):
			if input_actions[i] == 1:
				self.player.update(self.screen, i)
				has_ate = self.Food.update(self.screen, self.player)
				self.blit_grid()
				break

		if self.player.is_dead:
			terminal = True
			self.__init__()
			reward = -1
			self.blit_grid()
		elif has_ate:
			reward = 1
			self.time = 0

		point = self.font.render(str(self.player.point), True, white_color)
		self.screen.blit(point, (0, 0))
		image_data = pygame.surfarray.array3d(pygame.display.get_surface())
		pygame.display.update()

		return image_data, reward, terminal