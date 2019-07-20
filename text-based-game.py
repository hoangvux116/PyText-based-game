#!/usr/bin/env python3
__doc__ = '''
Trò chơi đánh đối kháng giữa 2 nhân vật. Mỗi nhân vật có tên (str),
máu (int), vũ khí.
Vũ khí chọn random khi tạo nhân vật, có damage (int) bằng lượng máu trừ đi
khi đánh trúng.

Cho 2 nhân vật lần lượt đánh nhau, print kết quả mỗi lượt đánh, print người
thắng.

'''
from random import choice
weapons = {'kicks': 18, 'punches': 15,
           'hair-pulls': 10, 'slaps': 8, 'scratches': 9}

# Creat a Character with damage generation, check isAlive and his/her status
class Fighter():
    def __init__(self, name, HP):
        self.name = name
        self.HP = HP

    def __str__(self):
        return '''{}, I'm {}, now I'm ready
                  for a Game of Throne
                  with {} HP.'''.format(choice(['Hi', 'Hello']),
                                        self.name, self.HP)

    def Attack(self, opponent):
        rand_wp = choice(list(weapons.keys()))
        if self is not opponent:
            opponent.HP -= weapons[rand_wp]
            print("{} {} against {} with {} dmg.".format(self.name,
                                                         rand_wp,
                                                         opponent.name,
                                                         weapons[rand_wp]))

    def isAlive(self):
        if self.HP > 0:
            return True
        else:
            return False

    def status(self):
        if self.isAlive():
            return ('''{} is a Winer,
                    remaining HP: {}.'''.format(self.name, self.HP))
        else:
            return ('''ahihi, {} was out of
                    blood and have to take care of
                    other half for the whole life.'''.format(self.name))
    # Add more if needed


def solve(player1, player2):

    # result = ('', 0)
    rounds = 1
    print(player1)
    print(player2)
    print('*' * 99)
    while player1.isAlive() and player2.isAlive():
        print('Rounds {}:\n'.format(rounds))
        if player1.isAlive():
            player1.Attack(player2)
        if player2.isAlive():
            player2.Attack(player1)
        print(player1.status())
        print(player2.status())
        rounds += 1
        print('-' * 69)
    if player1.isAlive():
        return (player1.name, player1.HP)
    else:
        return (player2.name, player2.HP)


def main():
    player1 = Fighter('Husband', 40)
    player2 = Fighter('Wife', 50)
    print(solve(player1, player2))


if __name__ == "__main__":
    main()
