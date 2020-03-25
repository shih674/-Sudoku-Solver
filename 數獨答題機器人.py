#!/usr/bin/env python
# coding: utf-8

# In[96]:


# 運算指標
pointer_x = 0
pointer_y = 0

# 數獨題目
# 題目打在這裡，9*9的List
question_ori = [[0, 0, 9, 0, 0, 0, 5, 0, 0], 
                [0, 0, 0, 0, 3, 0, 0, 9, 4], 
                [3, 1, 6, 0, 4, 0, 0, 0, 0], 
                [0, 0, 0, 0, 0, 0, 0, 0, 0], 
                [0, 0, 7, 0, 9, 0, 2, 8, 0], 
                [6, 0, 1, 0, 8, 4, 7, 0, 0], 
                [0, 7, 0, 0, 0, 5, 0, 0, 6], 
                [0, 2, 0, 7, 0, 0, 0, 0, 0], 
                [1, 0, 5, 0, 0, 0, 0, 0, 0]]


# In[97]:


# 快速輸入題目
count = 1
table = [] # 放置使用者輸入題目的表格

while count <= 9:
    while True:
        raw_input = input(f':: 請輸入第 {count} 列 \n >>')
        
        # 檢查長度是否為9，不是則重新輸入
        if len(raw_input) == 9:
            break
        else:
            print(f' [Warning] 輸入的長度有問題，請重新輸入')
    row = []
    
    # 把輸入的字串轉化成長度為9的字串
    for i in range(0,9):
        try:
            row.append(int(raw_input[i]))
        except:
            print(f' [Exception] 字元轉換錯誤，只能輸入數字')
    # 把list加回表中
    table.append(row)
    count = count + 1

# 印出使用者輸入檢查內容
print_table(table)
question_ori = table


# In[98]:


# 小工具: 印出表格狀題目
def print_table(table):
    print('')
    for i in range(9):
        tmp_content = ''
        for j in range(9):
            tmp_content = tmp_content + ' ' + str(table[i][j]) + ' '
            if j == 2:
                tmp_content = tmp_content + ' * '
            if j == 5:
                tmp_content = tmp_content + ' * '
        print(tmp_content)
        if i == 2:
            print(' * * * * * * * * * * * * * * * *')
        if i == 5:
            print(' * * * * * * * * * * * * * * * *')
    print('')

# 解答
def row_analy(i,question):
    numbers = []
    counter = 0
    for j in range(9):
        #print(f'第{j+1}次執行 >> {question[i][j]}')
        if question[i][j] != 0:
            numbers.append(question[i][j])
        counter = counter + 1
    return numbers
def column_analy(j,question):
    numbers = []
    for i in range(9):
        if question[i][j] != 0:
            numbers.append(question[i][j])
    return numbers
def block_analy(i,j,question):
    standard_i = int(i/3)
    standard_j = int(j/3)
    #print(i,j)
    #print('===========')
    numbers = []
    for i1 in range(3):
        for j1 in range(3):
            #print((standard_i*3+i1),(standard_j*3+j1))
            if question[(standard_i*3+i1)][(standard_j*3+j1)] != 0:
                numbers.append(question[(standard_i*3+i1)][(standard_j*3+j1)])
    return numbers

# 綜合分析
def total_analy(row_result,column_result,block_result):
    answer_sheet = { 1:True, 2:True, 3:True, 4:True, 5:True, 6:True, 7:True, 8:True, 9:True}
    for ele in row_result:
        answer_sheet[ele] = False
    for ele in column_result:
        answer_sheet[ele] = False
    for ele in block_result:
        answer_sheet[ele] = False

    possible_answer = []
    #
    for i in range(1,10):
        if answer_sheet[i] == True:
            possible_answer.append(i)
    if len(possible_answer) == 1:
        return True,possible_answer[0]
    else:
        return False,0


# In[99]:


