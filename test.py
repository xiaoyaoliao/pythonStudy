# 第七章while循环
# 使用用户输入来补全字典
# responses={}
# polling_active=True
# while polling_active:
#     #enter the key
#     name=input("enter the user name:")
#     #enter the value
#     response=input("enter the response:")
#     #给键值对赋值
#     responses[name]=response
#     repeat=input("continue?")
#     if repeat=='no':
#         polling_active=False
# print(responses)

# sandwich_order problem
# sandwich_order=['love','cute','coco']
# finished_sandwich=[]
# while sandwich_order:
#     current_sandwish=sandwich_order.pop()
#     print("the current sandwish:"+current_sandwish)
#     finished_sandwich.append(current_sandwish)
# print(finished_sandwich)

#调查结果调用
# observes={}
#是否继续进行调查
# polling_active=True
# while polling_active:
#     id=input("enter the id:")
#     info=input("enter the information:")
#     observes[id]=info
#     flag=input("continue?")
#     if flag=='no':
#         polling_active=False
# print(observes)

# 第八章函数
# def formated_name(firstname,lastname,midname=''):
#     person={'first':firstname,'last':lastname}
#     if midname:
#         person['mid']=midname
#     return person
# tempPerson=formated_name('Alice','Green','cc')
# print(tempPerson)

# 对列表的操作
# def printModel(unprinted_designs,completed_models):
#     #将未完成的任务一个一个的取出来并且打印出来，添加到complted_models
#     while unprinted_designs:
#         current=unprinted_designs.pop()
#         print(current)
#         completed_models.append(current)
#
# unprints=['cc','aa','bb']
# complete=[]
# printModel(unprints,complete)
# print(unprints)
# print(complete)

# 使用任意数量的关键字实参
# def build_profile(first,last,**user_info):
#     person={}
#     person['first']=first
#     person['last']=last
#     for k,v in user_info.items():
#         person[k]=v
#     return person
# temp=build_profile('Alice','Green',location='id',filed='5')
# print(temp)

# test 8-14
# def car_design(name,num,**car_info):
#     car={}
#     car['name']=name
#     car['num']=num
#     for k,v in car_info.items():
#         car[k]=v
#     return car
# temp_car=car_design('Toyota','1002',color='red',peijian='gear')
# print(temp_car)

# 第九章：类
# class Dog:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#
#     def sit(self):
#         print("My name is "+self.name+", I'm sitting!")
#
#     def roll_over(self):
#         print("My name is "+self.name+", I'm rolling!")
# my_dog=Dog('whille',6)
# print("My name is "+my_dog.name+", and my age is "+str(my_dog.age))
# my_dog.sit()
# my_dog.roll_over()

# 9-1餐馆
# class Restaurant():
#     def __init__(self,restaurant_name,cuisine_type):
#         self.name=restaurant_name
#         self.type=cuisine_type
#         self.number_served=0
#
#     def describe_restaurant(self):
#         print("The  name:"+self.name)
#         print("The  type:"+self.type)
#
#     def open_restaurant(self):
#         print("The restaurant open now!")
#
#     def set_number_served(self,num):
#         self.number_served=num

# rest_one=Restaurant('DW','China food')
# rest_two=Restaurant('Crazy','America food')
# rest_three=Restaurant('KFC','juke food')
# rest_one.set_number_served(30)
# print(rest_one.number_served)
# rest_one.number_served=10
# print(rest_one.number_served)

# 新建ice cream类继承restaurant类
# class IceCreamStand(Restaurant):
#     cailiao=[]
#     def __init__(self,restaurant_name,cuisine_type,*toppings):
#         super().__init__(restaurant_name,cuisine_type)
#         for topping in toppings:
#             self.cailiao.append(topping)
#
#     def describe(self):
#         print("the ice cream store:"+self.name)
#         print("the ice cream type:"+self.type)
#         for cai in self.cailiao:
#             print(cai+" ")

# my_icecream=IceCreamStand('IceIsland','tianping','banana','apple')
# my_icecream.describe()

