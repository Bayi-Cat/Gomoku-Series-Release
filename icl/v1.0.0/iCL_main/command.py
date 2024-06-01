import os
import linecache #导入
acc_select = 0
user_EXP = 0
user_winstreak = 0
user_designation = 0
user_namel = 0
user_passwordl = 0
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
                    print("X方胜利！")
                    count_import_chess[0] = 1
                else:
                    print("O方胜利！")
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
                    print("X方胜利！")
                    count_import_chess[0] = 1
                else:
                    print("O方胜利！")
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
                    print("X方胜利！")
                    count_import_chess[0] = 1
                else:
                    print("O方胜利！")
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
                    print("X方胜利！")
                    count_import_chess[0] = 1
                else:
                    print("O方胜利！")
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
                    print("X方胜利！")
                    count_import_chess[0] = 1
                else:
                    print("O方胜利！")
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
                    print("X方胜利！")
                    count_import_chess[0] = 1
                else:
                    print("O方胜利！")
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
                    print("X方胜利！")
                    count_import_chess[0] = 1
                else:
                    print("O方胜利！")
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
                    print("X方胜利！")
                    count_import_chess[0] = 1
                else:
                    print("O方胜利！")
                    count_import_chess[0] = 0
                break
            else:count_chess = 1
    return 0                               
def normal_chess(chess_sizeX,chess_sizeY):
    chess = []
    for x in range(chess_sizeX * chess_sizeY):
        chess.append("#")
    round = 0
    turn = 0
    chess_location = 0
    count_import_chess = [2]
    while(count_import_chess[0] == 2):
        if(round == len(chess) + 1):
            print("平局！")
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
        print("第"+round+"回合。")
        round = int(round)
        try:#开始下子
            print("输入下子点X坐标。")
            locationX = int(input("请输入整数。"))
            print("输入下子点Y坐标。")
            locationY = int(input("请输入整数。"))
        except ValueError:
            print("游戏崩溃了！\n原因：输入值错误。")
            break
        else:
            try:
                if(locationX > chess_sizeX or locationY > chess_sizeY):
                    locationX = 1145
                    locationY = 1919
                chess_location = (locationY - 1) * chess_sizeX + (locationX - 1)
                print(chess[chess_location])
            except IndexError:
                    print("游戏崩溃了！\n原因：超出棋盘范围。")
                    break
            else:
                chess_location = (locationY - 1) * chess_sizeX + (locationX - 1)
                if(chess[chess_location] == "#"):
                    if(turn == 0):
                        chess[chess_location] = "O"
                    else:chess[chess_location] = "X"
                    checkchess(chess,count_import_chess,locationX,locationY,chess_sizeX,chess_sizeY)
                else:
                    print("游戏崩溃了！\n原因：此处已下子。")
                    break
    result(count_import_chess,chess_choser,user_EXP,user_winstreak)
    return 0
def result(win,chess_choser):#游戏结算
    if(win[0] != 2):
        if(chess_choser != 0):
            if(win[0] == chess_choser):
                print("胜利")
                exp += 1
                winstreak += 1
            else:
                print("失败")
                winstreak = 0
        else:print("你尚未登录，登录后可以记录战绩。")
    else:print("本局未正常结束，不记录。")
