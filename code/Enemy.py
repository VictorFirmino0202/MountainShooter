import pygame

from code.Entity import Entity
from code.EnemyShot import EnemyShot
from code.Const import ENTITY_SPEED, ENTITY_HEALTH, ENTITY_DAMAGE, ENTITY_SCORE, ENTITY_SHOT_DELAY, WIN_HEIGHT


class Enemy3(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.health = 80  # Vida do Enemy3
        self.damage = 15   # Dano causado pelo Enemy3
        self.score = 200   # Pontuação ao derrotar o Enemy3
        self.speed = ENTITY_SPEED[self.name]  # Velocidade horizontal
        self.vertical_speed = 2  # Velocidade vertical normal
        self.direction = 1  # Direção do movimento vertical (1 para baixo, -1 para cima)
        self.shoot_delay = ENTITY_SHOT_DELAY.get(name, 100)  # Atraso de tiro
        self.last_shot_time = pygame.time.get_ticks()  # Tempo em milissegundos

    def move(self):
        # Lógica de movimento horizontal e vertical
        self.rect.centerx -= self.speed
        self.rect.centery += self.direction * self.vertical_speed

        # Mudança de direção vertical
        if self.rect.bottom >= WIN_HEIGHT:
            self.direction = -1  # Começa a subir
        elif self.rect.top <= 0:
            self.direction = 1  # Começa a descer

    def shoot(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_shot_time >= self.shoot_delay:
            self.last_shot_time = current_time
            shot_position = (self.rect.centerx, self.rect.centery)
            return EnemyShot(name=f'{self.name}Shot', position=shot_position)  # Utiliza EnemyShot
        return None
