# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют 
# два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. 
# За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, 
# чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

from random import *

rules = (
    '"Игра с конфетами"\n'
    'Правила игры:\n'
    'Играют два игрока делая ход друг после друга.\n'
    'Первый ход определяется жеребьевкой.\n'
    'Исходные данные:\n'
    'На столе лежит 2021 конфета\n'
    'За один ход можно забрать не более чем 28 конфет\n'
    'Все конфеты оппонента достаются сделавшему последний ход\n'
    )
print(rules)
bot_or_player=int(input('если хотите играть с ботом, нажмите 1, иначе нажмите 0 \n'))

max_number_move = 28
total_sweets = 2021

message = ['Твой ход брать конфеты', 'Давай, бери конфеты',
            'Сколько конфет берешь?', 'Бери!']
message_out = ['Ну, куда, перебор!', 'Так много нельзя!',
            'Куда сколько конфет берешь?', 'Жадина!']

def player_bot(): # Игра с ботом
    player1 = input('Игрок, представьтесь\n')
    player2 = 'Искуственный интеллект'
    print(f'Сегодня Вы играете с {player2}')
    return [player1, player2]

def player_player(): # игра с игроком
    player1 = input('Первый игрок, представьтесь\n')
    player2 = input('Второй игрок, представьтесь\n')
    print(f'{player1} играет против {player2}')
    return [player1, player2]

def turn_player(): # выбор очереди
    turn = randint(0,2)
    return turn

if bot_or_player == 0:
    players = player_player()
else:
    players = player_bot()
turn = turn_player()

if turn == 0:
    flag = False
    print(f'Вы, {players[0]}, ходите первыми')
else:
    flag = True
    print(f'Вы, {players[1]}, ходите первыми') # второй игрок или бот

# print(flag)
flag_out=0
  
game_over = 0

if bot_or_player == 1:
    while total_sweets > 0:
        if flag == True:
        # обычный бот
            sweet_on_bot = randint(1,29)
            
        # часть с умным ботом    
            # sweet_on_bot = randint(1,29)
            # while total_sweets-sweet_on_bot <= 28 and total_sweets > 29:
            #     sweet_on_bot = randint(1,29)
            
            total_sweets -=sweet_on_bot
            print(f'{players[1]} взял {sweet_on_bot} конфет')
            print('')    
        else:
            sweet_on = int(input(f'{players[0]}, {choice(message)} \n'))
               
            if sweet_on > max_number_move or sweet_on > total_sweets:
                print(f'{players[0]}! {choice(message_out)}')
                chance = 2 
                while chance > 0:
                    sweet_on = int(input(f'У вас есть еще шанс, {players[0]}. {choice(message)} \n'))
                    if sweet_on <= max_number_move and sweet_on <= total_sweets:
                        total_sweets -=sweet_on
                        break
                    else:
                        chance -= 1
                if chance == 0:
                    print(f'Game over! Вы, {players[0]} {choice(message_out)}')
                    flag_out =1
                    game_over = 1
            else:
                print(f'Вы, {players[0]} взяли {sweet_on} конфет')
                total_sweets -=sweet_on
                print('')
            
        
        if total_sweets > 0:
            print(f'Осталось {total_sweets} конфет')
            flag = not flag
        else:
            print('Все конфеты разобраны.')
    print('')
    
else:        
    while total_sweets > 0 and flag_out !=1:
    
        if flag == False:
            sweet_on = int(input(f'{players[0]}, {choice(message)} \n'))
                
            if sweet_on > max_number_move or sweet_on > total_sweets:
                print(f'{players[0]}! {choice(message_out)}')
                chance = 2 
                while chance > 0:
                    sweet_on = int(input(f'У вас есть еще шанс, {players[0]}. {choice(message)} \n'))
                    if sweet_on <= max_number_move and sweet_on <= total_sweets:
                        total_sweets -=sweet_on
                        break
                    else:
                        chance -= 1
                if chance == 0:
                    print(f'Game over! Вы, {players[0]}, {choice(message_out)}')
                    flag_out =1
                    game_over = 1
            else:
                print(f'Вы, {players[0]}, взяли {sweet_on} конфет')
                total_sweets -=sweet_on
            
            
        elif flag == True:
            sweet_on = int(input(f'{players[1]}, {choice(message)} \n'))
            
            if sweet_on > max_number_move or sweet_on > total_sweets:
                print(f'{players[1]}! {choice(message_out)} ')
                chance = 2
                while chance > 0:
                    sweet_on = int(input(f'{players[1]} {choice(message)} \n'))
                    if sweet_on <= max_number_move and sweet_on <= total_sweets:
                        total_sweets -=sweet_on
                        break
                    else:
                        chance-=1
                if chance ==0:
                    print(f'Game over! Вы, {players[1]} {choice(message_out)}')
                    flag_out =1
                    game_over = 2
            else:
                print(f'Вы, {players[1]}, взяли {sweet_on} конфет')
                total_sweets -=sweet_on
            
            
        
        if total_sweets > 0:
                print(f'Осталось {total_sweets} конфет')
                flag = not flag
        else:
                print('Все конфеты разобраны.')
                # print(f'Осталось {total_sweets} конфет')
        print('')

    
if game_over !=0:
    print(f'{players[flag]}, выиграл!')
else:
    if flag == False and total_sweets <= 0:
        print(f'{players[0]}, выиграл!')
    else:
        print(f'{players[1]}, выиграл!')
