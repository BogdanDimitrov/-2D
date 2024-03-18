import random

WIDTH = 600
HEIGHT = 400

TITLE = "Космическое путешествие"
FPS = 30

ship = Actor('ship', (300, 350))
space = Actor('space')
enemies = []
planets = [Actor("plan1", (random.randint(0, 600), -100)), Actor("plan2", (random.randint(0, 600), -100)), Actor("plan3", (random.randint(0, 600), -100))]
meteors = []
mode = 'menu'
type1 = Actor('ship1', (100, 200))
type2 = Actor('ship2', (300, 200))
type3 = Actor('ship3', (500, 200))
bullets = []
count = 0

# Заполнение списка врагов
for i in range(6):
        x = random.randint(0, 600)
        y = random.randint(-450, -50)
        enemy = Actor('enemy', (x, y))
        enemy.speed = random.randint(2, 8)
        enemies.append(enemy)

# Заполнение списка метеоритов
for i in range(6):
        x = random.randint(0, 600)
        y = random.randint(-450, -50)
        meteor = Actor('meteor', (x, y))
        meteor3 = Actor('meteor3', (x, y))
        meteor.speed = random.randint(2, 8)
        meteor3.speed = random.randint(3, 6)
        rand_meteor = random.choice([meteor, meteor3])
        meteors.append(rand_meteor)

# Отрисовка
def draw():
        # Режим игры
        if mode == 'menu':
                space.draw()
                screen.draw.text("Select ship!", center = (300, 100), color = "white", fontsize = 36)
                type1.draw()
                type2.draw()
                type3.draw()
        elif mode == 'game':
                space.draw()
                planets[0].draw()
                screen.draw.text(str(count), center = (15, 15), color = "white", fontsize = 50)
                # Отрисовка метеоритов
                for i in range(len(meteors)):
                        meteors[i].draw()
                        ship.draw()
                # Отрисовка врагов
                for i in range(len(enemies)):
                        enemies[i].draw()
                # Отрисовка bullet
                for i in range(len(bullets)):
                        bullets[i].draw()
        # Окно проигрыша
        elif mode == 'end':
                space.draw()
                screen.draw.text('GAME OVER!', center=(300, 200), color='white', fontsize=36)
                screen.draw.text(str(count), center = (300, 300), color = "white", fontsize = 36)
# Управление
def on_mouse_move(pos):
        ship.pos = pos

# Добавление в список нового врага
def new_enemy():
        x = random.randint(0, 600)
        y = -50
        enemy = Actor('enemy', (x, y))
        enemy.speed = random.randint(2, 8)
        enemies.append(enemy)

# Движение врагов
def enemy_ship():
        for i in range(len(enemies)):
                if enemies[i].y < 650:
                        enemies[i].y = enemies[i].speed + enemies[i].y
                else:
                        enemies.pop(i)
                        new_enemy()

# Движение планет
def planet():
        if planets[0].y < 550:
                planets[0].y = planets[0].y + 1
        else:
                        planets[0].y = -100
                        planets[0].x =                         random.randint(0, 600)
                        first =                         planets.pop(0)
                        planets.append(first)

# Движение метеоритов
def meteorites():
        for i in range(len(meteors)):
                if meteors[i].y < 450:
                        meteors[i].y = meteors[i].y + meteors[i].speed
                else:
                        meteors[i].x =                         random.randint(0, 600)
                        meteors[i].y = -20
                        meteors[i].speed = random.randint(2, 10)

# Столкновения
def collisions():
        global mode, count
        for i in range(len(enemies)):
                if ship.colliderect(enemies[i]):
                    mode = 'end'
                for j in range(len(bullets)):
                        if enemies[i].colliderect(bullets[j]):
                                enemies.pop(i)
                                bullets.pop(j)
                                new_enemy()
                                count += 1
                                break

def on_mouse_down(button, pos):
        global mode, ship, bullets
        if mode == 'menu' and type1.collidepoint(pos):
                ship.image = "ship1"
                mode = 'game'
        elif mode == 'menu' and type2.collidepoint(pos):
                ship.image = "ship2"
                mode = 'game'
        elif mode == 'menu' and type3.collidepoint(pos):
                ship.image = "ship3"
                mode = 'game'
        elif mode == 'game' and button == mouse.LEFT:
                bullet = Actor('missiles')
                bullet.pos = ship.pos
                bullets.append(bullet)

def update(dt):
        if mode == 'game':
                enemy_ship()
                collisions()
                planet()
                meteorites()
                for i in range(len(bullets)):
                        if bullets[i].y < 0:
                                bullets.pop(i)
                                break
                        else:
                                bullets[i].y -= 10