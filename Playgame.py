import sys
import random
import os
import json

with open(os.getcwd() + '/monsters.lib', 'r') as monsters:
    monsters_informations = json.load(monsters)


class Player:

    def __init__(self, player_name):
        self.player_life = 30
        self.player_name = player_name
        self.player_level = 1
        self.player_exp = 0
        self.continue_status = True
        self.player_attack = 3

        print('================================')
        print('=                              =')
        print('=                              =')
        print('=          Game Start          =')
        print('=                              =')
        print('=                              =')
        print('================================')

    def give_damage(self, damage):
        monster_info.monster_life -= damage
        return monster_info.monster_life

    def recovery_life(self):
        self.player_life += 10
        return self.player_life

    def reset_life(self):
        self.player_life = 30

    def action_turn(self):

        print('-------------현재 상태------------')
        print('현재 플레이어 체력은 : ', player_info.player_life)
        print('현재 몬스터 체력은 : ', monster_info.monster_life)
        print('--------------------------------')
        print('')

        print('================================')
        print(player_info.player_name, "님 차례 입니다. ")
        print('======1 = 공격 / 2 = 회복(10)======')

        command = input()

        try:
            validate_playing_command(command)
        except KeyError:
            print('*잘못된 값을 입력하였습니다. 행동 실패*')
            print('')

        if command == '1':
            damage = random.randrange(self.player_attack, self.player_attack+3)
            print("################################")
            print(damage, '데미지 공격')
            print("################################")
            print("")
            self.give_damage(damage)
            if monster_info.monster_life <= 0:
                print("********************************")
                print("**                            **")
                print("**            승리             **")
                print("**          Victory           **")
                print("**                            **")
                print("********************************")
                print('')
                print('')
                print('계속 진행 하시겠습니까? ')
                print('계속 진행 == 3 | 게임 종료 == 4 ')
                self.calculate_experience()
                try:
                    validate_countinum_command(input())
                except KeyError:
                    print('잘못된 값을 입력하였습니다. 게임을 종료 합니다.')
                    sys.exit(0)


        elif command == '2':
            if player_info.recovery_life() > 30:
                player_info.reset_life()
                print("################################")
                print('최대 체력 30이상 회복 할 수 없습니다.')
                print("################################")
                print("")

    def define_experience(self, level):
        a, b = 1, 0
        for i in range(level):
            a, b = b, a + b
        return b

    def level_up(self):
        raise_life = random.randrange(3, 10)
        raise_attack = random.randrange(self.player_attack, self.player_attack + 3)

        self.player_life += raise_life
        self.player_attack += raise_attack

        print(raise_life, '만큼 체력이 증가되었습니다.')
        print(raise_attack, '만큼 공격력이 증가되었습니다.')

    def calculate_experience(self):
        self.player_exp += 1
        if self.define_experience(self.player_level) + 3 <= self.player_exp:
            self.player_level += 1
            print('레벨업 하였습니다. 현재 레벨 ', self.player_level)
            self.player_exp = 0
            self.level_up()
        print('다음 레벨업 필요 경험치 ', self.define_experience(self.player_level) + 3)
        print('현재 경험치 ', self.player_exp)


class Monster:
    monster_life = 0
    monster_name = ''
    monster_attack = 0
    monster_index = 0

    def __init__(self):
        self.monster_assign()

    def give_damage(self, damage):
        player_info.player_life -= damage
        return player_info.player_life

    def reset_life(self):
        self.monster_life = 30

    def action_turn(self):
        damage = random.randrange(monsters_informations[self.monster_index]['minatk'], monsters_informations[self.monster_index]['maxatk'])

        print("################################")
        print(self.monster_name, ' 이 ', damage, ' 만큼 공격하였습니다.')
        print("################################")
        print("")

        if self.give_damage(damage) <= 0:
            print("********************************")
            print("**                            **")
            print("**            패배             **")
            print("**            Lose            **")
            print("**                            **")
            print("********************************")
            sys.exit(0)

    def monster_assign(self):
        monster_positions = random.randrange(0, len(monsters_informations))
        self.monster_index = monster_positions

        self.monster_name = monsters_informations[monster_positions]['name']
        self.monster_life = monsters_informations[monster_positions]['health']
        self.monster_attack = random.randrange(monsters_informations[monster_positions]['minatk'],
                                               monsters_informations[monster_positions]['maxatk'])
        self.monster_level = monsters_informations[monster_positions]['level']




def validate_countinum_command(command):

    if command not in('3','4'):
        raise KeyError


    elif command == '3':
        monster_info.monster_assign()
        print("################################")
        print('새로운 전투 시작.')
        print("################################")
        print("")
        monster_info.monster_assign()

        print("################################")
        print('Level :', player_info.player_level)
        print('life :', player_info.player_life)
        print("################################")
        print("")
    elif command == '4':
        print("################################")
        print('게임을 종료합니다.')
        print("################################")
        print("")
        player_info.continue_status == False


def validate_playing_command(command):
    if command not in ('1', '2'):
        raise KeyError


if __name__ == '__main__':

    print('플레이어 이름을 입력해주세요.')
    player_info = Player(player_name=input())
    monster_info = Monster()
    monster_info.monster_assign()
    while player_info.continue_status == True:
        player_info.action_turn()
        monster_info.action_turn()
