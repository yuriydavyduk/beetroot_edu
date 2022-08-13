from random import randint


class Boss:

    def __init__(self, id_: int, name: str, company: str):
        self.id = id_
        self.name = name
        self.company = company
        self.workers = []

    def __str__(self):
        return self.name

    def __repr__(self):
        return f'id: {self.id} name: {self.name} company {self.company}'


class Worker:

    def __init__(self, id_: int, name: str, company: str = '', _boss: Boss = None):
        self.id = id_
        self.name = name
        self.company = company
        self._boss = _boss

    def __str__(self):
        return self.name

    def __repr__(self):
        return f'id: {self.id} name: {self.name} company: {self.company} boss: {self.boss}'

    @property
    def boss(self):
        return self._boss

    @boss.setter
    def boss(self, boss: Boss):
        if type(self.boss) == Boss:
            self.boss.workers.remove(self)

        self.company = boss.company
        self._boss = boss

        if self not in boss.workers:
            boss.workers.append(self)


boss_petro = Boss(randint(1, 100), 'Petro', 'BM Parts')
boss_ivan = Boss(randint(1, 100), 'Ivan', 'Romashka')

worker_yuriy = Worker(randint(1, 100), 'Yuriy')
worker_pavlo = Worker(randint(1, 100), 'Pavlo')

worker_yuriy.boss = boss_ivan
worker_pavlo.boss = boss_ivan

print(f'{boss_petro} workers: {boss_petro.workers}')
print(f'{boss_ivan} workers: {boss_ivan.workers}')
print(worker_yuriy.boss)
print(worker_pavlo.boss)

worker_yuriy.boss = boss_petro

print(f'{boss_petro} workers: {boss_petro.workers}')
print(f'{boss_ivan} workers: {boss_ivan.workers}')
print(worker_yuriy.boss)
print(worker_pavlo.boss)
