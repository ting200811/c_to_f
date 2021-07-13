# c_to_f
temp = input('請輸入溫度(攝氏), 將為您轉換成溫度(華氏)')
temp = float(temp) # 轉換成float, 因為可以有小數點
# c_to_f result
print('華氏溫度為:', temp * 9 / 5 + 32)