import math
import pydantic
import pygame.sprite

from .env import *
from .foods import Food
from .sound_controller import SoundController
from mlgame.view.view_model import create_rect_view_data, create_image_view_data


class LevelParams(pydantic.BaseModel):

    playground_size_w: int = 300
    playground_size_h: int = 300
    score_to_pass: int = 10
    time_to_play: int = 300

    food_1: int = 3
    food_2: int = 0
    food_3: int = 0
    garbage_1: int = 0
    garbage_2: int = 0
    garbage_3: int = 0


# level_thresholds = [10, 15, 20, 25, 30]


class Squid(pygame.sprite.Sprite):
    ANGLE_TO_RIGHT = math.radians(-10)
    ANGLE_TO_LEFT = math.radians(10)

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.origin_image = pygame.Surface([SQUID_W, SQUID_H])
        self.image = self.origin_image
        self.rect = self.image.get_rect()
        self.rect.center = (350, 300)
        self._score = 0
        self._vel = LEVEL_PROPERTIES[1]['vel']
        self._lv = 1
        self.angle = 0

    def update(self, motion):
        # for motion in motions:
        if motion == "UP":
            self.rect.centery -= self._vel
        elif motion == "DOWN":
            self.rect.centery += self._vel
        elif motion == "LEFT":
            self.rect.centerx -= self._vel
            self.angle = self.ANGLE_TO_LEFT
        elif motion == "RIGHT":
            self.rect.centerx += self._vel
            self.angle = self.ANGLE_TO_RIGHT
        else:
            self.angle = 0
        # self.image = pygame.transform.rotate(self.origin_image, self.angle)
        # print(self.angle)
        # center = self.rect.center
        # self.rect = self.image.get_rect()
        # self.rect.center = center

    @property
    def game_object_data(self):

        return create_image_view_data(
            "squid",
            self.rect.x,
            self.rect.y,
            self.rect.width,
            self.rect.height,
            self.angle

        )

    def eat_food_and_change_level_and_play_sound(self, food: Food, sound_controller: SoundController):
        self._score += food.score
        new_lv = get_current_level(self._score)

        if new_lv > self._lv:
            sound_controller.play_lv_up()
        elif new_lv < self._lv:
            sound_controller.play_lv_down()
        if new_lv != self._lv:
            self.rect.width = SQUID_W * LEVEL_PROPERTIES[new_lv]['size_ratio']
            self.rect.height = SQUID_H * LEVEL_PROPERTIES[new_lv]['size_ratio']
            self._vel = LEVEL_PROPERTIES[new_lv]['vel']
            self._lv = new_lv

    @property
    def score(self):
        return self._score

    @property
    def vel(self):
        return self._vel
    @property
    def lv(self):
        return self._lv


def get_current_level(score: int) -> int:
    """
    Determines the current level based on the player's score.

    :param score: int - The current score of the player.
    :return: int - The current level of the player.
    """

    for level, threshold in enumerate(LEVEL_THRESHOLDS, start=1):
        if score < threshold:
            return min(level,6)
    return len(LEVEL_THRESHOLDS) # Return the next level if score is beyond all thresholds
