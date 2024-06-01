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
import linecache #导入/import
log = 0
user_EXP = 0
user_type = "0"
user_winstreak = 0
user_namel = 0
user_passwordl = 0
achievement_information = ["获得1点经验/Gain 1 EXP","获得10点经验/Gain 10 EXP","Gain 50 EXP","连胜3局/Win 3 straight games","连胜15局/Win 15 straight games","连胜30局/Win 30 straight games","连胜10局且经验达到25/Win 10 straight games and gain 25 EXP","连胜30局且经验达到50/Win 30 straight games and gain 50 EXP"]
achievement = ["爱棋者I","爱棋者II","爱棋者III","连战连胜I","连战连胜II","连战连胜III","棋王","棋神"]
user_achievement = []
for x in range(len(achievement)):
    user_achievement.append("0")
uachievement = 0
version = "ver 1.2.1 LTS"
user_describel = 0#初始变量声明/Initial variable declaration
folder_path = ("user_dat")
if not os.path.exists(folder_path):
    print("警告:存档文件夹丢失/Warning: Archive folder is missing")#如果user_dat不存在，则直接弹出提醒/If user_dat does not exist, a reminder is displayed
    os.makedirs(folder_path)
os.chdir(folder_path)#定位至存档文件夹/Locate to the archive folder
def achievement_check(exp,winstreak,achievement):
    print("————————————————————————————————————————————————————")
    if(exp >= 1 and achievement[0] == "0"):
        achievement[0] = "1"
        print("解锁成就:爱棋者I/Unlock Achievement: Chess Lover I\n获得1点经验/Gain 1 EXP")
    if(exp >= 10 and achievement[1] == "0"):
        achievement[1] = "1"
        print("解锁成就:爱棋者II/Unlock Achievement: Chess Lover II\n获得10点经验/Gain 10 EXP")
    if(exp >= 50 and achievement[2] == "0"):
        achievement[2] = "1"
        print("解锁成就:爱棋者III/Unlock Achievement: Chess Lover III\n获得50点经验/Gain 50 EXP")
    if(winstreak >= 3 and achievement[3] == "0"):
        achievement[3] = "1"
        print("解锁成就:连战连胜I/Unlock Achievement: Consecutive Wins I\n连胜3局/Win 3 straight games")
    if(winstreak >= 15 and achievement[4] == "0"):
        achievement[4] = "1"
        print("解锁成就:连战连胜II/Unlock Achievement: Consecutive Wins II\n连胜15局/Win 15 straight games")
    if(winstreak >= 30 and achievement[5] == "0"):
        achievement[5] = "1"
        print("解锁成就:连战连胜III/Unlock Achievement: Consecutive Wins III\n连胜30局/Win 30 straight games")
    if(winstreak >= 10 and exp >= 25 and achievement[6] == "0"):
        achievement[6] = "1"
        print("解锁成就:棋王/Unlock Achievement: Champion Chess Player\n连胜10局且经验达到25/Win 10 straight games and gain 25 EXP")
    if(winstreak >= 30 and exp >= 50 and achievement[7] == "0"):
        achievement[7] = "1"
        print("解锁成就:棋神/Unlock Achievement: Chess God\n连胜30局且经验达到50/Win 30 straight games and gain 50 EXP")
