import pygame
pygame.init()

WIDTH, HEIGHT = 800, 450
WHITE = (255,255,255)


clock = pygame.time.Clock()
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Vatnik TDF")

running = True
while running:

	screen.fill(WHITE)
	pygame.display.flip()
	clock.tick()

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

pygame.quit()