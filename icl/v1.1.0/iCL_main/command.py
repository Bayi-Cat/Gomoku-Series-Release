"""
iChess Launcher(iCL)
A command-line Gomoku (Five in a Row) program.
- Functionality: Possessing an account system (including username, user password, user description, user points,user level, consecutive wins), basic Gomoku features (create board,select side, place piece, record turns, determine win, loss, or draw).
- Developers: Bob, Bayi, Lang.
- Dependencies: None.
- Usage Instructions: How to run or use the program.
    Example Usage:
    python3 command.py
Note: Please ensure that the Python interpreter is installed before running this program.
"""
import os
import linecache #导入
acc_select = 0
user_EXP = 0
user_winstreak = 0
user_designation = 0
user_namel = 0
user_passwordl = 0
version = "1.1.0"
user_describel = 0#初始变量声明
folder_path = ("user_dat")
os.chdir(folder_path)#定位至存档文件夹
def checkchess(chess,count_import_chess,lX,lY,csizeX,csizeY):#检测是否连成五子
    save2 = lY
    save3 = lX#存储原点位置
    save = chess[(save2 - 1) * csizeX + (save3 - 1)]#确认下子方
    position = 0
    count_chess = 1
    back = 0
    for x in range(8):
        position += 1
        if(position == 1):
            lX = save3#重定位
            lY = save2                
            while(back == 0):
                if(lY != 1):
                    lY -= 1#移动点位进行计算
                    if(chess[(lY - 1) * csizeX + (lX - 1)] == save):
                        count_chess += 1
                    else:back = 1
                else:back = 1
            if(count_chess >= 5):#满足条件后胜利
                if(save == "X"):
                    print("X方胜利!/X victory!")
                    count_import_chess[0] = 1
                else:
                    print("O方胜利!/O victory!")
                    count_import_chess[0] = 0
                break
        if(position == 2):
            lX = save3
            lY = save2
            while(back == 1):
                if(lY != csizeY):
                    lY += 1
                    if(chess[(lY - 1) * csizeX + (lX - 1)] == save):
                        count_chess += 1
                    else:back = 0
                else:back = 0                  
            if(count_chess >= 5):
                if(save == "X"):
                    print("X方胜利!/X victory!")
                    count_import_chess[0] = 1
                else:
                    print("O方胜利!/O victory!")
                    count_import_chess[0] = 0
                break
            else:count_chess = 1  
        if(position == 3):
            lX = save3
            lY = save2                
            while(back == 0):
                if(lX != 1):
                    lX -= 1
                    if(chess[(lY - 1) * csizeX + (lX - 1)] == save):
                        count_chess += 1
                    else:back = 1
                else:back = 1
            if(count_chess >= 5):
                if(save == "X"):
                    print("X方胜利!/X victory!")
                    count_import_chess[0] = 1
                else:
                    print("O方胜利!/O victory!")
                    count_import_chess[0] = 0
                break
        if(position == 4):
            lX = save3
            lY = save2
            while(back == 1):
                if(lX != csizeX):
                    lX += 1
                    if(chess[(lY - 1) * csizeX + (lX - 1)] == save):
                        count_chess += 1
                    else:back = 0
                else:back = 0                  
            if(count_chess >= 5):
                if(save == "X"):
                    print("X方胜利!/X victory!")
                    count_import_chess[0] = 1
                else:
                    print("O方胜利!/O victory!")
                    count_import_chess[0] = 0
                break
            else:count_chess = 1 
        if(position == 5):
            lX = save3
            lY = save2                
            while(back == 0):
                if(lX != 1 and lY != 1):
                    lX -= 1
                    lY -= 1
                    if(chess[(lY - 1) * csizeX + (lX - 1)] == save):
                        count_chess += 1
                    else:back = 1
                else:back = 1
            if(count_chess >= 5):
                if(save == "X"):
                    print("X方胜利!/X victory!")
                    count_import_chess[0] = 1
                else:
                    print("O方胜利!/O victory!")
                    count_import_chess[0] = 0
                break
        if(position == 6):
            lX = save3
            lY = save2
            while(back == 1):
                if(lX != csizeX and lY != csizeY):
                    lX += 1
                    lY += 1
                    if(chess[(lY - 1) * csizeX + (lX - 1)] == save):
                        count_chess += 1
                    else:back = 0
                else:back = 0                  
            if(count_chess >= 5):
                if(save == "X"):
                    print("X方胜利!/X victory!")
                    count_import_chess[0] = 1
                else:
                    print("O方胜利!/O victory!")
                    count_import_chess[0] = 0
                break
            else:count_chess = 1 
        if(position == 7):
            lX = save3
            lY = save2                
            while(back == 0):
                if(lX != csizeX and lY != 1):
                    lX += 1
                    lY -= 1
                    if(chess[(lY - 1) * csizeX + (lX - 1)] == save):
                        count_chess += 1
                    else:back = 1
                else:back = 1
            if(count_chess >= 5):
                if(save == "X"):
                    print("X方胜利!/X victory!")
                    count_import_chess[0] = 1
                else:
                    print("O方胜利!/O victory!")
                    count_import_chess[0] = 0
                break
        if(position == 8):
            lX = save3
            lY = save2
            while(back == 1):
                if(lX != 1 and lY != csizeY):
                    lX -= 1
                    lY += 1
                    if(chess[(lY - 1) * csizeX + (lX - 1)] == save):
                        count_chess += 1
                    else:back = 0
                else:back = 0              
            if(count_chess >= 5):
                if(save == "X"):
                    print("X方胜利!/X victory!")
                    count_import_chess[0] = 1
                else:
                    print("O方胜利!/O victory!")
                    count_import_chess[0] = 0
                break
            else:count_chess = 1
    return 0                               
