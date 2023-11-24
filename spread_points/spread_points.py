import random

import numpy as np


class Box:
    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    def periodic(self, dx, dy):
        if abs(dx) > self.x / 2:
            dx = dx - self.x * np.sign(dx)
        if abs(dy) > self.y / 2:
            dy = dy - self.y * np.sign(dy)
        return dx, dy


def force(r, f0=1.0, r0=1.0):
    if r < r0:
        return f0 * (1 - r / r0)
    else:
        return 0


def points_coord(N, box_x, box_y, dt=0.1, max_shift=0.001, max_iteration=10000):
    if N < 1 or box_x < 0.0 or box_y < 0.0:
        raise ValueError("N or box_x or box_y are not correct")
    r0 = (box_x * box_y / N) ** 0.5
    box = Box(box_x, box_y)

    # нач коорд всех точек
    x = (0.5 - np.random.random(N)) * box.x
    y = (0.5 - np.random.random(N)) * box.y

    # red_or_blue = ['red', 'blue']
    # colors = random.choices(red_or_blue, k = N)

    # смотрим взаим точек
    max_shift = 1  # макс смещение за один шаг
    cycles = 0
    while max_shift > 0.001 and cycles < max_iteration:
        cycles += 1
        fx = np.zeros(N)
        fy = np.zeros(N)
        for i in range(N - 1):
            for j in range(i + 1, N):
                dx = x[i] - x[j]
                dy = y[i] - y[j]
                dx, dy = box.periodic(
                    dx, dy
                )  # так как коробка замкнута как цилиндр выбираем меньшее (правильное) расстояние
                r = np.sqrt(dx**2 + dy**2)
                f = force(r, r0=r0) * dt
                fx[i] += f * dx / r
                fy[i] += f * dy / r
                fx[j] -= f * dx / r
                fy[j] -= f * dy / r
        x = x + fx
        y = y + fy
        max_shift = np.max(fx)
        for i in range(N):
            x[i], y[i] = box.periodic(x[i], y[i])  # не даем вылетить за коробку
    # m = int(N*fraction)
    # best_indecies = []
    # best_distance = 0.0
    # for _ in range(N**2):
    #     indecies = random.choices(list(range(N)), k=m)
    #     sum_distance = 0.0
    #     for i in range(m-1):
    #         for j in range(i+1, m):
    #             ii = indecies[i]
    #             jj = indecies[j]
    #             dx = x[ii] - x[jj]
    #             dy = y[ii] - y[jj]
    #             dx, dy = box.periodic(
    #                 dx, dy
    #             )  # так как коробка замкнута как цилиндр выбираем меньшее (правильное) расстояние
    #             r = dx**2 + dy**2
    #             sum_distance += np.sqrt(r)
    #     if sum_distance > best_distance:
    #         best_distance = sum_distance
    #         best_indecies = indecies
    return x, y