# class User:
#     def __init__(self,first_name,last_name):
#         self.first=first_name
#         self.last=last_name
#         self.login_attempts=0
#
#     def desscribe_user(self):
#         print("the first name:"+self.first)
#         print("the last name:"+self.last)
#
#     def greet_user(self):
#         full_name=self.first+" "+self.last
#         print("Hello! "+full_name)
#
#     def increment_login_attempts(self):
#         self.login_attempts=self.login_attempts+1
#
#     def reset_login_attempts(self):
#         self.login_attempts=0
#
# class Privileges():
#     privileges=[]
#     def __init__(self,*toppings):
#         for topping in toppings:
#             self.privileges.append(topping)
#
#     def show_privileges(self):
#         for priv in self.privileges:
#             print(priv)
#
# class Admin(User):
#     privileges=[]
#     def __init__(self,first_name,last_name,*toppings):
#         super().__init__(first_name,last_name)
#         self.privileges=Privileges(toppings)
#
# my_admin=Admin('Alice','Green','can add post','can delete post')
# my_admin.privileges.show_privileges()

# my_user=User('Alice','Green')
# my_user.increment_login_attempts()
# my_user.increment_login_attempts()
# my_user.increment_login_attempts()
#my_user.reset_login_attempts()
# print(my_user.login_attempts)
# 第十章文件
# filename='test.txt'
# with open(filename) as file_object:
#     for line in file_object:
#         print(line.rstrip())

# filename='test.txt'
# with open(filename) as obj:
#     lines=obj.readlines()
#
# for line in lines:
#     print(line.rstrip())

# filename='test.txt'
# 得到文件中的所有行的内容
# with open(filename) as file_object:
#     lines=file_object.readlines()
# string_test=' '
# for line in lines:
#     string_test+=line.strip()
# print(string_test)
# print(len(string_test))

# 查看圆周率里面有没有自己的生日
# filename='test.txt'
# with open(filename) as file_object:
#     lines=file_object.readlines()
# # 去掉每一行的换行符
# string_pi=' '
# for line in lines:
#     string_pi+=line.strip()
#
# birthday=input("enter your birthday:")
# if birthday in string_pi:
#     print("your birthday in pi!")
# else:
#     print("NO!")

# 10-1 and 10-2
# 不同的方式打印文件
# filename='youcan.txt'
# with open(filename) as file_obj:
#     lines=file_obj.readlines()
#
# for line in lines:
#     if 'Python' in line:
#         print(line.replace('Python','C'))

# 10-3
# filename='user.txt'
# user_choose=True
# with open(filename,'a') as file_obj:
#     while user_choose:
#         choose=input("Do you like computer?")
#         if choose=='y':
#             result=input("the result:")
#             file_obj.write(result+"\n")
#         else:
#             user_choose=False
#         flag=input("continue?")
#         if flag=='y':
#             user_choose=True
#         else:
#             user_choose=False

# def countnum(filename):
#     try:
#         with open(filename) as file_obj:
#             count=file_obj.read()
#     except FileNotFoundError:
#         print("Not found "+str(filename)+"\n")
#     else:
#         word=count.split()
#         num=len(word)
#         print(str(filename)+" words number is "+str(num))
#
# filenames=['test.txt','apple.txt','youcan.txt']
# for filename in filenames:
#     countnum(filename)

# 10-6
# try:
#     first=input("enter the first number:")
#     first=int(first)
#
#     second=input("enter the second number:")
#     second=int(second)
# except ValueError:
#     print("Please enter the number!")
# else:
#     sum=first+second
#     print(str(sum))

# while True:
#     try:
#         first = input("enter the first number:")
#         first = int(first)
#
#         second = input("enter the second number:")
#         second = int(second)
#     except ValueError:
#         print("Please enter the number!")
#     else:
#         sum = first + second
#         print(str(sum))

# 利用json存储数据
import json
# filename='number.json'
# numbers=[2,3,2,4,5]
# with open(filename,'w') as file_obj:
#     json.dump(numbers,file_obj)
# 读取Json数据
# with open(filename) as file_obj:
#     numbers=json.load(file_obj)
# print(numbers)
# import json
# filename='username.json'
# try:
#     with open(filename) as file_obj:
#         username=json.load(file_obj)
# except FileNotFoundError:
#     username=input("enter the username:")
#     with open(filename,'w') as file_obj:
#         json.dump(username,file_obj)
# else:
#     print("Welcome to back "+username)