def checkchess(chess,count_import_chess,locationX,locationY,csizeX,csizeY):#检测是否连成五子/Test for penta
    originY = locationY
    originX = locationX#存储原点位置/Memory origin location
    origin = chess[(originY - 1) * csizeX + (originX - 1)]#确认下子方/Confirm subsquare
    position = 0
    count_chess = 1
    back = 0
    count = 0
    back_save = 0#初始设置/initial setting
    for x in range(8):
        if(count % 2 == 0):
            position += 1        
        count += 1
        back_save = back
        locationX = originX#重定位/relocate
        locationY = originY             
        while(back == back_save):
            if(position == 1):
                if(back_save == 0):
                    if(locationY != 1):locationY -= 1#移动点位进行计算/Move the point for calculation
                    else:back = 1
                else:
                    if(locationY != csizeY):locationY += 1
                    else:back = 0
            elif(position == 2): 
                if(back_save == 0):
                    if(locationX != 1):locationX -= 1
                    else:back = 1
                else:
                    if(locationX != csizeX):locationX += 1
                    else:back = 0
            elif(position == 3): 
                if(back_save == 0):
                    if(locationX != 1 and locationY != 1):
                        locationX -= 1
                        locationY -= 1
                    else:back = 1
                else:
                    if(locationX != csizeX and locationY != csizeY):
                        locationX += 1
                        locationY += 1
                    else:back = 0
            else: 
                if(back_save == 0):
                    if(locationX != csizeX and locationY != 1):
                        locationX += 1
                        locationY -= 1
                    else:back = 1
                else:
                    if(locationX != 1 and locationY != csizeY):
                        locationX -= 1
                        locationY += 1
                    else:back = 0
            if(back == back_save):
                if(chess[(locationY - 1) * csizeX + (locationX - 1)] == origin):
                    count_chess += 1
                else:
                    if(back_save == 1):
                        back = 0
                    else:back = 1
            else:break
        if(count_chess >= 5):#满足条件后胜利/Victory after meeting the conditions
            if(origin == "X"):
                print("X方胜利!/X victory!")
                count_import_chess[0] = 1
            else:
                print("O方胜利!/O victory!")
                count_import_chess[0] = 0
            break
        else:
            if(back_save == 1):
                count_chess = 1
    return 0                               
def normal_chess(chess_sizeX,chess_sizeY,count_import_chess):
    print("————————————————————————————————————————————————————")
    chess = []
    for x in range(chess_sizeX * chess_sizeY):
        chess.append("#")
    round = 0
    chess_location = 0
    while(count_import_chess[0] == 2):
        if(round == len(chess)):
            print("平局!/Draw!")
            break
        round += 1
        count_numberX = 0
        count_numberY = 0
        for x in range(chess_sizeY + 1):#打印棋盘/Print board
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
        round = int(round)
        round = str(round)
        print("第"+round+"回合/Round"+round)
        round = float(round)
        if(round % 2 == 1):
            print("X方开始行动/X is in action")
        else:print("O方开始行动/O is in action")
        try:#开始下子/Get started
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
                print("该点为/The point is:"+chess[chess_location])
            except IndexError:
                    print("游戏崩溃了!/The game crashed!\n原因:超出棋盘范围/Cause: Out of board range")
                    break
            else:
                chess_location = (locationY - 1) * chess_sizeX + (locationX - 1)
                if(chess[chess_location] == "#"):
                    if(round % 2 == 0):
                        chess[chess_location] = "O"
                    else:chess[chess_location] = "X"
                    checkchess(chess,count_import_chess,locationX,locationY,chess_sizeX,chess_sizeY)
                else:
                    print("游戏崩溃了!/The game crashed!\n原因:此处已下子/Cause: The following operations have been performed")
                    break
    count_numberX = 0
    count_numberY = 0
    for x in range(chess_sizeY + 1):#打印棋盘/Print board
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
    return 0