def normal_chess(chess_sizeX,chess_sizeY,count_import_chess):
    chess = []
    for x in range(chess_sizeX * chess_sizeY):
        chess.append("#")
    round = 0
    turn = 0
    chess_location = 0
    while(count_import_chess[0] == 2):
        if(round == len(chess) + 1):
            print("平局!/Draw!")
            break
        round += 1
        if(turn == 0):
            turn = 1
        else:turn = 0
        count_numberX = 0
        count_numberY = 0
        for x in range(chess_sizeY + 1):#打印棋盘
            for x in range(chess_sizeX + 1):
                if(count_numberY == 0):
                    if(count_numberX == chess_sizeX):
                        print(count_numberX % 10)
                    else:print(count_numberX % 10,end="")
                else:
                    if(count_numberX == 0):
                        print(count_numberY % 10,end="")
                    else:
                        if(count_numberX != chess_sizeX):
                            print(chess[(count_numberX - 1) + (count_numberY - 1) * chess_sizeX],end="")
                        else:print(chess[(count_numberX - 1) + (count_numberY - 1) * chess_sizeX])
                count_numberX += 1
            count_numberY += 1
            count_numberX = 0
        round = str(round)
        print("第"+round+"回合/Round"+round)
        round = int(round)
        try:#开始下子
            print("输入下子点X坐标/Enter the sub-point X coordinates")
            locationX = int(input("请输入整数/Please enter an integer:"))
            print("输入下子点Y坐标/Enter the subpoint Y coordinates")
            locationY = int(input("请输入整数/Please enter an integer:"))
        except ValueError:
            print("游戏崩溃了!/The game crashed!\n原因:输入值错误/Cause: The input value is incorrect")
            break
        else:
            try:
                if(locationX > chess_sizeX or locationY > chess_sizeY):
                    locationX = 1145
                    locationY = 1919
                chess_location = (locationY - 1) * chess_sizeX + (locationX - 1)
                print("该点为:"+chess[chess_location])
            except IndexError:
                    print("游戏崩溃了!/The game crashed!\n原因:超出棋盘范围/Cause: Out of board range")
                    break
            else:
                chess_location = (locationY - 1) * chess_sizeX + (locationX - 1)
                if(chess[chess_location] == "#"):
                    if(turn == 0):
                        chess[chess_location] = "O"
                    else:chess[chess_location] = "X"
                    checkchess(chess,count_import_chess,locationX,locationY,chess_sizeX,chess_sizeY)
                else:
                    print("游戏崩溃了!/The game crashed!\n原因:此处已下子/Cause: The following operations have been performed")
                    break
    return 0
