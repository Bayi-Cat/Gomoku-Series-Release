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
log = 0
user_EXP = 0
user_winstreak = 0
user_designation = 0
user_namel = 0
user_passwordl = 0
version = "ver 1.1.1 LTS"
user_describel = 0#初始变量声明
folder_path = ("user_dat")
if not os.path.exists(folder_path):
    print("警告:存档文件夹丢失/Warning: Archive folder is missing")#如果user_dat不存在，则直接弹出提醒
    os.makedirs(folder_path)
os.chdir(folder_path)#定位至存档文件夹
def checkchess(chess,count_import_chess,locationX,locationY,csizeX,csizeY):#检测是否连成五子
    originY = locationY
    originX = locationX#存储原点位置
    origin = chess[(originY - 1) * csizeX + (originX - 1)]#确认下子方
    position = 0
    count_chess = 1
    back = 0
    count = 0
    back_save = 0
    for x in range(8):
        if(count % 2 == 0):
            position += 1        
        count += 1
        back_save = back
        locationX = originX#重定位
        locationY = originY             
        while(back == back_save):
            if(position == 1):
                if(back_save == 0):
                    if(locationY != 1):locationY -= 1#移动点位进行计算
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
        if(count_chess >= 5):#满足条件后胜利
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
                print("该点为/The point is:"+chess[chess_location])
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
print("————————————————————————————————————————————————————")
print("iChess Launcher\n输入help以获得帮助/Enter help to get help")
while(quit != 0):  #循环,直到输入“quit”
    quit = 1
    print("————————————————————————————————————————————————————")
    typing = input("请输入命令/Please enter the command:") #输入部分
    print("————————————————————————————————————————————————————")
    if(typing == "help"): #输入实现
        print("help - 罗列可使用命令/Lists available commands\nver - 查看iCL版本信息/View iCL version information\nabout - 关于iChess Launcher/About iChess Launcher\nquit - 退出iCL(需先退出登录才可关闭iCL)/Log out of the iCL(You need to log out before you can disable the iCL)\nlog-in - 登录iCL账户/Log in to your iCL account\nlog-out - 退出iCL账户/Exit iCL account\nreg - 注册新的iCL账户/Register a new iCL account\nacc - 查看当前登录账户档案/View the current login account file\nstart-game - 开始游戏!/Start game!")
    elif(typing == "ver"):print("iChess Launcher(iCL)"+version)
    elif(typing == "about"):print("iChess Launcher "+version+"\n开发者:Bob, Bayi, Lang/Developers: Bob, Bayi, Lang.\n功能简介:拥有一个账户系统（包括用户名、用户密码、用户描述、用户积分、用户等级、连胜次数）,基本的五子棋功能（创建棋盘、选择方向、放置棋子、记录轮次、判定胜、负或和棋）。\nFunction Overview: Possessing an account system (including username, user password, user description, user points,user level, consecutive wins), basic Gomoku features (create board,select side, place piece, record turns,determine win, loss, or draw).")
    elif(typing == "quit"):
        if(log == 0):
            quit = 0
        else:print("请先退出登录后再退出iCL/Please log out and then log out of iCL")
    elif(typing == "reg"):
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
    elif(typing == "log-in"):
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
                log = data_name
            else:print("密码错误/wrong password")
    elif(typing == "log-out"):
        user_EXP = str(user_EXP)
        user_winstreak = str(user_winstreak)
        fp = open(f"{log}.txt",'w',encoding="UTF-8")#基本信息写入文档
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
        log = 0
        print("成功退出登录!/Log out successfully!")
    elif(typing == "acc"):
        if(log != 0):
            user_EXP = str(user_EXP)
            user_winstreak = str(user_winstreak)
            fp = open(f"{log}.txt","r",encoding="UTF-8")
            print(user_namel,end="")
            print(user_describel,end="")
            print("经验/EXP:"+user_EXP)
            print("连胜局数/Winning streak:"+user_winstreak)
            print("称号/designation:"+user_designation,end="")
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
                            else:print("你尚未登录,登录后可以记录战绩/You are not logged in yet, you can log in and record your record")
                        else:print("本局未正常结束,不记录/This session does not end normally, no record")
                    else:print("输入错误/input error")
            else:print("输入错误/input error") 
print("再见不是结束,而是新的开始。/Goodbye is not an end, but a new beginning.")