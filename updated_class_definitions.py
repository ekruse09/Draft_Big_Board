# class definitions

from abc import ABC
from enum import Enum


class Grade(Enum):
    A = 5
    B = 4
    C = 3
    D = 2
    F = 1


class Player(ABC):
    def __init__(self, name, college, height, weight, birth_date, rating, url):
        self.name = name
        self.college = college
        self.height = height
        self.weight = weight
        self.birth_date = birth_date
        self.rating = rating
        self.url = url


class QB(Player):
    def __init__(self, name, college, height, weight, birth_date, rating, url, arm_strength=Grade.F,
                 ball_placement=Grade.F,
                 field_processing=Grade.F, pocket_presence=Grade.F, scrambling=Grade.F):
        super().__init__(name, college, height, weight, birth_date, rating, url)
        self.arm_strength = arm_strength
        self.ball_placement = ball_placement
        self.field_processing = field_processing
        self.pocket_presence = pocket_presence
        self.scrambling = scrambling


class RB(Player):
    def __init__(self, name, college, height, weight, birth_date, rating, url, acceleration=Grade.F,
                 contact_balance=Grade.F,
                 pass_catching=Grade.F, pass_protection=Grade.F, top_end_speed=Grade.F, vision=Grade.F):
        super().__init__(name, college, height, weight, birth_date, rating, url)
        self.acceleration = acceleration
        self.contact_balance = contact_balance
        self.pass_catching = pass_catching
        self.pass_protection = pass_protection
        self.top_end_speed = top_end_speed
        self.vision = vision


class WR(Player):
    def __init__(self, name, college, height, weight, birth_date, rating, url, ball_carrier_ability=Grade.F,
                 catching=Grade.F,
                 contested_catching=Grade.F, field_awareness=Grade.F, route_running=Grade.F, run_blocking=Grade.F,
                 top_end_speed=Grade.F, quickness=Grade.F):
        super().__init__(name, college, height, weight, birth_date, rating, url)
        self.ball_carrier_ability = ball_carrier_ability
        self.catching = catching
        self.contested_catching = contested_catching
        self.field_awareness = field_awareness
        self.route_running = route_running
        self.run_blocking = run_blocking
        self.top_end_speed = top_end_speed
        self.quickness = quickness


class TE(Player):
    def __init__(self, name, college, height, weight, birth_date, rating, url, ball_carrier_ability=Grade.F,
                 catching=Grade.F,
                 movement_skills=Grade.F, pass_blocking=Grade.F, route_running=Grade.F, run_blocking=Grade.F):
        super().__init__(name, college, height, weight, birth_date, rating, url)
        self.ball_carrier_ability = ball_carrier_ability
        self.catching = catching
        self.movement_skills = movement_skills
        self.pass_blocking = pass_blocking
        self.route_running = route_running
        self.run_blocking = run_blocking


class OT(Player):
    def __init__(self, name, college, height, weight, birth_date, rating, url, awareness=Grade.F,
                 movement_skills=Grade.F,
                 pass_blocking=Grade.F, power_run_blocking=Grade.F, zone_run_blocking=Grade.F):
        super().__init__(name, college, height, weight, birth_date, rating, url)
        self.awareness = awareness
        self.movement_skills = movement_skills
        self.pass_blocking = pass_blocking
        self.power_run_blocking = power_run_blocking
        self.zone_run_blocking = zone_run_blocking


class IOL(Player):
    def __init__(self, name, college, height, weight, birth_date, rating, url, awareness=Grade.F,
                 movement_skills=Grade.F,
                 pass_blocking=Grade.F, power_run_blocking=Grade.F, zone_run_blocking=Grade.F):
        super().__init__(name, college, height, weight, birth_date, rating, url)
        self.awareness = awareness
        self.movement_skills = movement_skills
        self.pass_blocking = pass_blocking
        self.power_run_blocking = power_run_blocking
        self.zone_run_blocking = zone_run_blocking


class IDL(Player):
    def __init__(self, name, college, height, weight, birth_date, rating, url, awareness=Grade.F,
                 block_shedding=Grade.F,
                 movement_skills=Grade.F, pass_rushing=Grade.F, run_stuffing=Grade.F):
        super().__init__(name, college, height, weight, birth_date, rating, url)
        self.awareness = awareness
        self.block_shedding = block_shedding
        self.movement_skills = movement_skills
        self.pass_rushing = pass_rushing
        self.run_stuffing = run_stuffing


class EDGE(Player):
    def __init__(self, name, college, height, weight, birth_date, rating, url, awareness=Grade.F,
                 coverage_ability=Grade.F,
                 movement_skills=Grade.F, pass_rushing=Grade.F, run_stuffing=Grade.F):
        super().__init__(name, college, height, weight, birth_date, rating, url)
        self.awareness = awareness
        self.coverage_ability = coverage_ability
        self.movement_skills = movement_skills
        self.pass_rushing = pass_rushing
        self.run_stuffing = run_stuffing


class LB(Player):
    def __init__(self, name, college, height, weight, birth_date, rating, url, awareness=Grade.F,
                 block_shedding=Grade.F,
                 coverage_ability=Grade.F, movement_skills=Grade.F, tackling=Grade.F):
        super().__init__(name, college, height, weight, birth_date, rating, url)
        self.awareness = awareness
        self.block_shedding = block_shedding
        self.coverage_ability = coverage_ability
        self.movement_skills = movement_skills
        self.tackling = tackling


class CB(Player):
    def __init__(self, name, college, height, weight, birth_date, rating, url, awareness=Grade.F, man_coverage=Grade.F,
                 movement_skills=Grade.F, press=Grade.F, tackling=Grade.F, zone_coverage=Grade.F):
        super().__init__(name, college, height, weight, birth_date, rating, url)
        self.awareness = awareness
        self.man_coverage = man_coverage
        self.movement_skills = movement_skills
        self.press = press
        self.tackling = tackling
        self.zone_coverage = zone_coverage


class SAF(Player):
    def __init__(self, name, college, height, weight, birth_date, rating, url, awareness=Grade.F,
                 block_shedding=Grade.F,
                 man_coverage=Grade.F, movement_skills=Grade.F, tackling=Grade.F, zone_coverage=Grade.F):
        super().__init__(name, college, height, weight, birth_date, rating, url)
        self.awareness = awareness
        self.block_shedding = block_shedding
        self.man_coverage = man_coverage
        self.movement_skills = movement_skills
        self.tackling = tackling
        self.zone_coverage = zone_coverage