# import json
# filename='favorite_num.json'
# try:
#     with open(filename) as file_obj:
#         favoritenum=json.load(file_obj)
# except FileNotFoundError:
#     favoritenum=input("enter a number you like:")
#     with open(filename,'w') as file_obj:
#         json.dump(favoritenum,file_obj)
# else:
#     print("I know your favorite number is "+str(favoritenum))
# import unittest
# from restaurant import get_name
#
# class NameTestCase(unittest.TestCase):
#     def test_first_last_name(self):
#         full_name=get_name('janis','kim')
#         self.assertEqual(full_name,'Janis Kim')
#
#     def test_first_last_mid_name(self):
#         full_name=get_name('alice','happy','sum')
#         self.assertEqual(full_name,'Alice Sum Happy')
#
# unittest.main()
#
# import unittest
# from restaurant import get_city
#
# class CityTestCase(unittest.TestCase):
#     def city_country_test(self):
#         full_city=get_city('santiago','chile')
#         self.assertEqual(full_city,'tion=500')
#
# unittest.main()

# 创建一个类收集秘密调查问卷
# class AnonymousSurvey():
# # 1.存储一个问题，并为存储答案做准备
#     def __init__(self,question):
#         self.qustion=question
#         self.answer=[];
# # 2.显示调查问卷
#     def show_question(self):
#         print(self.qustion)
# # 3.存储单份调查问卷
#     def store_question(self,response):
#         self.answer.append(response)
# # 4.显示收集到的所有问卷
#     def show_all(self):
#         for ans in self.answer:
#             print(ans)
# my_question=AnonymousSurvey('Do you like bread')
# choose=True
# while choose:
#     answer=input("Do you like bread")
#     my_question.store_question(answer)
#     flag=input("continue?")
#     if flag=='y':
#         choose=True
#     else:
#         choose=False
# my_question.show_question()
# my_question.show_all()

# import unittest
# from restaurant import AnonymousSurvey
# class TestAnonymousSurvey(unittest.TestCase):
#     def test_store_answer(self):
#         question="What language did you first learn to speak?"
#         answers=['English','Spanish','Mandarin']
#         my_survey=AnonymousSurvey(question)
#         for answer in answers:
#             my_survey.store_question(answer)
#         for answer in answers:
#             self.assertIn(answer,my_survey.answer)
# unittest.main()

# import unittest
# from restaurant import AnonymousSurvey
# class SurveyTestCase(unittest.TestCase):
#     def setUp(self):
#         question="Do you like bread!"
#         self.answers=['Yes','Yes','Yes']
#         self.my_survey=AnonymousSurvey(question)
#     def test_store_single(self):
#         self.my_survey.store_question(self.answers[0])
#         self.assertIn(self.answers[0],self.my_survey.answer)
#
#     def test_store_three(self):
#         for answer in self.answers:
#             self.my_survey.store_question(answer)
#         for answer in self.answers:
#             self.assertIn(answer,self.my_survey.answer)
# unittest.main()

# 第十五章数据可视化
# import matplotlib.pyplot as plt
# input_num=[1,2,3,4,5]
# output_num=[1,4,9,16,25]
# plt.plot(input_num,output_num,linewidth=5)
# plt.title("Square",fontsize=24)
# plt.xlabel("x",fontsize=14)
# plt.ylabel("y",fontsize=14)
# plt.tick_params(axis='both',labelsize=14)
# plt.show()

# import matplotlib.pyplot as plt
# input_num=[1,2,3,4,5]
# output_num=[1,4,9,16,25]
# plt.scatter(input_num,output_num,s=40)
# plt.title("test",fontsize=24)
# plt.xlabel("x",fontsize=14)
# plt.ylabel("y",fontsize=14)
# plt.tick_params(axis='both',which='major',labelsize=14)
# plt.show()

# 自动计算
import matplotlib.pyplot as plt
# input_num=list(range(1,1001))
# output_num=[x**2 for x in input_num]
# plt.scatter(input_num,output_num,c=output_num,cmap=plt.cm.Blues,edgecolors='none',s=40)
# plt.title("test",fontsize=24)
# plt.xlabel("x",fontsize=14)
# plt.ylabel("y",fontsize=14)
# plt.tick_params([0, 1100,0,1100000])
# plt.savefig('test.png',bbox_inches='tight')

# x=[1,2,3,4,5]
# y=[1,4,9,16,25]
# plt.scatter(x,y,s=40)
# plt.show()

# x_lable=list(range(1,5001))
# y_lable=[x**3 for x in x_lable]
# plt.scatter(x_lable,y_lable,c=y_lable,cmap=plt.cm.Blues,s=40)
# plt.show()

