import random

WIDTH = 1280
HEIGHT = 720

TITLE = "Огонь и сталь"
FPS = 30

ship = Actor('tank', (300, 350))
fon = Actor('fon')
enemies = []
diris = [Actor("diris", (random.randint(0, 1200), -100)), Actor("diris", (random.randint(0, 1200), -100)), Actor("diris", (random.randint(0, 1200), -100))]
drons = []
mode = 'menu'
type1 = Actor('tank', (200, 300))
type2 = Actor('tank2', (600, 300))
type3 = Actor('tank3', (1000, 300))
bullets = []
count = 0

# Заполнение списка врагов
for i in range(6):
        x = random.randint(0, 600)
        y = random.randint(-450, -50)
        enemy = Actor('tank4', (x, y))
        enemy.speed = random.randint(2, 3)
        enemies.append(enemy)

# Заполнение списка метеоритов
for i in range(6):
        x = random.randint(0, 600)
        y = random.randint(-450, -50)
        dron = Actor('dron', (x, y))
        jet = Actor('jet', (x, y))
        dron.speed = random.randint(2, 6)
        jet.speed = random.randint(9, 12)
        rand_dron = random.choice([dron, jet])
        drons.append(rand_dron)

# Отрисовка
def draw():
        # Режим игры
        if mode == 'menu':
                fon.draw()
                screen.draw.text("Select tank!", center = (620, 160), color = "white", fontsize = 70)
                type1.draw()
                type2.draw()
                type3.draw()
        elif mode == 'game':
                fon.draw()
                ship.draw()
                # Отрисовка врагов
                for i in range(len(enemies)):
                        enemies[i].draw()
                # Отрисовка bullet
                for i in range(len(bullets)):
                        bullets[i].draw()
                diris[0].draw()
                screen.draw.text(str(count), center = (15, 15), color = "white", fontsize = 50)
                # Отрисовка метеоритов
                for i in range(len(drons)):
                        drons[i].draw()
        # Окно проигрыша
        elif mode == 'end':
                fon.draw()
                screen.draw.text('GAME OVER!', center=(640, 260), color='white', fontsize=80)
                screen.draw.text(str(count), center = (640, 360), color = "white", fontsize = 80)
# Управление
def on_mouse_move(pos):
        ship.pos = pos

# Добавление в список нового врага
def new_enemy():
        x = random.randint(0, 1280)
        y = -50
        enemy = Actor('tank5', (x, y))
        enemy.speed = random.randint(2, 3)
        enemies.append(enemy)

# Движение врагов
def enemy_ship():
        for i in range(len(enemies)):
                if enemies[i].y < 720:
                        enemies[i].y = enemies[i].speed + enemies[i].y
                else:
                        enemies.pop(i)
                        new_enemy()

# Движение планет
def diri():
        if diris[0].y < 800:
                diris[0].y = diris[0].y + 1
        else:
                        diris[0].y = -100
                        diris[0].x =                         random.randint(0, 1200)
                        first =                         diris.pop(0)
                        diris.append(first)

# Движение метеоритов
def dron():
        for i in range(len(drons)):
                if drons[i].y < 720:
                        drons[i].y = drons[i].y + drons[i].speed
                else:
                        drons[i].x =                         random.randint(0, 600)
                        drons[i].y = -20
                        drons[i].speed = random.randint(2, 10)

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
                ship.image = "tank"
                mode = 'game'
        elif mode == 'menu' and type2.collidepoint(pos):
                ship.image = "tank2"
                mode = 'game'
        elif mode == 'menu' and type3.collidepoint(pos):
                ship.image = "tank3"
                mode = 'game'
        elif mode == 'game' and button == mouse.LEFT:
                bullet = Actor('missiles')
                bullet.pos = ship.pos
                bullets.append(bullet)

def update(dt):
        global mode, count
        if mode == 'game':
                enemy_ship()
                collisions()
                diri()
                dron()
                for i in range(len(bullets)):
                        if bullets[i].y < 0:
                                bullets.pop(i)
                                break
                        else:
                                bullets[i].y -= 10
        elif mode == 'end' and keyboard.space:
            mode = 'game'
            count = 0
          
