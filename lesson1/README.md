# Lesson 1 Python 入學基本

# 變數 variable
任何數據類型或資料類型都可以用變數來代表

# 數據類型
- 布林   boolean
- 整數   int
- 浮點數 float
- 字串 string
## 布林 boolean
    布林分為 True 跟 False 通常使用在條件是否成立。
## 整數 int ，浮點數 float
    用來記錄、運算數字。
## 字串string
    用來記錄文字資料，可以改變大小寫，擷取裡面的某一段文字，改變裡面的某一段文字

# 資料類型
- 串列 list
- tuple
- 字典 dict
## 串列 list
記錄一連串的資料，可以改變資料的內容。

### 定義一個 list
```python
[1,2,3,4,5]

a_list = [1,2,3,4,5]
```
### 看資料
```python
a_list[0] #從list裡面取出第0個資料
> 1

a_list[1] #從list裡面取出第1個資料
> 2

a_list[0:4] #擷取第0到3的資料
> [1, 2, 3, 4]

a_list[::2] #隔兩格擷取資料
> [1, 3, 5]

a_list[3:] #擷取資料第三個以後的資料
> [4, 5]

a_list[:3] #擷取資料第三個以前的資料
> [1, 2, 3]
```
### 新增資料
```python
print(a_list)
> [1, 2, 3, 4, 5]

a_list.append('拉') # 新增到最後
a_list
> [1, 2, 3, 4, 5, '拉']

a_list.insert(300,3) # 插入到第三個位置
a_list
> [1, 2, 3, 300, 4, 5, '拉']
```

### 更改資料
```python
print(a_list)
> [1, 2, 3, 4, 5] #原本的

a_list[3] = '尛'
a_list
> [1, 2, 3, '尛', 5]
```

### 刪除資料
```python
print(a_list)
> [1, 2, 3, 4, 5]

del a_list[2] # 刪除第2個
a_list
> [1, 2, 4, 5]
```
## tuple
記錄一連串的資料，無法改變資料的內容，只能取用內容。
```python
(1,2,3) # 定義一個tuple
1,2,3   # 或是這樣
a_tuple = 1,2,3 #放到變數裡
```
### 看資料
```python
a_tuple[0]
> 1
```
### 取資料 unpack
```python
a,b,c = a_tuple
a
> 1
b
> 2
c
> 3
```

### 無法改變資料
```python
a_tuple[0]='尛'
>
TypeError                                 Traceback (most recent call last)
<ipython-input-46-cf0e1ae15f73> in <module>
      1 #不能改變
----> 2 a_tuple[0]='尛'

TypeError: 'tuple' object does not support item assignment
```

## 字典 dict
記錄一連串的資料，可以改變資料的內容，並增加一個可以代表內容的索引

### 定義一個 dict
```python
#前面他的名字，後面他的內容，內容可以是 int dict list .... 各種形式，但名字只能一個，不能重複。
{"HP_800_G3":200,"HP_800_G4":300} 
a = {"intel_chip":['tiger lake','elder lake']}
a = dict() #建立空的dict
```

### 新增、修改資料
```python
HP_Products = {"HP_800_G3":200,"HP_800_G4":300}
print(HP_Products,' <-- 原本的')
> {'HP_800_G3': 200, 'HP_800_G4': 300}  <-- 原本的

HP_Products.update({"HP_800_G5":400})
print(HP_Products,' <-- 增加 G5的資料')
> {'HP_800_G3': 200, 'HP_800_G4': 300, 'HP_800_G5': 400}  <-- 增加 G5的資料

HP_Products.update({"HP_800_G5":500})
print(HP_Products, ' <-- 修改 G5的資料')
> {'HP_800_G3': 200, 'HP_800_G4': 300, 'HP_800_G5': 500}  <-- 修改 G5的資料

# 或是
HP_Products["HP_800_G6"] = 500
print(HP_Products,' <-- 增加 G6的資料')
> {'HP_800_G3': 200, 'HP_800_G4': 300, 'HP_800_G5': 500, 'HP_800_G6': 500}  <-- 增加 G6的資料

HP_Products["HP_800_G6"] = 700
print(HP_Products, ' <-- 修改 G6的資料')
> 'HP_800_G3': 200, 'HP_800_G4': 300, 'HP_800_G5': 500, 'HP_800_G6': 700}  <-- 
修改 G6的資料
```
### 確認資料有沒有在裡面
```python
'HP_800_G6' in HP_Products
> True
```
### 取得一個資料的內容
```python
print(HP_Products['HP_800_G6'])
> 700

print(HP_Products.get('HP_800_G7',None)) # None是如果沒有HP_800_G7這個資料的話 則選擇None
> None
```

### 查看所有資料的名字
```python
HP_Products.keys()
> dict_keys(['HP_800_G3', 'HP_800_G4', 'HP_800_G5', 'HP_800_G6'])
```
### 查看所有資料的內容
```python
HP_Products.values()
> dict_values([200, 300, 500, 700])
```

### 查看所有資料名字跟內容
```python
HP_Products.items()
> dict_items([('HP_800_G3', 200), ('HP_800_G4', 300), ('HP_800_G5', 500), ('HP_800_G6', 700)])
```

### 刪除資料
```python
del HP_Products["HP_800_G6"]
print(HP_Products, ' <-- 刪除了 G6的資料')
> {'HP_800_G3': 200, 'HP_800_G4': 300, 'HP_800_G5': 500}  <-- 刪除了 G6的資料
HP_Products.clear()
print(HP_Products,' <-- 清除所有資料')
> {} <-- 清除所有資料
```

# 程式流程
- [ 🚧 ] if....else
- [ 🚧 ] if....elif....else
- for loop
- while loop

## for loop
for loop 可以應用在 list,str,dict,set,tuple, 主要是用來一個一個查看裡面的資料
```python
cars = ['BMW','Benz','Ford','Toyota','Vlokswagon']
for car in cars: # car 是代表cars裡面內容的變數，只在for裡面有效，for以外會沒有宣告 <- 就是所謂的區域變數，在：裡面有效而已 
    print(car)
>
BMW
Benz
Ford
Toyota
Vlokswagon
```
range 可以把它看成是一個list的產生器
ex: range(3) 就像他會產生出 [0,1,2] 這樣
```python
for i in range(3):
    print(i)
>
0
1
2
```
## Function
當有了變數跟區域變數的觀念，接下來就是function
## 宣告function
### 基本的function宣告：
```python
def function_name():
    ...
```
有return的就代表他做完function有回傳一個結果：
下面的例子是回傳一個字串
```python
def function的名字() -> str:
     for...: 
         if..:
             ... 
         else: 
             ..... 
        ..... 
    return 'something'
```
有變數的function宣告：
```python
def break_the_car(cars:list,broken:bool) -> str:
    if broken:
    ....
    cars...
    broken_car_list = ...
    return broken_car_list + 'broken'
```


