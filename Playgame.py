
import sys
import random

class Player:

    def __init__(self):
        self.player_life = 30
        self.player_name = ''


    def player_minus(self, damage):
        self.player_life -= damage
        return self.player_life

    def player_plus(self, damage):
        self.player_life += damage
        return self.player_life

    def player_current(self):
        return self.player_life

    def player_recovery(self):
        self.player_life +=10
        return self.player_life

    def player_reset(self):
        self.player_life = 30
        return self.player_life

    def player_zero(self):
        self.player_life = 0
        return self.player_life

    def player_setName(self,name):
        self.player_name = name
        return self.player_name

    def player_getName(self):
        return self.player_name


class Monster:
    def __init__(self):
        self.monster_life = 10
        self.monster_name = 'goblin'

    def monster_minus(self, damage):
        self.monster_life -= damage
        return self.monster_life

    def monster_plus(self, damage):
        self.monster_life += damage
        return self.monster_life

    def monster_current(self):
        return self.monster_life

    def monster_reset(self):
        self.monster_life = 30
        return self.monster_life

    def monster_zero(self):
        self.monster_life = 0
        return self.monster_life

    def monster_getName(self):
        return self.monster_name



player_info = Player()
monster_info = Monster()


def game_progress():


    print('-------------현재 상태------------')
    print('현재 플레이어 체력은 : ', player_info.player_current())
    print('현재 몬스터 체력은 : ', monster_info.monster_current())
    print('--------------------------------')
    print('')

    player_turn()
    monster_turn()


def player_turn():
    print('================================')
    print(player_info.player_getName(), "님 차례 입니다. ")
    print('======1 = 공격 / 2 = 회복(10)======')

    command = input()

    if command == '1' or command == '2':
        pass
    else:
        print('*잘못된 값을 입력하였습니다. 행동 실패*')
        print('')

    if command == '1':
        damege = random.randrange(1,6)
        print("################################")
        print(damege,'데미지 공격')
        print("################################")
        print("")
        if monster_info.monster_minus(damege) < 0:
            monster_info.monster_zero()
            print("********************************")
            print("**                            **")
            print("**            승리             **")
            print("**          Victory           **")
            print("**                            **")
            print("********************************")
            sys.exit(1)

    if command == '2':
        if player_info.player_recovery() > 30:
            player_info.player_reset()
            print("################################")
            print('최대 체력 30이상 회복 할 수 없습니다.')
            print("################################")
            print("")


def monster_turn():
    print('================================')
    print(monster_info.monster_getName(), " 차례")
    print('================================')
    print('')
    damage = random.randrange(3,11)

    print("################################")
    print(monster_info.monster_getName(), ' 이 ', damage, ' 만큼 공격하였습니다.')
    print("################################")
    print("")

    if player_info.player_minus(damage) < 0:
        player_info.player_zero()
        print("********************************")
        print("**                            **")
        print("**            패배             **")
        print("**            Lose            **")
        print("**                            **")
        print("********************************")
        print('패매하였습니다.')
        sys.exit(1)


def initialization_game():
    print('플레이어 이름을 입력해주세요.')
    player_info.player_setName(input())
    print('================================')
    print('=                              =')
    print('=                              =')
    print('=          Game Start          =')
    print('=                              =')
    print('=                              =')
    print('================================')



initialization_game()
while 'game'.__eq__('game'):
    game_progress()