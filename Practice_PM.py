import random

#region 输入玩家
def set_player_count():
    '''
    至少要有两位玩家
    '''
    while (True):
        player_count = input("玩家人数：")
        if (not player_count.isdigit()):
            print("请输入数字！")
        elif (int(player_count) < 2):
            print("至少要有2位玩家！")
        else:
            return int(player_count)


def set_player_name(player_count):
    '''
    用字典Dictionary记录玩家的名字和初始分数
    玩家名字不该重复
    '''
    players = {}

    for count in range(player_count):
        while (True):
            player = input("输入玩家{}名字：".format(count + 1))
            if (player == "" or player.isspace()):
                print("请输入玩家名字！")
            elif (players.__contains__(player)):
                print("玩家名字重复！")
            else:
                players[player] = 0
                break

    return players
#endregion


#region 设置游戏
def set_game_limit():
    '''
    游戏条件：
    1. 下限和上限都是整数
    2. 上限大于下限
    3. 上限与下限之前至少要有3个整数
    '''
    while (True):
        lower_limit = input("最低值：")
        upper_limit = input("最高值：")

        #TODO：输入正确的条件
        if ():
            print("请输入数字！")
        elif ():
            print("上限必需大于下限！")
        elif ():
            print("上限与下限之间至少要有3个数字！")
        else:
            return int(lower_limit), int(upper_limit)


def set_answer(lower_limit, upper_limit):
    # 用random随机抽取一个号码
    return random.randint(lower_limit + 1, upper_limit - 1)
#endregion


#region 游戏逻辑
def start_game(answer, lower_limit, upper_limit, players):
    '''
    主要游戏流程：
    1. 从第一位玩家开始
    2. 玩家猜一个号码
    3. 验证号码，要是号码无效就回到[2]
    4. 检查号码和终极密码是不是一样，一样就去到[5]，否则去[6]
    5. 除了目前玩家，其他玩家都得分，游戏结束
    6. 更新上下限
    7. 轮到下一位玩家，要是没有下一位玩家就轮回第一位玩家
    8. 回到[2]
    '''
    #使用下行来Debug
    #print("answer:{}".format(answer))
    while(True):
        for player in players:
            print()
            print("---玩家[{}]的回合---".format(player))

            # 玩家猜一个号码
            while (True):
                guess_input = input("请从[{0}]到[{1}]之间选择一个数字：".format(lower_limit, upper_limit))
                if (not is_guess_valid(guess_input, lower_limit, upper_limit)):
                    print("无效的数字！")
                else:
                    break

            guess = int(guess_input)
            # 检查号码和终极密码是不是一样
            #TODO: 用现有的函数Function得到条件
            if ():
                print("太倒霉了！玩家[{}]说中终极密码了。。。".format(player))
                print("除了玩家[{}]以外的玩家都获得一分！".format(player))
                #TODO：用现有的函数Function，给除了输家以外的玩家加分
                                
                return
            else:
                print("玩家[{}]安全度过这回合！".format(player))
                #TODO：用现有的函数Function更新上下限
                                
                print("新的范围是[{0}]到[{1}]！".format(lower_limit, upper_limit))


def is_guess_valid(guess_input, lower_limit, upper_limit):
    '''
    有效输入的条件：
    1. 是整数
    2. 大于下限
    3. 小于上限
    '''
    #TODO：输出正确的布林
    
    return


def is_guess_matched(guess, answer):
    '''
    检查号码和终极密码是不是一样
    '''
    #TODO：输出正确的布林

    return


def update_limit(guess, answer, lower_limit, upper_limit):
    '''
    如果号码小于终极密码，更新下限
    否则，更新上限
    '''

    #TODO 更新上下限

    return lower_limit, upper_limit


def add_point(players, loser):
    '''
    除了输家以外的玩家都获得1分
    '''
    
    #TODO: 填进正确的条件
    
    #TODO：如何加分？

#endregion


#region 总结成绩
def show_winner(players):
    '''
    赢家可能多过一个
    只要有最高分数的都是赢家
    '''
    print("===玩家得分===")
    for player in players:
        print("玩家[{0}]：{1}分".format(player, players[player]))

    print()
    print("===获胜玩家===")

    #TODO: 列出赢家的名字

#endregion


def __main__():
    player_count = set_player_count()
    players = set_player_name(player_count)

    print()
    print("----------------------------------")
    print()

    while(True):
        print("===设置上下限===")
        lower_limit, upper_limit = set_game_limit()
        answer = set_answer(lower_limit, upper_limit)

        print()
        print("===游戏开始===")
        start_game(answer, lower_limit, upper_limit, players)
        print("===游戏结束===")
        print()

        next_game = input("再玩一场？ (Y/N) ")
        if (next_game == "N" or next_game == "n"):
            show_winner(players)
            print()
            print("----------------------------------")
            break


__main__()
