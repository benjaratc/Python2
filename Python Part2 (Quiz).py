#!/usr/bin/env python
# coding: utf-8

# 1.เขียนโปรแกรมรับ input จากผู้ใช้ 1 ตัว แปลงให้เป็น int และตรวจสอบว่าเป็นเลขคู่หรือเลขคี่ 
# 
# 	- หากเป็นเลขคู่ ให้พิมพ์ว่า เลขคู่
# 
# 	- หากเป็นเลขคี่ ให้พิมพ์ว่า เลขคี่
# 
# 	- หากเป็นเลขศูนย์ให้พิมพ์ว่า เลขศูนย์

# In[6]:


number = int(input("enter a number: ",))
if number == 0:
    print("the number is 0")
elif number % 2 != 0:
    print("the number is odd")
elif number % 2 == 0:
    print("the number is even")


# 2.เขียนโปรแกรมรับค่า input 2 ตัว ในรูปแบบ float โดยให้ตัวแรกเป็นตัวตั้ง ตัวที่สองเป็นตัวหาร
# 
# 	- หาผลลัพธ์ของการหาร
# 
# 	- ใส่เลขทศนิยมได้
# 
# 	- ถ้าตัวหารเป็น 0 ให้รับค่าใหม่จนกว่าจะเป็นเลขที่หารได้  

# In[3]:


number1 =float(input("enter a number1: ",))
number2 =float(input("enter a number2: ",))

while number2 == 0:
    number2 = float(input("put a number2: ",))

result = float(number1 / number2)
print(result)


# 3.เขียนโปรแกรม infinity while loop โดยรับค่า input มาเรื่อยๆ จนกว่าผู้ใช้จะใส่เลข 0 และนำเลขทั้งหมดมาหาค่าเฉลี่ย

# In[10]:


total_sum = 0
for n in range(num):
    numbers = float(input('enter a number: '))
    total_sum += numbers
    if numbers != 0:
        numbers = int(input("enter a number: ",))
        total_sum += numbers
    elif numbers == 0:
        break 
       
avg = total_sum/num
print('Average of ', num + 1, ' numbers is :', avg)


# 4.เขียนโปรมแกรมรับค่า input ที่เป็น integer มาหนึ่งตัว ตรวจสอบว่าเลขนั้นหาร 7 ลงตัวหรือไม่
# 
# 	- ถ้าหารลงตัว ให้ปริ้น ‘หาร 7 ลงตัว’
# 
# 	- ถ้าหารไม่ลงตัว ให้ปริ้น ‘หาร 7 ไม่ลงตัว’

# In[9]:


number = int(input('enter a number: ',))

if number % 7 == 0: 
    print('หาร 7 ลงตัว')
else:
    print('หาร 7 ไม่ลงตัว')


# 5.เขียนโปรแกรมรับค่า int มา 3 จำนวน และตรวจสอบว่า 3 เลขนั้นสามารถนำมาสร้าง 3 เหลี่ยมมุมฉากได้หรือไม่

# In[22]:


num1 = int(input('enter a number: ',))
num2 = int(input('enter a number: ',))
num3 = int(input('enter a number: ',))
nums = [num1,num2, num3]
#print(nums)
nums.sort(reverse = True)
#print(nums)

a = nums[0]
b = nums[1]
c = nums[2]

#print(a)
#print(b)
#print(c)

if a ** 2 == b ** 2 + c ** 2:
    print("right traiangle")
    
else: 
    print("not a right traiangle")


# 6.เขียนโปรแกรมรับค่า int มา 3 จำนวน และตรวจสอบว่าเมื่อนำ 3 เลขนั้นมาสร้าง 3 เหลี่ยม จะได้สามเหลี่ยมแบบใด
# 	
# 	- สามเหลี่ยมมุมแหลม
# 
# 	- สามเหลี่ยมมุมป้าน
# 
# 	- สามเหลี่ยมมุมฉาก

# In[11]:


