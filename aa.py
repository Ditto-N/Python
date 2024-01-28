# 聚餐计算人均费用

fee = input("请输入晚餐费用：")
members = input('请输入聚餐人姓名，以英文逗号,分隔：')

# 将人员放入一个列表
members = members.split(',')
# 得到人数
headcount = len(members)

# 计算人均费用
avgfee = float(fee) / headcount
print(f'人均费用为{avgfee}')