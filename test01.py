# hello = '刘总你好啊'
# print(hello[:2])
#
# length = len(hello)
# print(length)

# print(3 ** 2)
# print(type(3))

# def interview(interviewee):
#     print("把求职者"+ interviewee +"带到3号会议室")
#     print("请求职者 完成答卷")
#     print("让测试经理来面试 求职者")
#     print("让技术总监面试 求职者")
#
# interview("聂德鑫")
#
# def squareNums(nums1, nums2):
#     return nums1 ** 2 + nums2 ** 2
#
# nums = squareNums(1,2)
# print(nums)

# upChars = '零壹贰叁肆伍陆柒捌玖'
# def getZh(num):
#     print('对应的汉字是：' + upChars[num])
#
# getZh(5)

# salary = input('Enter your salary: ')
# print(salary)

#salary = input('请输入张三薪资:')
# intSalary = int(salary)
# print(intSalary)
#print('税后的薪资为：' + str(int(salary)*75/100))

# var = 100
# a = [1, 2, var * 3 + 20, 'hello', [7, 8, '你好']]
# print(a)

# a = [1, 2, 3]
# a += [4, 5, 6]
# print(a)

# list1 = [1, 2, 3, 4, 'hello']
# tuple1 = (1, 2, 3, 4, 'hello')
# if 'hello' in list1:
#     print("hello在列表中")
# if 'boy' not in tuple1:
#     print('boy在元组中不存在')
#

# def func1():
#     age = input('请输入年龄：')
#     gender = input('请输入性别：')
#     return [age, gender]
#
# print(func1())

# def registerUser():
#     phone = input('请输入你的手机号码（不超过11个字符）:')
#     if len(phone) > 11:
#         print('输入错误！手机号码过长')
#     elif not phone.startswith('1'):
#         print('输入错误，手机号码需要以数字1开头')
#
# registerUser()

#判断天气怎么样
# def junctionWeather(wether, pa):
#     if(wether < -8 or wether > 30):
#         print('不舒适')
#         return
#
#     if(pa < 20 or pa>300):
#         print('不舒适')
#         return
#
#     if(25 < wether <= 30):
#         if(200 < pa <= 300):
#             print('比较舒适')
#         elif(100 < pa <= 200):
#             print('特别舒适')
#         elif(20 < pa <= 100):
#             print('比较舒适')
#         else:
#             print('本程序不能判断')
#
# weather = int(input("请输入今天的气温（摄氏度）："))
# pa = int(input('请输入今天的气压（帕）：'))
# junctionWeather(weather, pa)

# print('税前薪资：%-10s 元' % 100000)
# print('税前薪资：%-10s 元' % 10000)
# print('税前薪资：%-10s 元' % 1000)

# #员工1
# salary = 8000
# tax = int(salary) * 0.25
# aftertax = int(salary) * 0.75
# print(f'税前薪资是: {salary:8}元，缴税:{tax:8}元，税后薪资是:{aftertax:8}')
#
# # 员工 2
# salary = 15000
# tax = int(salary) *25/100
# aftertax = int(salary) *75/100
# print(f'税前薪资是：{salary:8}元， 缴税：{tax:8}元， 税后薪资是：{aftertax:8}元')
#
#
# # 员工 3
# salary = 100000
# tax = int(salary) *25/100
# aftertax = int(salary) *75/100
# print(f'税前薪资是：{salary:8}元， 缴税：{tax:8}元， 税后薪资是：{aftertax:8}元')

# def CalTax(salary):
#     tax = salary * 0.25
#     afterTax = salary * 0.75
#     print(f'税前薪资是：{salary:08}元， 缴税：{tax:8}元， 税后薪资是：{afterTax:8}元')
#
# CalTax(8000)
# CalTax(10000)
# CalTax(15000)

# times1 = 1000
# times2 = 2000
#
# print(f'文章中 {{ 符号 出现了 {times1} 次')
# print(f'文章中 }} 符号 出现了 {times2} 次')

# for n in range(1,11):
#     print(n)
#     print('我爱你')

# studentAges = ['小王:17', '小赵:16', '小李:17', '小孙:16', '小徐:18']
#
# # enumerate (studentAges) 每次迭代返回 一个元组
# # 里面有两个元素，依次是 元素的索引和元素本身
# for idx, student in enumerate(studentAges):
#     if int(student.split(':')[-1]) > 17:
#         print(idx)

# list1 = ['关羽','张飞','赵云','马超','黄忠']
# list2 = ['典韦','许褚','张辽','夏侯惇','夏侯渊']
#
# for member1 in list1:
#     for member2 in list2:
#         print(f'{member1} 大战 {member2}')

# print(b'\xe4\xbd\xa0\xe5\xa5\xbd'.decode('utf8'))
# print(b'\xc4\xe3\xba\xc3'.decode('utf8'))

# print(ord('欣'))

# f = open('tmp.txt', 'a', encoding='utf-8')
# f.write('千万不要放弃呀，加油！')
# f.close()

# f = open('tmp.txt','r', encoding='utf-8')
# content = f.read()
# print(content)