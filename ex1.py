name="大肥鱼"
age=22
city="杭州"
print(f"我叫{name},今年{age},来自{city}")
price="12000"
count="3"
print(price+count)
all_1=int(price)*int(count)
print(f"总价：{all_1}")
scores=[88,92,75,60,95]
total=0
for i in range(5):
    total=total+scores[i]
p=total/len(scores)
print(f"总分{total},平均分{p}")