print("iChess Launcher\n输入help以获得帮助。")
while(quit != 0):  #循环，直到输入“quit”
    quit = 1
    typing = input("请输入命令。") #输入部分
    if(typing == "help"): #输入实现
        print("以下为可输入命令。")
        print("help - 罗列可使用命令。\nver - 查看iCL版本信息。\nnews - 查看iCL资讯。\nquit - 退出iCL(需先退出登录才可关闭iCL)。\nacc-in - 登录iCL账户。\nacc-out - 退出iCL账户。\nacc-new - 注册新的iCL账户。\nacc - 查看当前登录账户档案。\nstart-game - 开始游戏！")
    elif(typing == "ver"):print("iChess Launcher(iCL)v1.0.0")
    elif(typing == "news"):print("更新主题:星辰起航\n更新内容\n普通模式：最基础的iChess模式，原汁原味的五子棋。")
    elif(typing == "quit"):
        if(acc_select == 0):
            quit = 0
        else:print("请先退出登录后再退出iCL。")
    elif(typing == "acc-new"):
        print("请输入账户名。")
        user_name = input("")#输入用户名
        if(user_name == ""):
            print("不能输入空字符，已自动退出注册。")
        else:
            print("请输入账户密码。")
            user_password = input("")
            print("给自己写段介绍吧。")
            user_describe = input("")
            fp = open(f"{user_name}.txt",'w',encoding="UTF-8")#基本信息写入文档
            fp.write(user_name+"\nname:\n")
            fp.write(user_password+"\npassword:\n")
            if(user_describe != ""):#介绍判断，没写介绍则写入默认内容
                fp.write(user_describe)
            else:fp.write("这个人很施朗，什么也没写")
            fp.write("\ndescribe:")
            fp.write("\n0\nEXP:")
            fp.write("\n0\nwin_streak:")
            fp.write("\n新人\ndesignation:")
            fp.flush()
            fp.close
            print("注册成功！")
    elif(typing == "acc-in"):
        data_name = input("请输入账户名。")
        try:#防止输入不存在账户
            fp = open(f"{data_name}.txt","r",encoding="UTF-8")
        except FileNotFoundError:
            print("未找到此存档，已退出登录。")
        else:
            contents = linecache.getline(f"{data_name}.txt",3)
            user_password = input("请输入密码。")
            if(user_password+"\n" == contents):
                user_namel = linecache.getline(f"{data_name}.txt",1)#基本信息覆盖
                user_passwordl = linecache.getline(f"{data_name}.txt",3)
                user_describel = linecache.getline(f"{data_name}.txt",5)
                user_EXP = linecache.getline(f"{data_name}.txt",7)
                user_winstreak = linecache.getline(f"{data_name}.txt",9)
                user_designation = linecache.getline(f"{data_name}.txt",11)
                print("登录成功！")
                acc_select = data_name
            else:print("密码错误，已自动退出登录。")
    elif(typing == "acc-out"):
        fp = open(f"{acc_select}.txt",'w',encoding="UTF-8")#基本信息写入文档
        fp.write(user_namel+"name:")
        fp.write("\n"+user_passwordl+"password:")
        if(user_describel != ""):#介绍判断，没写介绍则写入默认内容
            fp.write("\n"+user_describel)
        else:fp.write("这个人很施朗，什么也没写")
        fp.write("describe:")
        fp.write("\n"+user_EXP+"EXP:")
        fp.write("\n"+user_winstreak+"win_streak:")
        fp.write("\n"+user_designation+"designation:")
        fp.flush()
        fp.close
        acc_select = 0
        print("成功退出登录！")
    elif(typing == "acc"):
        if(acc_select != 0):
            fp = open(f"{acc_select}.txt","r",encoding="UTF-8")
            print("\n"+linecache.getline(f"{acc_select}.txt",1))
            print(linecache.getline(f"{acc_select}.txt",5))
            print("经验:"+linecache.getline(f"{acc_select}.txt",7))
            print("连胜局数:"+linecache.getline(f"{acc_select}.txt",9))
            print("称号:"+linecache.getline(f"{acc_select}.txt",11))
        else:
            print("当前未登录，请在登录后重试。")
    elif(typing == "start-game"):
        chess_sx = int(input("请输入棋盘长度。(输入5~150整数)"))
        if(chess_sx >= 5 and chess_sx <= 150):
                chess_sy = int(input("请输入棋盘宽度。(输入5~150整数)"))
                if(chess_sy >= 5 and chess_sy <= 150):
                    if(acc_select != 0):
                        chess_choser = input("请输入你的阵营。(X或O)")
                        if(chess_choser == "O" or chess_choser == "X"):
                            if(chess_choser == "O"):
                                chess_choser = 0
                            else:chess_choser = 1
                        else:
                            chess_choser = 0
                            print("输入错误，已默认为O。")
                    else:chess_choser = 0
                    normal_chess(chess_sx,chess_sy)
                else:print("输入错误，已退出游戏。")
        else:print("输入错误，已退出游戏。") 
print("感谢你的使用，下次启动再见。")