print("————————————————————————————————————————————————————")
print("iChess Launcher\n输入help以获得帮助/Enter help to get help")
while(quit != 0):  #循环,直到输入“quit”/Loop until you type "quit"
    quit = 1
    print("————————————————————————————————————————————————————")
    typing = input("请输入命令/Please enter the command:") #输入部分/input section
    print("————————————————————————————————————————————————————")
    if(typing == "help"): #输入实现/Input implementation
        print("help - 罗列可使用命令/Lists available commands\nver - 查看iCL版本信息/View iCL version information\nabout - 关于iChess Launcher/About iChess Launcher\nquit - 退出iCL(需先退出登录才可关闭iCL)/Log out of the iCL(You need to log out before you can disable the iCL)\nlog-in - 登录iCL账户/Log in to your iCL account\nlog-out - 退出iCL账户/Exit iCL account\nreg - 注册新的iCL账户/Register a new iCL account\nacc - 查看当前登录账户档案/View the current login account file\nstart-game - 开始游戏!/Start game!\nachievement - 查看成就解锁进度/View the achievement unlocking progress")
    elif(typing == "ver"):print("iChess Launcher(iCL)"+version)
    elif(typing == "about"):print("iChess Launcher "+version+"\n开发者:Bob, Bayi, Lang/Developers: Bob, Bayi, Lang.\n功能简介:拥有一个账户系统（包括用户名、用户密码、用户描述、用户积分、用户等级、连胜次数）,基本的五子棋功能（创建棋盘、选择方向、放置棋子、记录轮次、判定胜、负或和棋）。\nFunction Overview: Possessing an account system (including username, user password, user description, user points,user level, consecutive wins), basic Gomoku features (create board,select side, place piece, record turns,determine win, loss, or draw).")
    elif(typing == "quit"):
        if(log == 0):
            quit = 0
        else:print("请先退出登录后再退出iCL/Please log out and then log out of iCL")
    elif(typing == "reg"):
        user_name = input("请输入账户名/Please enter your account name:")#输入用户名/Enter username
        if(user_name == ""):
            print("不能输入空字符,已自动退出注册/Null characters cannot be entered. The registration is automatically exited")
        else:
            user_password = input("请输入账户密码/Please enter your account password:")
            user_describe = input("给自己写段介绍吧/Write yourself an introduction:")
            select_type = input("要允许KitOS使用此账号吗?(0 - 是 | 1 - 否)/Do you want to allow KitOS to use this account? (0 - yes | 1 - no):")
            if(select_type == "0" or select_type == "1"):
                print("设置成功!/successfully set!")
            else:
                print("输入错误,默认为可以/Input error, the default is yes")
                select_type = "0"
            print("正在生成存档…/Generating an archive…")
            log = 0
            fp = open(f"{user_name}.txt",'w',encoding="UTF-8")#基本信息写入文档/Write basic information to the document
            if(select_type == "0"):
                fp.write("iChess/Kit\ntype:\n")
            else:fp.write("iChess\ntype:\n")
            fp.write(user_name+"\nname:\n")
            fp.write(user_password+"\npassword:\n")
            if(user_describe != ""):#介绍判断,没写介绍则写入默认内容/If no introduction is written, the default content is written
                fp.write(user_describe)
            else:fp.write("留白是世间最美的艺术。/Blank space is the most beautiful art in the world.")
            fp.write("\ndescribe:")
            fp.write("\n0\nEXP:")
            fp.write("\n0\nwin_streak:\n")
            for x in range(len(achievement)):
                fp.write("0")
            fp.write("\nachievement:")
            fp.flush()
            fp.close
            print("注册成功!/registered successfully")
    elif(typing == "log-in"):
        if(log == 0):
            data_name = input("请输入账户名/Please enter your account name:")
            try:#防止输入不存在账户/Prevents entering accounts that do not exist
                fp = open(f"{data_name}.txt","r",encoding="UTF-8")
            except FileNotFoundError:
                print("未找到此存档/This archive was not found")
            else:
                print("————————————————————————————————————————————————————")
                linecache.checkcache(f"{data_name}.txt")
                user_type = linecache.getline(f"{data_name}.txt",1)
                user_namel = linecache.getline(f"{data_name}.txt",3)#基本信息覆盖/Basic information overlay
                user_passwordl = linecache.getline(f"{data_name}.txt",5)
                user_describel = linecache.getline(f"{data_name}.txt",7)
                user_EXP = linecache.getline(f"{data_name}.txt",9)
                user_winstreak = linecache.getline(f"{data_name}.txt",11)
                uachievement = linecache.getline(f"{data_name}.txt",13)
                count_achievement = 0
                user_EXP = str(user_EXP)
                user_winstreak = str(user_winstreak)
                fp = open(f"{data_name}.txt","r",encoding="UTF-8")
                print(user_namel,end="")
                print(user_describel,end="")
                print("经验/EXP:"+user_EXP,end="")
                print("连胜局数/Winning streak:"+user_winstreak,end="")
                user_EXP = int(user_EXP)
                user_winstreak = int(user_winstreak)
                contents = linecache.getline(f"{data_name}.txt",5)
                print("————————————————————————————————————————————————————")
                user_password = input("请输入密码/enter your password:")
                if(user_password+"\n" == contents):
                    for x in range(len(uachievement) - 1):
                        user_achievement[count_achievement] = uachievement[count_achievement]
                        count_achievement += 1
                    user_EXP = int(user_EXP)
                    user_winstreak = int(user_winstreak)
                    print("登录成功!/login successfully!")
                    log = data_name
                else:print("密码错误/wrong password")
        else:print("请先退出登录后使用/Please log out before using")
    elif(typing == "log-out"):
        if(log != 0):
            user_EXP = str(user_EXP)
            user_winstreak = str(user_winstreak)
            fp = open(f"{log}.txt",'w',encoding="UTF-8")#基本信息写入文档/Write basic information to the document
            fp.write(user_type+"type:\n")
            fp.write(user_namel+"name:")
            fp.write("\n"+user_passwordl+"password:")
            if(user_describel != ""):#介绍判断,没写介绍则写入默认内容/If no introduction is written, the default content is written
                fp.write("\n"+user_describel)
            else:fp.write("留白是世间最美的艺术。/Blank space is the most beautiful art in the world.")
            fp.write("describe:")
            fp.write("\n"+user_EXP+"\nEXP:")
            fp.write("\n"+user_winstreak+"\nwin_streak:\n")
            count_achievement = 0
            uachievement = ""
            for x in range(len(user_achievement)):
                temp = user_achievement[count_achievement]
                uachievement = uachievement + temp
                count_achievement += 1
            fp.write(uachievement)
            fp.write("\nachievement:")
            fp.flush()
            fp.close
            log = 0
            print("成功退出登录!/Log out successfully!")
        else:print("还未登录，不可退出登录/You cannot log out if you have not logged in")
    elif(typing == "acc"):
        if(log != 0):
            user_EXP = str(user_EXP)
            user_winstreak = str(user_winstreak)
            fp = open(f"{log}.txt","r",encoding="UTF-8")
            print(user_namel,end="")
            print(user_describel,end="")
            print("经验/EXP:"+user_EXP)
            print("连胜局数/Winning streak:"+user_winstreak)
            user_EXP = int(user_EXP)
            user_winstreak = int(user_winstreak)
        else:
            print("当前未登录,请在登录后重试/You are not currently logged in, please try again after login")
    elif(typing == "start-game"):
        try:
            chess_sx = int(input("请输入棋盘长度(输入5~150整数)/Please enter the length of the board (enter 5~150 integers):"))
        except ValueError:
            print("输入错误/input error") 
        else:
            if(chess_sx >= 5 and chess_sx <= 150):
                try:
                    chess_sy = int(input("请输入棋盘宽度(输入5~150整数)/Please enter the board width (enter 5~150 integers):"))
                except ValueError:
                    print("输入错误/input error") 
                else:
                    if(chess_sy >= 5 and chess_sy <= 150):
                        if(log != 0):
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
                                achievement_check(user_EXP,user_winstreak,user_achievement)
                            else:print("你尚未登录,登录后可以记录战绩/You are not logged in yet, you can log in and record your record")
                        else:print("本局未正常结束,不记录/This session does not end normally, no record")
                    else:print("输入错误/input error")
            else:print("输入错误/input error") 
    elif(typing == "achievement"):
        if(log != 0):
            select_achievement = 0
            for x in range(len(achievement)):
                print(achievement[select_achievement]+"\n"+achievement_information[select_achievement])
                if(user_achievement[select_achievement] == "1"):
                    print("已达成!/You did it!\n")
                else:print("未达成!/More effort!\n")
                select_achievement += 1
        else:print("你尚未登录，登录后可以查看成就/You are not logged in yet, so you can view your achievements when you log in")
print("再见不是结束,而是新的开始。/Goodbye is not an end, but a new beginning.")
input("按下回车退出/Press Enter to exit:")