num1 = int(input('enter a number: ',))
num2 = int(input('enter a number: ',))
num3 = int(input('enter a number: ',))
nums = [num1,num2, num3]
#print(nums)
nums.sort(reverse = True)
#print(nums)

a = nums[0]
b = nums[1]
c = nums[2]

#print(a)
#print(b)
#print(c)

if a ** 2 == b ** 2 + c ** 2:
    print("right traiangle")
    
elif a ** 2 > b ** 2 + c ** 2:
    print("obtuse traiangle")
    
elif a ** 2 < b ** 2 + c ** 2:
    print("acute traiangle")


# 7.เขียนโปรแกรมให้รับค่าอาหาร 3 ครั้งที่ไปทานอาหารนอกบ้านล่าสุด โดยแต่ละครั้งต้องไม่ต่ำกว่า 1,000 และไม่เกิน 5,000 (ผู้ใช้ต้องใส่อยู่ในช่วงนี้) และนำค่าอาหารทั้ง 3 ครั้งมาบวกกัน หากเกิน 6,000 บาท จะได้รับส่วนลด 15% หากเกิน 12,000 จะได้รับส่วนลด 25% จงหายอดเงินสุดท้ายที่ต้องจ่าย

# In[14]:


meal1 = float(input('enter a number between 1000 and 5000: ',))
meal2 = float(input('enter a number between 1000 and 5000: ',))
meal3 = float(input('enter a number between 1000 and 5000: ',))

print("Total bill: ", meal1 + meal2 + meal3)

if meal1 + meal2 + meal3 > 12000:
    result1 = (1-0.25)*(meal1 + meal2 + meal3)
    print("Discounted bill = ", result1)
    
elif meal1 + meal2 + meal3 > 6000:
    result2 = (1-0.15)*(meal1 + meal2 + meal3)
    print("Discounted bill = ", result2)


# 8.เขียนโปรแกรมให้รับค่าอาหาร 4 ครั้งที่ไปทานอาหารนอกบ้านล่าสุด โดยแต่ละครั้งต้องไม่ต่ำกว่า 1,000 และไม่เกิน 5,000 (ผู้ใช้ต้องใส่อยู่ในช่วงนี้) และนำค่าอาหาร 3 ครั้งแรกมาบวกกัน หากเกิน 6,000 บาท จะได้รับส่วนลด 15% หากเกิน 12,000 จะได้รับส่วนลด 25% ของมื้อที่ 4 จงหายอดเงินสุดท้ายที่ต้องจ่ายของมื้อที่ 4

# In[15]:


meal1 = float(input('enter a number between 1000 and 5000: ',))
meal2 = float(input('enter a number between 1000 and 5000: ',))
meal3 = float(input('enter a number between 1000 and 5000: ',))
meal4 = float(input('enter a number between 1000 and 5000: ',))

print("Total bill: ", meal1 + meal2 + meal3)

if meal1 + meal2 + meal3 > 12000:
    result1 = (1-0.25)*(meal4)
    print("Discounted bill = ", result1)
    
elif meal1 + meal2 + meal3 > 6000:
    result2 = (1-0.15)*(meal4)
    print("Discounted bill = ", result2)


# 9.เขียนโปรแกรมให้รับค่าอาหาร 4 ครั้งที่ไปทานอาหารนอกบ้านล่าสุด โดยแต่ละครั้งต้องไม่ต่ำกว่า 1,000 และไม่เกิน 5,000 (เขียนให้ผู้ใช้ใส่ใหม่หากไม่อยู่ในช่วงที่กำหนด) และนำค่าอาหาร 3 ครั้งแรกมาบวกกัน หากเกิน 4,000 บาท จะได้รับส่วนลด 25% หากเกิน 9,000 จะได้รับส่วนลด 30% ของมื้อที่ 4 จงหายอดเงินสุดท้ายที่ต้องจ่ายของมื้อที่ 4

# In[1]:


meal1 = float(input('enter a number between 1000 and 5000 (meal1): ',)) 
while meal1 < 1000 or meal1 > 5000:
        meal1 = float(input('enter a number between 1000 and 5000 (meal1): ',))
        
