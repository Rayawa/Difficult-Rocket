#  -------------------------------
#  Difficult Rocket
#  Copyright © 2020-2023 by shenjackyuanjie 3695888@qq.com
#  All rights reserved
#  -------------------------------

import random
import unittest

from typing import Tuple

from libs.pyglet_rs import Vector2_rs, Vector3_rs, Vector4_rs


# 用于自动在测试运行前后输出测试信息的装饰器
def print_test_info(func):
    def wrapper(*args, **kwargs):
        print(f"{'=' * 20} {func.__name__} {'=' * 20}")
        func(*args, **kwargs)
        print(f"{'=' * 20} {func.__name__} {'=' * 20}")

    return wrapper


def gen_random_vector() -> Tuple[Vector2_rs, Vector3_rs, Vector4_rs]:
    vec2 = Vector2_rs(random.randint(1, 100), random.randint(1, 100))
    vec3 = Vector3_rs(random.randint(1, 100), random.randint(1, 100), random.randint(1, 100))
    vec4 = Vector4_rs(random.randint(1, 100), random.randint(1, 100), random.randint(1, 100), random.randint(1, 100))
    return vec2, vec3, vec4


class TestVector(unittest.TestCase):

    @print_test_info
    def test1_create_print_vector(self):
        vec2, vec3, vec4 = gen_random_vector()

        print(f"{vec2=}")
        print(f"{vec3=}")
        print(f"{vec4=}")

    @print_test_info
    def test2_calculate_vector(self):
        vec2, vec3, vec4 = gen_random_vector()
        vec2_1, vec3_1, vec4_1 = gen_random_vector()

        print('test add')
        self.assertEqual(vec2 + vec2_1, Vector2_rs(vec2.x + vec2_1.x, vec2.y + vec2_1.y))
        self.assertEqual(vec3 + vec3_1, Vector3_rs(vec3.x + vec3_1.x, vec3.y + vec3_1.y, vec3.z + vec3_1.z))
        self.assertEqual(vec4 + vec4_1, Vector4_rs(vec4.x + vec4_1.x, vec4.y + vec4_1.y, vec4.z + vec4_1.z, vec4.w + vec4_1.w))

        print('test sub')
        self.assertEqual(vec2 - vec2_1, Vector2_rs(vec2.x - vec2_1.x, vec2.y - vec2_1.y))
        self.assertEqual(vec3 - vec3_1, Vector3_rs(vec3.x - vec3_1.x, vec3.y - vec3_1.y, vec3.z - vec3_1.z))
        self.assertEqual(vec4 - vec4_1, Vector4_rs(vec4.x - vec4_1.x, vec4.y - vec4_1.y, vec4.z - vec4_1.z, vec4.w - vec4_1.w))

        print('test mul')
        self.assertEqual(vec2 * vec2_1, Vector2_rs(vec2.x * vec2_1.x, vec2.y * vec2_1.y))
        self.assertEqual(vec3 * vec3_1, Vector3_rs(vec3.x * vec3_1.x, vec3.y * vec3_1.y, vec3.z * vec3_1.z))
        self.assertEqual(vec4 * vec4_1, Vector4_rs(vec4.x * vec4_1.x, vec4.y * vec4_1.y, vec4.z * vec4_1.z, vec4.w * vec4_1.w))

        print('test true_div')
        self.assertEqual(vec2 / vec2_1, Vector2_rs(vec2.x / vec2_1.x, vec2.y / vec2_1.y))
        self.assertEqual(vec3 / vec3_1, Vector3_rs(vec3.x / vec3_1.x, vec3.y / vec3_1.y, vec3.z / vec3_1.z))
        self.assertEqual(vec4 / vec4_1, Vector4_rs(vec4.x / vec4_1.x, vec4.y / vec4_1.y, vec4.z / vec4_1.z, vec4.w / vec4_1.w))

        print('test floor_div')
        self.assertEqual(vec2 // vec2_1, Vector2_rs(vec2.x // vec2_1.x, vec2.y // vec2_1.y))
        self.assertEqual(vec3 // vec3_1, Vector3_rs(vec3.x // vec3_1.x, vec3.y // vec3_1.y, vec3.z // vec3_1.z))
        self.assertEqual(vec4 // vec4_1, Vector4_rs(vec4.x // vec4_1.x, vec4.y // vec4_1.y, vec4.z // vec4_1.z, vec4.w // vec4_1.w))