# 方法2
def scheme2(target,question):
    location = []
    # 保存行列中是否有可能為target的表，True有，False沒有
    big_table = [[True, True, True, True, True, True, True, True, True], 
                 [True, True, True, True, True, True, True, True, True], 
                 [True, True, True, True, True, True, True, True, True], 
                 [True, True, True, True, True, True, True, True, True], 
                 [True, True, True, True, True, True, True, True, True], 
                 [True, True, True, True, True, True, True, True, True], 
                 [True, True, True, True, True, True, True, True, True], 
                 [True, True, True, True, True, True, True, True, True], 
                 [True, True, True, True, True, True, True, True, True]]
    
    for i in range(0,9): # 從question的第一列做到第九列
        for j in range(0,9): # 從question的第一行做到第九行
            # 如果題目格裡的數字不是零，即非空格
            if question[i][j] != 0:
                big_table[i][j] = False
                
            # 如果題目格裡的數字跟目標(target)相同
            if question[i][j] == target:
                location.append((i,j))
                # row全部沒可能
                big_table[i] = [False, False, False, False, False, False, False, False, False]
                # column全部沒可能
                for temp in range(0,9):
                    big_table[temp][j] = False
                # 同block全部沒可能
                basic_x = int(i/3)
                basic_y = int(j/3)
                big_table[basic_x*3][(basic_y*3)] = False
                big_table[basic_x*3][(basic_y*3+1)] = False
                big_table[basic_x*3][(basic_y*3+2)] = False
                big_table[basic_x*3+1][(basic_y*3)] = False
                big_table[basic_x*3+1][(basic_y*3+1)] = False
                big_table[basic_x*3+1][(basic_y*3+2)] = False
                big_table[basic_x*3+2][(basic_y*3)] = False
                big_table[basic_x*3+2][(basic_y*3+1)] = False
                big_table[basic_x*3+2][(basic_y*3+2)] = False
    
    #print_table(big_table)
    
    return_list = []
    # 篩選整row只有一個True
    for i in range(0,9):
        temp1 = []
        for j in range(0,9):
            if big_table[i][j] == True:
                temp1.append((i,j))
        if len(temp1) == 1:
            return_list.append(temp1[0])
    
    # 篩選整column只有一個True
    for j in range(0,9):
        temp1 = []
        for i in range(0,9):
            if big_table[i][j] == True:
                temp1.append((i,j))
        if len(temp1) == 1:
            return_list.append(temp1[0])                
    
    # 篩選整BLOCK只有一個True
    for basicX in range(0,3):
        for basicY in range(0,3):
            temp1 = []
            # 上左
            if big_table[basicX*3][basicY*3] == True:
                temp1.append((basicX*3,basicY*3))
            # 上中
            if big_table[basicX*3][basicY*3+1] == True:
                temp1.append((basicX*3,basicY*3+1))
            # 上右
            if big_table[basicX*3][basicY*3+2] == True:
                temp1.append((basicX*3,basicY*3+2))
            # 中左
            if big_table[basicX*3+1][basicY*3] == True:
                temp1.append((basicX*3+1,basicY*3))
            # 正中
            if big_table[basicX*3+1][basicY*3+1] == True:
                temp1.append((basicX*3+1,basicY*3+1))
            # 中右
            if big_table[basicX*3+1][basicY*3+2] == True:
                temp1.append((basicX*3+1,basicY*3+2))
            # 下左
            if big_table[basicX*3+2][basicY*3] == True:
                temp1.append((basicX*3+2,basicY*3))
            # 下中
            if big_table[basicX*3+2][basicY*3+1] == True:
                temp1.append((basicX*3+2,basicY*3+1))
            # 下右
            if big_table[basicX*3+2][basicY*3+2] == True:
                temp1.append((basicX*3+2,basicY*3+2))
            if len(temp1) == 1:
                return_list.append(temp1[0])
                
    return return_list


# In[100]:


# 主程式段

running = True
while running:
    # 流程控制元件
    counter = 0
    
    # scheme1
    pointer_x = 0
    while pointer_x <= 8:
        pointer_y = 0
        while pointer_y <= 8:
            if question_ori[pointer_x][pointer_y] == 0:
                result1 = row_analy(pointer_x,question_ori)
                result2 = column_analy(pointer_y,question_ori)
                result3 = block_analy(pointer_x,pointer_y,question_ori)
                #print('==========================')
                #print(f'result1>> {result1}')
                #print(f'result2>> {result2}')
                #print(f'result3>> {result3}')
                
                feedback = total_analy(result1,result2,result3)
                if feedback[0] == True:
                    question_ori[pointer_x][pointer_y] = feedback[1]
                    print(f':: 在({pointer_x},{pointer_y})，計算出結果{feedback[1]}')
                    counter = counter + 1
            pointer_y = pointer_y +1
        pointer_x = pointer_x +1

    print_table(question_ori)
    
    # scheme2
    for this_turn in range(1,9):
        result = scheme2(this_turn,question_ori)
        if len(result) == 0:
            pass
        else:
            for ele in result:
                question_ori[ele[0]][ele[1]] = this_turn
            counter = counter +1
            print(f':: 計算出 {this_turn} 出現在 {result}')
            
    print_table(question_ori)
    
    # 流程控制開關
    if counter == 0:
        running = False

print("::計算結束，結果為")
print_table((question_ori))