# 随机漫步
# import matplotlib.pyplot as plt
# from random import choice
# class RamndomWalk():
#     def __init__(self,num_point=5000):
#         self.num_point=num_point
#         self.x_value=[0]
#         self.y_value=[0]
#
#     def fill_walk(self):
#         while len(self.x_value)<self.num_point:
#             x_direction=choice([1,-1])
#             x_distance=choice([0,1,2,3,4])
#             x_step=x_direction*x_distance
#
#             y_direction = choice([1, -1])
#             y_distance = choice([0, 1, 2, 3, 4])
#             y_step = y_direction * y_distance
#
#             x_next=self.x_value[-1]+x_step
#             y_next=self.y_value[-1]+y_step
#
#             self.x_value.append(x_next)
#             self.y_value.append(y_next)
#
# rw=RamndomWalk(50000)
# rw.fill_walk()
# plt.plot(rw.x_value,rw.y_value,linewidth=1)
# plt.show()
# plt.figure(dpi=128,figsize=(10,6))
# point_num=list(range(rw.num_point))
# plt.scatter(rw.x_value,rw.y_value,c=point_num,cmap=plt.cm.Blues,s=15)
# plt.scatter(0,0,c='green',s=100)
# plt.scatter(rw.x_value[-1],rw.y_value[-1],c='red',s=100)
# plt.show()
import csv
from datetime import datetime as dat
# filename='sitka_weather_07-2014.csv'
# with open(filename) as f:
#     reader=csv.reader(f)
#     header_row=next(reader)
    # print(header_row)
    # 获取索引极其值
    # for index,column_header in enumerate(header_row):
    #     print(index,column_header)
    # 获取最高温度
    # high=[]
    # dates=[]
    # for row in reader:
    #     current_day=dat.strptime(row[0],"%Y-%m-%d")
    #     dates.append(current_day)
    #     high.append(int(row[1]))
# plt.figure(dpi=128,figsize=(10,6))
# plt.plot(dates,high,c='red')
# plt.title('temper',fontsize=14)
# plt.xlabel('date',fontsize=3)
# plt.ylabel('temper',fontsize=14)
# plt.tick_params(axis='both',which='major',labelsize=16)
# plt.show()

# filename='death_valley_2014.csv'
# with open(filename) as f:
#     reader=csv.reader(f)
#     head_column=next(reader)
#     highs=[]
#     dates=[]
#     lows=[]
#     for row in reader:
#         try:
#             current_day = dat.strptime(row[0], "%Y-%m-%d")
#             high=int(row[1])
#             low=int(row[3])
#         except ValueError:
#             print(current_day,"miss data")
#         else:
#             dates.append(current_day)
#             highs.append(high)
#             lows.append(low)
#
# plt.figure(dpi=128,figsize=(10,6))
# plt.plot(dates,highs,c='red',alpha=0.5)
# plt.plot(dates,lows,c='blue',alpha=0.5)
# plt.fill_between(dates,highs,lows,facecolor='blue',alpha=0.1)
# plt.title('temper',fontsize=14)
# plt.xlabel('date',fontsize=3)
# plt.ylabel('temper',fontsize=14)
# plt.tick_params(axis='both',which='major',labelsize=16)
# plt.show()

# 16.2炒股图片展示
# import json
# import pygal
# filename='btc_close_2017.json'
# with open(filename) as f:
#     dates=[]
#     months=[]
#     weeks=[]
#     weekdays=[]
#     closes=[]
#     btc_datas=json.load(f)
#     for btc_data in btc_datas:
#         dates.append(btc_data['date'])
#         months.append(int(btc_data['month']))
#         weeks.append(int(btc_data['week']))
#         weekdays.append(btc_data['weekday'])
#         closes.append(int(float(btc_data['close'])))
# line_chart=pygal.Line(x_label_rotation=20,show_minor_x_labels=False)
# line_chart.title='收盘价（$）'
# line_chart.x_labels=dates
# N=20
# line_chart.x_labels_major=dates[::N]
# line_chart.add('收盘价',clo`ses)
# line_chart.render_to_file('收盘价折线图.svg')

import pygal
from random import randint
class Die:
    def __init__(self,num_sides=6):
        self.numsides=num_sides

    def roll(self):
        return randint(1,self.numsides)

die=Die()
results=[]
for roll_num in range(100):
    result=die.roll()
    results.append(result)
# 分析结果
# 分析结果
frequencies=[]
for value in range(1,die.numsides+1):
    frequency=results.count(value)
    frequencies.append(frequency)
print(frequencies)
hist=pygal.Bar()
hist.title='Result of rolling one D6 1000 times.'
hist.x_labels=['1','2','3','4','5','6']
hist.x_title="Result"
hist.y_title="Frequency of Result"

hist.add('D6',frequencies)
hist.render_to_file('die_visual.svg')