meal2 = float(input('enter a number between 1000 and 5000 (meal2): ',))
while meal2 < 1000 or meal2 > 5000:
        meal2 = float(input('enter a number between 1000 and 5000 (meal2): ',))

meal3 = float(input('enter a number between 1000 and 5000 (meal3): ',))
while meal3 < 1000 or meal3 > 5000:
        meal3 = float(input('enter a number between 1000 and 5000 (meal3): ',))
    
meal4 = float(input('enter a number between 1000 and 5000 (meal4): ',))
while meal4 < 1000 or meal4 > 5000:
        meal4 = float(input('enter a number between 1000 and 5000 (meal4): ',))

total_meals = meal1 + meal2 + meal3
print("Total bill: ", total_meals)

if total_meals > 9000:
    result1 = (1-0.30)*(meal4)
    print("Discounted bill = ", result1)
    
elif total_meals > 4000:
    result2 = (1-0.25)*(meal4)
    print("Discounted bill = ", result2)


# 10.เขียนโปรแกรมให้รับค่าอาหาร 4 ครั้งที่ไปทานอาหารนอกบ้านล่าสุด โดยแต่ละครั้งต้องไม่ต่ำกว่า 1,000 และไม่เกิน 5,000 (เขียนให้ผู้ใช้ใส่ใหม่หากไม่อยู่ในช่วงที่กำหนด) และถามผู้ใช้มีบัตรเครดิตหรือไม่(True/False) นำค่าอาหาร 3 ครั้งแรกมาบวกกัน หากเกิน 4,000 บาท จะได้รับส่วนลด 25% หากเกิน 9,000 จะได้รับส่วนลด 30% ของมื้อที่ 4 หากมีบัตรเครดิต ลดเพิ่มอีก 5%    จงหายอดเงินสุดท้ายที่ต้องจ่ายของมื้อที่ 4
# 

# In[3]:


meal1 = float(input('enter a number between 1000 and 5000 (meal1): ',)) 
while meal1 < 1000 or meal1 > 5000:
        meal1 = float(input('enter a number between 1000 and 5000 (meal1): ',))
        
meal2 = float(input('enter a number between 1000 and 5000 (meal2): ',))
while meal2 < 1000 or meal2 > 5000:
        meal2 = float(input('enter a number between 1000 and 5000 (meal2): ',))

meal3 = float(input('enter a number between 1000 and 5000 (meal3): ',))
while meal3 < 1000 or meal3 > 5000:
        meal3 = float(input('enter a number between 1000 and 5000 (meal3): ',))
    
meal4 = float(input('enter a number between 1000 and 5000 (meal4): ',))
while meal4 < 1000 or meal4 > 5000:
        meal4 = float(input('enter a number between 1000 and 5000 (meal4): ',))
        
total_meals = meal1 + meal2 + meal3
print("Total bill: ", total_meals)

credit_card = str(input('enter Y (have a credit card) or N (no credit card): ',))
if credit_card == 'Y':
    if total_meals > 9000:
        result1 = (1-0.35)*(meal4)
        print("Discounted bill = ", result1)
    elif total_meals > 4000:
        result2 = (1-0.30)*(meal4)
        print("Discounted bill = ", result2)

elif credit_card == 'N':
    if total_meals > 9000:
        result1 = (1-0.30)*(meal4)
        print("Discounted bill = ", result1)
    elif total_meals > 4000:
        result2 = (1-0.25)*(meal4)
        print("Discounted bill = ", result2)


# 11.จงเขียนโปรแกรมรับ input ที่เป็นประโยคแบบ string ที่มีความยาวของคำไม่ต่ำกว่า 7 ตัวอักษรภาษาอังกฤษ(สมมติว่าเป็นคำเดียว) และมีพิมพ์ใหญ่พิมพ์เล็กปนกัน จากนั้นให้ตรวจสอบแต่ละอักษร ให้แปลงพิมพ์ใหญ่เป็นพิมพ์เล็ก และพิมพ์เล็กเป็นพิมพ์ใหญ่พร้อมกับปริ้นออกมา

