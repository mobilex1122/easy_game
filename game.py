import pygame
import sys
import random

pygame.init()
pygame.mixer.init()

# setings
WIDTH = 400
HIGHT = 1000
player_color = (255, 0 ,0)
enemy_color = (0, 0 , 255)
pozadi = (0, 0, 0)
player_size = 100
enemy_size = 100
speed = 10
text_color = (255, 255, 0)


# setup

a = [0, 100, 200, 300]
player_pos = [WIDTH/2, HIGHT-player_size-40]
enemy_pos = [random.choice(a), 0]
myfont = pygame.font.SysFont("moonspace", 35)
myfonta = pygame.font.SysFont("moonspace", 40)
score = 0
bscore = 0
screen = pygame.display.set_mode((WIDTH, HIGHT))
loop = True
WSI = pygame.mixer.music.load('music.ogg')
pygame.mixer.music.play(-1)
gameIcon = pygame.image.load("icon.png")
pygame.display.set_icon(gameIcon)
pygame.display.set_caption("easy game")
prohra = True
clock = pygame.time.Clock()
def getscore():
	score = 0
	try:
		rscore = open("score.txt", "r")
		score = int(rscore.read())
		rscore.close()
		print("score read ok")
	except IOError:
		print("no bscore")
	except ValueError:
		print("error")
	return score

def savescore(newbscore):
	try:
		wscore = open("score.txt", "w")
		wscore.write(str(newbscore))
		wscore.close()
	except IOError:
		print("write error")

bscore = getscore()



def detect_collision(player_pos, enemy_pos):
	p_x = player_pos[0]
	p_y = player_pos[1]
	e_x = enemy_pos[0]
	e_y = enemy_pos[1]
	if (e_x >= p_x and e_x < (p_x + player_size)) or (p_x >= e_x and p_x < (e_x + enemy_size)):
		if (e_y >= p_y and e_y < (p_y + player_size)) or (p_y >= e_y and p_y < (e_y + enemy_size)):
			return True
	return False
keys=pygame.key.get_pressed()
#game
while loop:
	text = "score: " + str(score)
	label = myfont.render(text, 1, text_color)
	screen.blit(label, (WIDTH - 390, HIGHT -40))
	texta = "best: " + str(bscore)
	labelc = myfont.render(texta, 1, text_color)
	screen.blit(labelc, (WIDTH - 200, HIGHT -40))
	labela = myfonta.render("easy game!", 1, text_color)
	screen.blit(labela, (140, HIGHT/2-10))
	labela = myfont.render("press space", 1, text_color)
	screen.blit(labela, (142, HIGHT/2+30))
	pygame.display.update()
	if score > bscore:
		savescore(score)
		bscore = score
		print("new bscore")
	
	score = 0
	speed = 10
	while prohra:
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_SPACE:
					prohra = False
					pygame.mixer.music.stop()
					WSA = pygame.mixer.music.load('music2.ogg')
					pygame.mixer.music.play(-1)
			if event.type == pygame.QUIT:
				sys.exit()
	while not prohra:

		for event in pygame.event.get():
			
			if event.type == pygame.QUIT:
				if score > bscore:
					savescore(score)
					print("new bscore")

				
				sys.exit()
			if event.type == pygame.KEYDOWN:
				x = player_pos[0]
				y = player_pos[1]
				if event.key == pygame.K_LEFT:
					x -= player_size

				elif event.key == pygame.K_RIGHT:
				
				
					x += player_size
				player_pos = [x, y]
		screen.fill(pozadi)

		if enemy_pos[1] >= 0 and enemy_pos[1] < HIGHT:
			enemy_pos[1] += speed
		else:
			enemy_pos[0] = random.choice(a)
			enemy_pos[1] = 0
			prohra = True

		if detect_collision(player_pos, enemy_pos):
			score += 1
			speed += 0.5
			enemy_pos[0] = random.choice(a)
			enemy_pos[1] = 0
	
		text = "score: " + str(score)
		label = myfont.render(text, 1, text_color)
		screen.blit(label, (WIDTH - 390, HIGHT -40))
		texta = "speed: " + str(speed)
		labelc = myfont.render(texta, 1, text_color)
		screen.blit(labelc, (WIDTH - 200, HIGHT -40))


		pygame.draw.rect(screen, enemy_color, (enemy_pos[0], enemy_pos[1], enemy_size, enemy_size))
		pygame.draw.rect(screen, player_color, (player_pos[0], player_pos[1], player_size,player_size))
		if player_pos[0] > WIDTH - player_size:
			player_pos[0] = WIDTH - player_size
		if player_pos[0] < 0:
			player_pos[0] = 0
		clock.tick(30)

		#aktualisovat obraz
		pygame.display.update()


	
	screen.fill(pozadi)
	labela = myfont.render("game over", 2, text_color)
	screen.blit(labela, (149, HIGHT/2))
	text = "score: " + str(score)
	label = myfont.render(text, 1, text_color)
	screen.blit(label, (WIDTH - 390, HIGHT -40))
	texta = "best: " + str(bscore)
	labelc = myfont.render(texta, 1, text_color)
	screen.blit(labelc, (WIDTH - 200, HIGHT -40))
	labela = myfont.render("press space", 1, text_color)
	screen.blit(labela, (142, HIGHT/2+30))
	
	if score > bscore:
		savescore(score)
		bscore = score
		labela = myfonta.render("new best score!", 1, text_color)
		screen.blit(labela, (125, HIGHT/2-40))
	pygame.display.update()
	score = 0
	speed = 10
	pygame.mixer.music.stop()
	WSI = pygame.mixer.music.load('music.ogg')
	pygame.mixer.music.play(-1)
	while prohra:
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_SPACE:
					prohra = False
					pygame.mixer.music.stop()
					WSA = pygame.mixer.music.load('music2.ogg')
					pygame.mixer.music.play(-1)
			if event.type == pygame.QUIT:
				sys.exit()
