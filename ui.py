# ui.py

from enum import Enum
from datetime import datetime

class Grade(Enum):
    A = 5
    B = 4
    C = 3
    D = 2
    F = 1

class Player:
    def __init__(self, name, college, height, weight, birth_date, rating, url):
        self.name = name
        self.college = college
        self.height = height
        self.weight = weight
        self.birth_date = birth_date
        self.age = self.calculate_age()
        self.rating = rating
        self.url = url

    def calculate_age(self):
        today = datetime.today()
        age = today.year - self.birth_date.year - ((today.month, today.day) < (self.birth_date.month, self.birth_date.day))
        return age

    def __repr__(self):
        return f"{self.name}, {self.college}, {self.height}, {self.weight}, Age: {self.age}"

class QB(Player):
    def __init__(self, name, college, height, weight, birth_date, rating, url, arm_strength=Grade.C, ball_placement=Grade.C,
                 field_processing=Grade.C, pocket_presence=Grade.C, scrambling=Grade.C):
        super().__init__(name, college, height, weight, birth_date, rating, url)
        self.arm_strength = arm_strength
        self.ball_placement = ball_placement
        self.field_processing = field_processing
        self.pocket_presence = pocket_presence
        self.scrambling = scrambling

class RB(Player):
    def __init__(self, name, college, height, weight, birth_date, rating, url, acceleration=Grade.C, contact_balance=Grade.C,
                 pass_catching=Grade.C, pass_protection=Grade.C, top_end_speed=Grade.C, vision=Grade.C):
        super().__init__(name, college, height, weight, birth_date, rating, url)
        self.acceleration = acceleration
        self.contact_balance = contact_balance
        self.pass_catching = pass_catching
        self.pass_protection = pass_protection
        self.top_end_speed = top_end_speed
        self.vision = vision

class WR(Player):
    def __init__(self, name, college, height, weight, birth_date, rating, url, ball_carrier_ability=Grade.C, catching=Grade.C,
                 contested_catching=Grade.C, field_awareness=Grade.C, route_running=Grade.C, run_blocking=Grade.C,
                 top_end_speed=Grade.C, quickness=Grade.C):
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
    def __init__(self, name, college, height, weight, birth_date, rating, url, ball_carrier_ability=Grade.C, catching=Grade.C,
                 movement_skills=Grade.C, pass_blocking=Grade.C, route_running=Grade.C, run_blocking=Grade.C):
        super().__init__(name, college, height, weight, birth_date, rating, url)
        self.ball_carrier_ability = ball_carrier_ability
        self.catching = catching
        self.movement_skills = movement_skills
        self.pass_blocking = pass_blocking
        self.route_running = route_running
        self.run_blocking = run_blocking

class OT(Player):
    def __init__(self, name, college, height, weight, birth_date, rating, url, awareness=Grade.C, movement_skills=Grade.C,
                 pass_blocking=Grade.C, power_run_blocking=Grade.C, zone_run_blocking=Grade.C):
        super().__init__(name, college, height, weight, birth_date, rating, url)
        self.awareness = awareness
        self.movement_skills = movement_skills
        self.pass_blocking = pass_blocking
        self.power_run_blocking = power_run_blocking
        self.zone_run_blocking = zone_run_blocking

class IOL(Player):
    def __init__(self, name, college, height, weight, birth_date, rating, url, awareness=Grade.C, movement_skills=Grade.C,
                 pass_blocking=Grade.C, power_run_blocking=Grade.C, zone_run_blocking=Grade.C):
        super().__init__(name, college, height, weight, birth_date, rating, url)
        self.awareness = awareness
        self.movement_skills = movement_skills
        self.pass_blocking = pass_blocking
        self.power_run_blocking = power_run_blocking
        self.zone_run_blocking = zone_run_blocking

class IDL(Player):
    def __init__(self, name, college, height, weight, birth_date, rating, url, awareness=Grade.C, block_shedding=Grade.C,
                 movement_skills=Grade.C, pass_rushing=Grade.C, run_stuffing=Grade.C):
        super().__init__(name, college, height, weight, birth_date, rating, url)
        self.awareness = awareness
        self.block_shedding = block_shedding
        self.movement_skills = movement_skills
        self.pass_rushing = pass_rushing
        self.run_stuffing = run_stuffing

class Edge(Player):
    def __init__(self, name, college, height, weight, birth_date, rating, url, awareness=Grade.C, coverage_ability=Grade.C,
                 movement_skills=Grade.C, pass_rushing=Grade.C, run_stuffing=Grade.C):
        super().__init__(name, college, height, weight, birth_date, rating, url)
        self.awareness = awareness
        self.coverage_ability = coverage_ability
        self.movement_skills = movement_skills
        self.pass_rushing = pass_rushing
        self.run_stuffing = run_stuffing

class LB(Player):
    def __init__(self, name, college, height, weight, birth_date, rating, url, awareness=Grade.C, block_shedding=Grade.C,
                 coverage_ability=Grade.C, movement_skills=Grade.C, tackling=Grade.C):
        super().__init__(name, college, height, weight, birth_date, rating, url)
        self.awareness = awareness
        self.block_shedding = block_shedding
        self.coverage_ability = coverage_ability
        self.movement_skills = movement_skills
        self.tackling = tackling

class CB(Player):
    def __init__(self, name, college, height, weight, birth_date, rating, url, awareness=Grade.C, man_coverage=Grade.C,
                 movement_skills=Grade.C, press=Grade.C, tackling=Grade.C, zone_coverage=Grade.C):
        super().__init__(name, college, height, weight, birth_date, rating, url)
        self.awareness = awareness
        self.man_coverage = man_coverage
        self.movement_skills = movement_skills
        self.press = press
        self.tackling = tackling
        self.zone_coverage = zone_coverage

class SAF(Player):
    def __init__(self, name, college, height, weight, birth_date, rating, url, awareness=Grade.C, block_shedding=Grade.C,
                 man_coverage=Grade.C, movement_skills=Grade.C, tackling=Grade.C, zone_coverage=Grade.C):
        super().__init__(name, college, height, weight, birth_date, rating, url)
        self.awareness = awareness
        self.block_shedding = block_shedding
        self.man_coverage = man_coverage
        self.movement_skills = movement_skills
        self.tackling = tackling
        self.zone_coverage = zone_coverage
