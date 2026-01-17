rent = 3000
''''def cost():
    global variable_cost
    # 将在cost()函数中定义的variable_cost变量定义为全局变量
    utilities = int(input('请输入本月的水电费用'))
    food_cost = int(input('请输入本月的食材费用'))
    variable_cost = utilities + food_cost
    print('本月的变动成本是' + str(variable_cost))'''


def sum_cost():
    sum = rent + variable_cost
    # 在cost()函数中定义的variable_cost变量可以在sum_cost()函数中使用
    print('本月的总成本是' + str(sum))


cost()
sum_cost()

'