# In[1]:


word = str(input('enter a word: ',))

for i in word: 
    if i.isupper() == True:
        print(i.lower())
    elif i.islower() == True:
         print(i.upper())


# 12.เขียนโปรแกรมรับ input 4 ตัวที่เป็น string จากนั้นตรวจสอบว่า input ใดมีความยาวมากที่สุด รองลงมา และน้อยที่สุด จากนั้น ปริ้นแต่ละ input ออกมาตามลำดับน้อยสุดไปมากสุด

# In[69]:


word1 = str(input('enter a word: ',))
word2 = str(input('enter a word: ',))
word3 = str(input('enter a word: ',))
word4 = str(input('enter a word: ',))

lst = [word1, word2, word3 , word4]

def Sorting(a):
    a.sort(key=len)
    return a

print(Sorting(lst))


# 13.เขียนโปรแกรมรับ input สองตัวเป็นจำนวนเต็มระหว่าง 0-60 โดยตัวแรกเป็นชั่วโมงและตัวที่สองเป็นนาที คำนวณค่าที่จอดรถถ้าชั่วโมงละ 150 บาท เศษนาทีคิดเป็นนาทีละ 2 บาท

# In[72]:


hour = int(input('enter a number between 0 and 60: ',))
min = int(input('enter a number between 0 and 60: ',))

fee = (hour * 150) + (min * 2)
print("the parking fee is ", fee)


# 14.เขียนโปรแกรมรับ input สองตัวเป็นจำนวนเต็มระหว่าง 0-60 โดยตัวแรกเป็นชั่วโมงและตัวที่สองเป็นนาที คำนวณค่าที่จอดรถถ้าชั่วโมงละ 300 บาท เศษนาทีเกิน 15 นาทีคิดเป็นหนึ่งชั่วโมง หากไม่เกินไม่คิดเงิน และชั่วโมงแรกจอดฟรี

# In[77]:


hour = int(input('enter a number between 0 and 60: ',))
mins = int(input('enter a number between 0 and 60: ',))

total_mins = (hour * 60) + min 

if total_mins > 15:
    fee = hour * 300
elif total_min < 15:
    fee = 0 
    
print("the parking fee is ", fee)


# 15.โรงละครสัตว์มีนก กับ วัว และต้องจ่ายภาษีสัตว์ 2 ขา 150 บาทต่อตัว   จ่ายภาษีสัตว์ 4 ขา 220 บาทต่อตัว เขียนโปรแกรมรับค่า input สองตัว ตัวแรกเป็นผลรวมจำนวนหัวของสัตว์ ตัวสองเป็นผลรวมจำนวนขาของสัตว์ จงหาว่าโรงละครสัตว์ต้องจ่ายภาษีเท่าใด

# In[81]:


number_2legs = int(input("enter number of 2-leg animal: ",))
number_4legs = int(input("enter number of 4-leg animal: ",))

tax = (number_2legs * 150) + (number_4legs * 220)
print("total tax is",tax)    #the question is probobably wrong. too hard to solve it but I figured it out  


# In[49]:


from sympy import Eq, Symbol as sym, solve
x = symbols('x')

total_heads = int(input("enter number of head: ",))
total_legs = int(input("enter number of leg: ",))

bird_heads = x 
cow_heads = total_heads - x 

bird_legs = 2
cow_legs = 4 

eqa = Eq((bird_heads *  bird_legs) + (cow_heads * cow_legs), total_legs)
result = solve(eqa)

bird_heads = result

def convert(list): 
      
    # Converting integer list to string list 
    # and joining the list using join() 
    res = int("".join(map(str, list))) 
      
    return res 
  
# Driver code 

cow_heads = total_heads - convert(bird_heads)

tax = (150 * convert(bird_heads)) + (220 * cow_heads)
print(tax)