print("iChess Launcher\n输入help以获得帮助/Enter help to get help")
while(quit != 0):  #循环,直到输入“quit”
    quit = 1
    typing = input("请输入命令/Please enter the command:") #输入部分
    if(typing == "help"): #输入实现
        print("help - 罗列可使用命令/Lists available commands\nver - 查看iCL版本信息/View iCL version information\nabout - 关于iChess Launcher/About iChess Launcher\nquit - 退出iCL(需先退出登录才可关闭iCL)/Log out of the iCL(You need to log out before you can disable the iCL)\nacc-in - 登录iCL账户/Log in to your iCL account\nacc-out - 退出iCL账户/Exit iCL account\nacc-new - 注册新的iCL账户/Register a new iCL account\nacc - 查看当前登录账户档案/View the current login account file\nstart-game - 开始游戏!/Start game!")
    elif(typing == "ver"):print("iChess Launcher(iCL)"+version)
    elif(typing == "about"):print("iChess Launcher "+version+" LTS\n开发者:Bob, Bayi, Lang/Developers: Bob, Bayi, Lang.\n功能简介:拥有一个账户系统（包括用户名、用户密码、用户描述、用户积分、用户等级、连胜次数）,基本的五子棋功能（创建棋盘、选择方向、放置棋子、记录轮次、判定胜、负或和棋）。\nFunction Overview: Possessing an account system (including username, user password, user description, user points,user level, consecutive wins), basic Gomoku features (create board,select side, place piece, record turns,determine win, loss, or draw).")
    elif(typing == "quit"):
        if(acc_select == 0):
            quit = 0
        else:print("请先退出登录后再退出iCL/Please log out and then log out of iCL")
    elif(typing == "acc-new"):
        print("请输入账户名/Please enter your account name")
        user_name = input("")#输入用户名
        if(user_name == ""):
            print("不能输入空字符,已自动退出注册/Null characters cannot be entered. The registration is automatically exited")
        else:
            print("请输入账户密码/Please enter your account password")
            user_password = input("")
            print("给自己写段介绍吧/Write yourself an introduction")
            user_describe = input("")
            fp = open(f"{user_name}.txt",'w',encoding="UTF-8")#基本信息写入文档
            fp.write(user_name+"\nname:\n")
            fp.write(user_password+"\npassword:\n")
            if(user_describe != ""):#介绍判断,没写介绍则写入默认内容
                fp.write(user_describe)
            else:fp.write("留白是世间最美的艺术。/Blank space is the most beautiful art in the world.")
            fp.write("\ndescribe:")
            fp.write("\n0\nEXP:")
            fp.write("\n0\nwin_streak:")
            fp.write("\n新人\ndesignation:")
            fp.flush()
            fp.close
            print("注册成功!/registered successfully")
    elif(typing == "acc-in"):
        data_name = input("请输入账户名/Please enter your account name:")
        try:#防止输入不存在账户
            fp = open(f"{data_name}.txt","r",encoding="UTF-8")
        except FileNotFoundError:
            print("未找到此存档/This archive was not found")
        else:
            contents = linecache.getline(f"{data_name}.txt",3)
            user_password = input("请输入密码/enter your password:")
            if(user_password+"\n" == contents):
                linecache.checkcache(f"{data_name}.txt")
                user_namel = linecache.getline(f"{data_name}.txt",1)#基本信息覆盖
                user_passwordl = linecache.getline(f"{data_name}.txt",3)
                user_describel = linecache.getline(f"{data_name}.txt",5)
                user_EXP = linecache.getline(f"{data_name}.txt",7)
                user_winstreak = linecache.getline(f"{data_name}.txt",9)
                user_designation = linecache.getline(f"{data_name}.txt",11)
                user_EXP = int(user_EXP)
                user_winstreak = int(user_winstreak)
                print("登录成功!/login successfully!")
                acc_select = data_name
            else:print("密码错误/wrong password")
    elif(typing == "acc-out"):
        user_EXP = str(user_EXP)
        user_winstreak = str(user_winstreak)
        fp = open(f"{acc_select}.txt",'w',encoding="UTF-8")#基本信息写入文档
        fp.write(user_namel+"name:")
        fp.write("\n"+user_passwordl+"password:")
        if(user_describel != ""):#介绍判断,没写介绍则写入默认内容
            fp.write("\n"+user_describel)
        else:fp.write("留白是世间最美的艺术。/Blank space is the most beautiful art in the world.")
        fp.write("describe:")
        fp.write("\n"+user_EXP+"\nEXP:")
        fp.write("\n"+user_winstreak+"\nwin_streak:")
        fp.write("\n"+user_designation+"designation:")
        fp.flush()
        fp.close
        acc_select = 0
        print("成功退出登录!/Log out successfully!")
    elif(typing == "acc"):
        if(acc_select != 0):
            user_EXP = str(user_EXP)
            user_winstreak = str(user_winstreak)
            fp = open(f"{acc_select}.txt","r",encoding="UTF-8")
            print(user_namel,end="")
            print(user_describel,end="")
            print("经验/EXP:"+user_EXP)
            print("连胜局数/Winning streak:"+user_winstreak)
            print("称号/designation:"+user_designation)
            user_EXP = int(user_EXP)
            user_winstreak = int(user_winstreak)
        else:
            print("当前未登录,请在登录后重试/You are not currently logged in, please try again after login")
    elif(typing == "start-game"):
        chess_sx = int(input("请输入棋盘长度(输入5~150整数)/Please enter the length of the board (enter 5~150 integers):"))
        if(chess_sx >= 5 and chess_sx <= 150):
                chess_sy = int(input("请输入棋盘宽度(输入5~150整数)/Please enter the board width (enter 5~150 integers):"))
                if(chess_sy >= 5 and chess_sy <= 150):
                    if(acc_select != 0):
                        chess_choser = input("请输入你的阵营(X或O)/Please enter your camp (X or O):")
                        if(chess_choser == "O" or chess_choser == "X"):
                            if(chess_choser == "O"):
                                chess_choser = 0
                            else:chess_choser = 1
                        else:
                            chess_choser = 0
                            print("输入错误,已默认为O/Input error, the default is O")
                    else:chess_choser = 2
                    win = [2]
                    normal_chess(chess_sx,chess_sy,win)
                    if(win[0] != 2):
                        if(chess_choser != 2):
                            if(win[0] == chess_choser):
                                print("胜利!/Victory!")
                                user_EXP += 1
                                user_winstreak += 1
                            else:
                                print("失败!/Defeat!")
                                user_winstreak = 0
                        else:print("你尚未登录,登录后可以记录战绩/You are not logged in yet, you can log in and record your record")
                    else:print("本局未正常结束,不记录/This session does not end normally, no record")
                else:print("输入错误/input error")
        else:print("输入错误/input error") 
    elif(typing == "nice" or typing == "试卷毁灭者" or typing == "I blew up" or typing == "备胎" or typing == "star"):
        if(typing == "I blew up"):print("还没记完，我炸了！")
        if(typing == "nice"):print("寄完了，赖氏！")
        if(typing == "试卷毁灭者"):print("呃，问一下，我没有语文寒假作业的第1、2页，谁有请发一下，谢谢。")
        if(typing == "备胎"):print("你个备胎就别说话了")
        if(typing == "star"):print("'Star'这个词有多重含义，主要如下：\n1. 天文学上的星体：\n•恒星（如太阳）：指宇宙中自身发光发热的气体球，通过核反应产生能量。\n•星星：泛指夜空中可见的天体，包括行星、恒星、流星等，但通常非专业情况下指的是恒星。\n2. 象征意义：\n•命运；走运的阶段：常用于表达个人的运势或时期，如“他的星运正旺”。\n•理想；希望：如“指路的明星”，比喻指引方向的目标或理想。\n3. 名人与杰出人物：\n•明星，名角，名家：在娱乐、体育、艺术等领域中非常有名或才华出众的人。\n•电影明星、歌星等：特指在影视、音乐等行业中的知名人士。\n4. 符号与形状：\n•星形物：任何星形的物体或图案，如装饰品、图标等。\n•星号（*）：用于标示、强调或作为评分系统的一部分。\n5. 其他特定用法：\n•（美军的）星章：军衔标志中使用的星形徽章。\n•海星：海洋生物，属于棘皮动物门。\n•（旅馆或餐馆的）星级：评价服务质量和奢华程度的标准。\n•特定名称或地名：如瑞典的斯塔尔，德国的施塔尔，美国得克萨斯州的别称“孤星州”。\n此外，“star”在语法上可用作名词、形容词、及物动词和不及物动词，具有不同的用法和变形，如主演（to star in a movie）、出名（to become a star）、星形的（star-shaped）。")
print("再见不是结束,而是新的开始。/Goodbye is not an end, but a new beginning.")