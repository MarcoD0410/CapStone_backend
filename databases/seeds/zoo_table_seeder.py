"""ZooTableSeeder Seeder."""

from masoniteorm.seeds import Seeder
from app.Zoo import Zoo


class ZooTableSeeder(Seeder):
    def run(self):
        Zoo.create({"country": "United States", "animal": "Mountain Lion"})
        Zoo.create({"country": "China", "animal": "Panda"})
        Zoo.create({"country": "Russia", "animal": "Bears"})
