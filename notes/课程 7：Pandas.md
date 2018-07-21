# 课程 7：pandas

[TOC]

## pandas 简介

pandas 是 Python 中的数据操纵和分析软件包。

pandas 为 Python 带来了两个新的数据结构，即 Series 和 DataFrame。借助这两个数据结构，我们能够轻松直观地处理带标签数据和关系数据。这些课程将简单介绍 pandas，并讲解一些最重要的 pandas 功能。

在下面的课程中，你将学习：

- 导入 pandas
- 创建 Series 和 DataFrame
- 访问和修改 Series 和 DataFrame
- Series 的算术运算
- DataFrame 的数据加载
- 处理 NaN 值

学习以下课程的前提是你已经熟悉 NumPy。

### 下载 pandas

Anaconda 中包含 pandas。如果你的计算机尚未安装 Anaconda，请参阅 Anaconda 部分，详细了解如何在 PC 或 Mac 设备上安装 Anaconda。

### pandas 版本

和很多 Python 软件包一样，pandas 也会时不时地更新。以下课程在制作时采用的是 pandas 0.22 版。你可以检查你的 pandas 版本：在 Jupyter notebook 中输入 !conda list pandas，或在 Anaconda 提示符处输入 conda list pandas。如果你的计算机安装的是另一个版本的 pandas，你可以通过在 Anaconda 提示符处输入 conda install pandas=0.22 更新你的 pandas 版本。随着新版 pandas 的推出，一些功能可能会过时或被替换掉，因此确保在运行代码前，安装正确的 pandas 版本。这样可以保证代码顺利运行。

### pandas 文档

pandas 是一个强大的数据分析库，其中包含很多函数和功能。在这些入门课程中，我们将仅介绍 pandas 的一些基本功能。如果你想深入学习 pandas，确保参阅 pandas 文档：

[pandas 文档](https://pandas.pydata.org/pandas-docs/stable/)

## 为何要使用 pandas？

机器学习算法能取得最近的飞速发展，部分原因就是我们可以用大量数据训练算法。但是，对于数据来说，**数量并不是唯一重要的方面，数据质量也同等重要**。经常大型数据库并不能直接馈送到学习算法中。很多时候，大型数据集缺失值、存在离群值、不正确的值，等等…例如，如果数据存在大量丢失值或糟糕值，机器学习算法将无法达到很好的性能。

**因此，机器学习的重要一步是首先检查数据，通过进行一些基本的数据分析，确保数据很适合你的训练算法**。

这时候，pandas 就派上用场了。pandas Series 和 DataFrame 专门用于快速进行数据分析和操纵，并且使用起来灵活简单。以下是使 pandas 成为出色的数据分析软件包的几个功能：

- 允许为行和列设定标签
- 可以针对时间序列数据计算滚动统计学指标
- 轻松地处理 NaN 值
- 能够将不同格式的数据加载到 DataFrame 中
- 可以将不同的数据集合并到一起
- 与 NumPy 和 Matplotlib 集成

pandas DataFrame 已经成为 Python 中最常用的数据分析 pandas 对象之一。

## 创建 pandas Series

Series 是像数组一样的一维对象，可以存储很多类型的数据，例如数字或字符串。

pandas Series 和 NumPy ndarray 之间的主要区别之一是你可以为 pandas Series 中的每个元素**分配索引标签**。

pandas Series 和 NumPy ndarrays 之间的另一个明显区别是 pandas Series 可以**存储不同类型的数据**。

我们先在 Python 中导入 pandas。通常，我们使用 pd 导入 pandas。因此，你可以在 Jupyter Notebook 中输入以下命令，导入 pandas：

```py
import pandas as pd
```

我们先创建一个 Series。你可以使用 `pd.Series(data, index)` 命令创建 pandas Series，其中 index 是一个索引标签列表。我们使用 Series 存储一个购物清单。我们将使用食品条目作为索引标签，使用购买数量作为数据。

```py
# We import pandas as pd into Python
import pandas as pd

# We create a pandas Series that stores a grocery list
groceries = pd.Series(data = [30, 6, 'Yes', 'No'], index = ['eggs', 'apples', 'milk', 'bread'])

# We display the Groceries pandas Series
groceries
eggs           30
apples         6
milk         Yes
bread       No
dtype: object
```

可以看出 pandas Series 的显示方式为：第一列是索引，第二列是数据。注意，数据的索引不是从 0 到 3，而是采用我们设置的食品名称，即鸡蛋、苹果、等...此外注意，我们的 pandas Series 中的数据既包括整数，又包括字符串。

和 NumPy ndarray 一样，通过 pandas Series 的一些属性，我们可以轻松地获取 series 中的信息。我们来看一些属性：

```py
# We print some information about Groceries
print('Groceries has shape:', groceries.shape)
print('Groceries has dimension:', groceries.ndim)
print('Groceries has a total of', groceries.size, 'elements')
Groceries has shape: (4,)
Groceries has dimension: 1
Groceries has a total of 4 elements
```

我们还可以单独输出 pandas Series 的索引标签和数据。如果你不知道 pandas Series 的索引标签是什么，这种方法就很有用。

```py
# We print the index and data of Groceries
print('The data in Groceries is:', groceries.values)
print('The index of Groceries is:', groceries.index)
The data in Groceries is: [30 6 'Yes' 'No']
The index of Groceries is: Index(['eggs', 'apples', 'milk', 'bread'], dtype='object')
```

如果你处理的是非常庞大的 pandas Series，并且不清楚是否存在某个索引标签，可以使用 in 命令检查是否存在该标签：

```py
# We check whether bananas is a food item (an index) in Groceries
x = 'bananas' in groceries

# We check whether bread is a food item (an index) in Groceries
y = 'bread' in groceries

# We print the results
print('Is bananas an index label in Groceries:', x)
print('Is bread an index label in Groceries:', y)
Is bananas an index label in Groceries: False
Is bread an index label in Groceries: True
```

## 访问和删除 pandas Series 中的元素

现在我们来了解如何访问或修改 pandas Series 中的元素。pandas Series 的一大优势是我们能够以很多不同的方式访问数据。我们可以通过在方括号 [ ] 内添加索引标签或数字索引访问元素，就像访问 NumPy ndarray 中的元素一样。因为我们可以使用数字索引，因此可以使用正整数从 Series 的开头访问数据，或使用负整数从末尾访问。因为我们可以通过多种方式访问元素，为了清晰地表明我们指代的是索引标签还是数字索引，pandas Series 提供了两个属性 .loc 和 .iloc，帮助我们清晰地表明指代哪种情况。属性 .loc 表示 位置，用于明确表明我们使用的是标签索引。同样，属性 .iloc 表示整型位置，用于明确表明我们使用的是数字索引。我们来看一些示例：

```py
# We access elements in Groceries using index labels:

# We use a single index label
print('How many eggs do we need to buy:', groceries['eggs'])
print()

# we can access multiple index labels
print('Do we need milk and bread:\n', groceries[['milk', 'bread']]) 
print()

# we use loc to access multiple index labels
print('How many eggs and apples do we need to buy:\n', groceries.loc[['eggs', 'apples']]) 
print()

# We access elements in Groceries using numerical indices:

# we use multiple numerical indices
print('How many eggs and apples do we need to buy:\n',  groceries[[0, 1]]) 
print()

# We use a negative numerical index
print('Do we need bread:\n', groceries[[-1]]) 
print()

# We use a single numerical index
print('How many eggs do we need to buy:', groceries[0]) 
print()
# we use iloc to access multiple numerical indices
print('Do we need milk and bread:\n', groceries.iloc[[2, 3]])
```

```
How many eggs do we need to buy: 30

Do we need milk and bread:
milk       Yes
bread     No
dtype: object

How many eggs and apples do we need to buy:
eggs       30
apples     6
dtype: object

How many eggs and apples do we need to buy:
eggs       30
apples     6
dtype: object

Do we need bread:
bread     No
dtype: object

How many eggs do we need to buy: 30

Do we need milk and bread:
milk       Yes
bread     No
dtype: object
```

和 NumPy ndarray 一样，pandas Series 也是可变的，也就是说，创建好 pandas Series 后，我们可以更改其中的元素。例如，我们更改下购物清单中的鸡蛋购买数量

```py
# We display the original grocery list
print('Original Grocery List:\n', groceries)

# We change the number of eggs to 2
groceries['eggs'] = 2

# We display the changed grocery list
print()
print('Modified Grocery List:\n', groceries)
```

```
Original Grocery List:
eggs           30
apples         6
milk         Yes
bread       No
dtype: object

Modified Grocery List:
eggs             2
apples         6
milk         Yes
bread       No
dtype: object
```

我们还可以使用 .drop() 方法删除 pandas Series 中的条目。Series.drop(label) 方法会从给定 Series 中删除给定的 label。请注意，Series.drop(label) 方法不在原地地从 Series 中删除元素，即不会更改被修改的原始 Series。我们来看看代码编写方式

```py
# We display the original grocery list
print('Original Grocery List:\n', groceries)

# We remove apples from our grocery list. The drop function removes elements out of place
print()
print('We remove apples (out of place):\n', groceries.drop('apples'))

# When we remove elements out of place the original Series remains intact. To see this
# we display our grocery list again
print()
print('Grocery List after removing apples out of place:\n', groceries)
```

```
Original Grocery List:
eggs           30
apples         6
milk         Yes
bread       No
dtype: object

We remove apples (out of place):
eggs           30
milk         Yes
bread       No
dtype: object

Grocery List after removing apples out of place:
eggs           30
apples         6
milk         Yes
bread       No
dtype: object
```

我们可以通过在 .drop() 方法中将关键字 inplace 设为 True，原地地从 pandas Series 中删除条目。我们来看一个示例：

```py
# We display the original grocery list
print('Original Grocery List:\n', groceries)

# We remove apples from our grocery list in place by setting the inplace keyword to True
groceries.drop('apples', inplace = True)

# When we remove elements in place the original Series its modified. To see this
# we display our grocery list again
print()
print('Grocery List after removing apples in place:\n', groceries)
```

```
Original Grocery List:
eggs           30
apples         6
milk         Yes
bread       No
dtype: object

Grocery List after removing apples in place:
eggs           30
milk         Yes
bread       No
dtype: object
```

## 对 pandas Series 执行算术运算

和 NumPy ndarray 一样，我们可以对 pandas Series 执行元素级算术运算。在这节课，我们将了解 pandas Series 和单个数字之间的算术运算。我们创建一个新的 pandas Series，用于存储只有水果的购物清单。

```py
# We create a pandas Series that stores a grocery list of just fruits
fruits= pd.Series(data = [10, 6, 3,], index = ['apples', 'oranges', 'bananas'])

# We display the fruits pandas Series
fruits
apples         10
oranges        6
bananas       3
dtype: int64
```

我们现在可以通过执行基本的算术运算，修改 fruits 中的数据。我们来看一些示例：

```py
# We print fruits for reference
print('Original grocery list of fruits:\n ', fruits)

# We perform basic element-wise operations using arithmetic symbols
print()
print('fruits + 2:\n', fruits + 2) # We add 2 to each item in fruits
print()
print('fruits - 2:\n', fruits - 2) # We subtract 2 to each item in fruits
print()
print('fruits * 2:\n', fruits * 2) # We multiply each item in fruits by 2 
print()
print('fruits / 2:\n', fruits / 2) # We divide each item in fruits by 2
print()
```

```
Original grocery list of fruits:
apples         10
oranges        6
bananas       3
dtype: int64

fruits + 2:
apples         12
oranges        8
bananas       5
dtype: int64

fruits - 2:
apples           8
oranges        4
bananas       1
dtype: int64

fruits * 2:
apples         20
oranges      12
bananas       6
dtype: int64

fruits / 2:
apples           5.0
oranges        3.0
bananas       1.5
dtype: float64
```

我们还可以对 pandas Series 中的所有元素应用 NumPy 中的数学函数，例如 sqrt(x)。

```py
# We import NumPy as np to be able to use the mathematical functions
import numpy as np

# We print fruits for reference
print('Original grocery list of fruits:\n', fruits)

# We apply different mathematical functions to all elements of fruits
print()
print('EXP(X) = \n', np.exp(fruits))
print() 
print('SQRT(X) =\n', np.sqrt(fruits))
print()
print('POW(X,2) =\n',np.power(fruits,2)) # We raise all elements of fruits to the power of 2
```

```
Original grocery list of fruits:
apples         10
oranges        6
bananas       3
dtype: int64

EXP(X) =
apples        22026.465795
oranges         403.428793
bananas          20.085537
dtype: float64

SQRT(X) =
apples            3.162278
oranges         2.449490
bananas        1.732051
dtype: float64

POW(X,2) =
apples         100
oranges        36
bananas         9
dtype: int64
```

pandas 还允许我们仅对 fruits 购物清单中的部分条目应用算术运算。我们来看一些示例：

```py
# We print fruits for reference
print('Original grocery list of fruits:\n ', fruits)
print()

# We add 2 only to the bananas
print('Amount of bananas + 2 = ', fruits['bananas'] + 2)
print()

# We subtract 2 from apples
print('Amount of apples - 2 = ', fruits.iloc[0] - 2)
print()

# We multiply apples and oranges by 2
print('We double the amount of apples and oranges:\n', fruits[['apples', 'oranges']] * 2)
print()

# We divide apples and oranges by 2
print('We half the amount of apples and oranges:\n', fruits.loc[['apples', 'oranges']] / 2)
```

```
Original grocery list of fruits:
apples         10
oranges        6
bananas       3
dtype: int64

Amount of bananas + 2 = 5

Amount of apples - 2 = 8

We double the amount of apples and oranges:
apples         20
oranges      12
dtype: int64

We half the amount of apples and oranges:
apples         5.0
oranges      3.0
dtype: float64
```

你还可以对具有混合数据类型的 pandas Series 应用算术运算，前提是该算术运算适合 Series 中的所有数据类型，否则会出错。我们来看看将购物清单乘以 2 会发生什么

```py
# We multiply our grocery list by 2
groceries * 2
eggs                 60
apples             12
milk         YesYes
bread        NoNo
dtype: object
```

可以看出，在上述示例中，我们乘以了 2，pandas 使每个条目的数据翻倍，包括字符串。pandas 能够这么操作是因为，乘法运算 * 对数字和字符串来说都可行。如果你要应用对数字有效但是对字符串无效的运算，例如 /，则会出错。如果 pandas Series 中有混合类型的数据，确保对于所有的元素数据类型，这些算术运算都有效。

## 创建 DataFrame

DataFrame 是具有带标签的行和列的二维数据结构，可以存储很多类型的数据。

如果你熟悉 Excel 的话，可以将 pandas DataFrames 看做类似于电子表格。

在接下来的课程中，我们将开始学习如何手动地通过字典创建 pandas DataFrame，稍后，我们将学习如何将数据文件中的数据加载到 DataFrame 中。

首先，我们将使用 pandas Series 字典手动创建一个 DataFrame。第一步是创建 pandas Series 字典。字典创建完毕后，我们可以将该字典传递给 pd.DataFrame() 函数。

我们将创建一个字典，其中包含 Alice 和 Bob 从在线商店中购买的商品。该 pandas Series 将使用所买商品的价格作为数据，所买商品作为索引标签。我们来看看如何编写代码：

```py
# We import pandas as pd into Python
import pandas as pd

# We create a dictionary of pandas Series 
items = {'Bob' : pd.Series(data = [245, 25, 55], index = ['bike', 'pants', 'watch']),
         'Alice' : pd.Series(data = [40, 110, 500, 45], index = ['book', 'glasses', 'bike', 'pants'])}

# We print the type of items to see that it is a dictionary
print(type(items))
```

```
class 'dict'
```

字典已经创建完毕，我们可以通过将其传递给 pd.DataFrame() 函数，创建 DataFrame。我们将创建一个可以表示多位用户的购物车的 DataFrame，在此例中只有两位用户，即 Alice 和 Bob。

```py
# We create a pandas DataFrame by passing it a dictionary of pandas Series
shopping_carts = pd.DataFrame(items)

# We display the DataFrame
shopping_carts
```

? | Alice | Bob
---|---|---
bike | 500.0 | 245.0
book | 40.0	| NaN
glasses | 110.0 | NaN
pants | 45.0 | 25.0
watch | NaN | 55.0

有几个事项需要注意。我们发现 DataFrame 以表格形式显示，和 Excel 电子表格很像，行和列的标签以粗体形式显示。此外注意，DataFrame 的行标签根据构建字典所用的两个 pandas Series 的索引标签创建而成。DataFrame 的列标签来自字典的键。另一个注意事项是，列按照字母顺序排序，而不是字典中的顺序。稍后我们将发现，当我们从数据文件中向 DataFrame 加载数据时，不会发生这种情况。最后要注意的是，我们发现该 DataFrame 中出现了一些 NaN 值。NaN 是指非数字，pandas 通过这种方式表示该行和列索引没有值。例如，如果我们查看 Alice 列，我们发现手表索引的值是 NaN。你可以通过查看一开始创建的字典，了解为何是这种情况。可以清晰地看出，Alice 手表标签没有条目。因此，在创建 DataFrame 时，如果特定行索引的特定列没有值，pandas 将用 NaN 值填充。如果要将此数据馈送到机器学习算法中，我们首先需要删掉这些 NaN 值。在后面的课程中，我们将学习如何处理 NaN 值以及如何清理数据。暂时先将这些值留在我们的 DataFrame 中。

在上述示例中，我们使用具有定义清晰的索引的 pandas Series 字典创建了 pandas DataFrame。如果我们不向 pandas Series 提供索引标签，pandas 在创建 DataFrame 时将使用数字行索引。我们来看一个示例：

```py
# We create a dictionary of pandas Series without indexes
data = {'Bob' : pd.Series([245, 25, 55]),
        'Alice' : pd.Series([40, 110, 500, 45])}

# We create a DataFrame
df = pd.DataFrame(data)

# We display the DataFrame
df
```

? | Alice | Bob
---|---|---
0 | 40 | 245.0
1| 110	| 25.0
2 | 500 | 55.0
3 | 45 | NaN

可以看出，pandas DataFrame 的行索引从 0 开始，就像 NumPy ndarray 的索引一样。

现在，和 pandas Series 一样，我们也可以使用属性从 DataFrame 中提取信息。我们输出 shopping_carts DataFrame 中的一些信息

```py
# We print some information about shopping_carts
print('shopping_carts has shape:', shopping_carts.shape)
print('shopping_carts has dimension:', shopping_carts.ndim)
print('shopping_carts has a total of:', shopping_carts.size, 'elements')
print()
print('The data in shopping_carts is:\n', shopping_carts.values)
print()
print('The row index in shopping_carts is:', shopping_carts.index)
print()
print('The column index in shopping_carts is:', shopping_carts.columns)
```

```
shopping_carts has shape: (5, 2)
shopping_carts has dimension: 2
shopping_carts has a total of: 10 elements

The data in shopping_carts is:
[[    500.    245.]
[       40.     nan]
[     110.     nan]
[       45.      25.]
[     nan       55.]]

The row index in shopping_carts is: Index(['bike', 'book', 'glasses', 'pants', 'watch'], dtype='object')

The column index in shopping_carts is: Index(['Alice', 'Bob'], dtype='object')
```

在 shopping_carts DataFrame 时，我们将整个字典传递给了 pd.DataFrame() 函数。但是，有时候你可能只对一部分数据感兴趣。在 pandas 中，我们可以通过关键字 columns 和 index 选择要将哪些数据放入 DataFrame 中。我们来看一些示例：

```py
# We Create a DataFrame that only has Bob's data
bob_shopping_cart = pd.DataFrame(items, columns=['Bob'])

# We display bob_shopping_cart
bob_shopping_cart
```

? | Bob
---|---
bike | 245
pants | 25
watch | 55

```py
# We Create a DataFrame that only has selected items for both Alice and Bob
sel_shopping_cart = pd.DataFrame(items, index = ['pants', 'book'])

# We display sel_shopping_cart
sel_shopping_cart
```

? | Alice | Bob
---|---|---
pants | 45 | 25.0
book | 40 | NaN

```py
# We Create a DataFrame that only has selected items for Alice
alice_sel_shopping_cart = pd.DataFrame(items, index = ['glasses', 'bike'], columns = ['Alice'])

# We display alice_sel_shopping_cart
alice_sel_shopping_cart
```

你还可以使用列表（数组）字典手动地创建 DataFrame。流程和之前一样，首先创建一个字典，然后将该字典传递给 pd.DataFrame() 函数。但是在这种情况下，字典中的所有列表（数组）长度必须一样。我们来看一个示例：

```py
# We create a dictionary of lists (arrays)
data = {'Integers' : [1,2,3],
        'Floats' : [4.5, 8.2, 9.6]}

# We create a DataFrame 
df = pd.DataFrame(data)

# We display the DataFrame
df
```

注意，因为我们创建的 data 字典没有标签索引，因此 pandas 在创建 DataFrame 时自动使用数字行索引。但是，我们可以通过在 pd.DataFrame() 函数中使用关键字 index，为行索引添加标签。我们来看一个示例：

```py
# We create a dictionary of lists (arrays)
data = {'Integers' : [1,2,3],
        'Floats' : [4.5, 8.2, 9.6]}

# We create a DataFrame and provide the row index
df = pd.DataFrame(data, index = ['label 1', 'label 2', 'label 3'])

# We display the DataFrame
df
```

手动创建 pandas DataFrame 的最后一种方式是使用 Python 字典列表。流程和之前一样，我们先创建字典，然后将该字典传递给 pd.DataFrame() 函数。

```py
# We create a list of Python dictionaries
items2 = [{'bikes': 20, 'pants': 30, 'watches': 35}, 
          {'watches': 10, 'glasses': 50, 'bikes': 15, 'pants':5}]

# We create a DataFrame 
store_items = pd.DataFrame(items2)

# We display the DataFrame
store_items
```

同样注意，因为我们创建的 items2 字典没有标签索引，因此 pandas 在创建 DataFrame 时自动使用数字行索引。和之前一样，我们可以通过在 pd.DataFrame() 函数中使用关键字 index，为行索引添加标签。假设我们将使用该 DataFrame 存储某个商店的商品库存数量。我们将行索引的标签设为 store 1 和 store 2。

```py
# We create a list of Python dictionaries
items2 = [{'bikes': 20, 'pants': 30, 'watches': 35}, 
          {'watches': 10, 'glasses': 50, 'bikes': 15, 'pants':5}]

# We create a DataFrame  and provide the row index
store_items = pd.DataFrame(items2, index = ['store 1', 'store 2'])

# We display the DataFrame
store_items
```

## 访问 pandas DataFrame 中的元素

我们可以通过多种不同的方式访问 pandas DataFrame 中的元素。

通常，我们可以使用行和列标签访问 DataFrame 的行、列或单个元素。

我们使用在上节课创建的 `store_items` DataFrame。我们来看一些示例：

```py
# We print the store_items DataFrame
print(store_items)

# We access rows, columns and elements using labels
print()
print('How many bikes are in each store:\n', store_items[['bikes']])
print()
print('How many bikes and pants are in each store:\n', store_items[['bikes', 'pants']])
print()
print('What items are in Store 1:\n', store_items.loc[['store 1']])
print()
print('How many bikes are in Store 2:', store_items['bikes']['store 2'])
```

bikes	glasses	pants	watches
store 1	20	NaN	30	35
store 2	15	50.0	5	10
How many bikes are in each store:

bikes
store 1	20
store 2	15
How many bikes and pants are in each store:

bikes	pants
store 1	20	30
store 2	15	5
What items are in Store 1:

bikes	glasses	pants	watches
store 1	20	NaN	30	35
How many bikes are in Store 2: 15

请注意，在访问 DataFrame 中的单个元素时，就像上个示例一样，必须始终提供标签，并且列标签在前，格式为 `dataframe[column][row]`。例如，在检索商店 2 中的自行车数量时，我们首先使用列标签 bikes，然后使用行标签 store 2。如果先提供行标签，将出错。

我们还可以通过添加行或列修改 DataFrame。我们先了解如何向 DataFrame 中添加新的列。

假设我们想添加每个商店的衬衫库存。为此，我们需要向 `store_items` DataFrame 添加一个新列，表示每个商店的衬衫库存。我们来编写代码：

```py
# We add a new column named shirts to our store_items DataFrame indicating the number of shirts in stock at each store. We
# will put 15 shirts in store 1 and 2 shirts in store 2
store_items['shirts'] = [15,2]

# We display the modified DataFrame
store_items
```

bikes	glasses	pants	watches	shirts
store 1	20	NaN	30	35	15
store 2	15	50.0	5	10	2

可以看出，当我们添加新的列时，新列添加到了 DataFrame 的末尾。

还可以使用算术运算符向 DataFrame 中的其他列之间添加新列。我们来看一个示例：

```py
# We make a new column called suits by adding the number of shirts and pants
store_items['suits'] = store_items['pants'] + store_items['shirts']

# We display the modified DataFrame
store_items
```

bikes	glasses	pants	watches	shirts	suits
store 1	20	NaN	30	35	15	45
store 2	15	50.0	5	10	2	7

假设现在你开了一家新店，需要将该商店的商品库存添加到 DataFrame 中。为此，我们可以向 store_items Dataframe 中添加一个新行。要向 DataFrame 中添加行，我们首先需要创建新的 Dataframe，然后将其附加到原始 DataFrame 上。我们来看看代码编写方式

```py
# We create a dictionary from a list of Python dictionaries that will number of items at the new store
new_items = [{'bikes': 20, 'pants': 30, 'watches': 35, 'glasses': 4}]

# We create new DataFrame with the new_items and provide and index labeled store 3
new_store = pd.DataFrame(new_items, index = ['store 3'])

# We display the items at the new store
new_store
bikes	glasses	pants	watches
store 3	20	4	30	35
现在，我们使用 .append() 方法将此行添加到 store_items DataFrame 中。

# We append store 3 to our store_items DataFrame
store_items = store_items.append(new_store)

# We display the modified DataFrame
store_items
```

bikes	glasses	pants	shirts	suits	watches
store 1	20	NaN	30	15.0	45.0	35
store 2	15	50.0	5	2.0	7.0	10
store 3	20	4.0	30	NaN	NaN	35

注意，将新行附加到 DataFrame 后，列按照字母顺序排序了。

我们还可以仅使用特定列的特定行中的数据向 DataFrame 添加新的列。例如，假设你想在商店 2 和 3 中上一批新手表，并且新手表的数量与这些商店原有手表的库存一样。我们来看看如何编写代码

```py
# We add a new column using data from particular rows in the watches column
store_items['new watches'] = store_items['watches'][1:]

# We display the modified DataFrame
store_items
```

bikes	glasses	pants	shirts	suits	watches	new watches
store 1	20	NaN	30	15.0	45.0	35	NaN
store 2	15	50.0	5	2.0	7.0	10	10.0
store 3	20	4.0	30	NaN	NaN	35	35.0

我们还可以将新列插入 DataFrames 的任何位置。dataframe.insert(loc,label,data) 方法使我们能够将新列（具有给定列标签和给定数据）插入 dataframe 的 loc 位置。我们将名称为 shoes 的新列插入 suits 列前面。因为 suits 的数字索引值为 4，我们将此值作为 loc。我们来看看代码编写方式：

```py
# We insert a new column with label shoes right before the column with numerical index 4
store_items.insert(4, 'shoes', [8,5,0])

# we display the modified DataFrame
store_items
```

bikes	glasses	pants	shirts	shoes	suits	watches	new watches
store 1	20	NaN	30	15.0	8	45.0	35	NaN
store 2	15	50.0	5	2.0	5	7.0	10	10.0
store 3	20	4.0	30	NaN	0	NaN	35	35.0

就像我们可以添加行和列一样，我们也可以删除它们。要删除 DataFrame 中的行和列，我们将使用 .pop() 和 .drop() 方法。.pop() 方法仅允许我们删除列，而 .drop() 方法可以同时用于删除行和列，只需使用关键字 axis 即可。我们来看一些示例：

```py
# We remove the new watches column
store_items.pop('new watches')

# we display the modified DataFrame
store_items
bikes	glasses	pants	shirts	shoes	suits	watches
store 1	20	NaN	30	15.0	8	45.0	35
store 2	15	50.0	5	2.0	5	7.0	10
store 3	20	4.0	30	NaN	0	NaN	35
# We remove the watches and shoes columns
store_items = store_items.drop(['watches', 'shoes'], axis = 1)

# we display the modified DataFrame
store_items
bikes	glasses	pants	shirts	suits
store 1	20	NaN	30	15.0	45.0
store 2	15	50.0	5	2.0	7.0
store 3	20	4.0	30	NaN	NaN
# We remove the store 2 and store 1 rows
store_items = store_items.drop(['store 2', 'store 1'], axis = 0)

# we display the modified DataFrame
store_items
```

bikes	glasses	pants	shirts	suits
store 3	20	4.0	30	NaN	NaN

有时候，我们可能需要更改行和列标签。我们使用 .rename() 方法将 bikes 列标签改为 hats

```py
# We change the column label bikes to hats
store_items = store_items.rename(columns = {'bikes': 'hats'})

# we display the modified DataFrame
store_items
hats	glasses	pants	shirts	suits
store 3	20	4.0	30	NaN	NaN
现在再次使用 .rename() 方法更改行标签。

# We change the row label from store 3 to last store
store_items = store_items.rename(index = {'store 3': 'last store'})

# we display the modified DataFrame
store_items
hats	glasses	pants	shirts	suits
last store	20	4.0	30	NaN	NaN
你还可以将索引改为 DataFrame 中的某个列。

# We change the row index to be the data in the pants column
store_items = store_items.set_index('pants')

# we display the modified DataFrame
store_items
```

pants	hats	glasses	shirts	suits
30	20	4.0	NaN	NaN

## 处理 NaN

正如之前提到的，在能够使用大型数据集训练学习算法之前，我们通常需要先清理数据。也就是说，我们需要通过某个方法检测并更正数据中的错误。虽然任何给定数据集可能会出现各种糟糕的数据，例如离群值或不正确的值，但是我们几乎始终会遇到的糟糕数据类型是缺少值。正如之前看到的，pandas 会为缺少的值分配 NaN 值。在这节课，我们将学习如何检测和处理 NaN 值。

首先，我们将创建一个具有一些 NaN 值的 DataFrame。

```py
# We create a list of Python dictionaries
items2 = [{'bikes': 20, 'pants': 30, 'watches': 35, 'shirts': 15, 'shoes':8, 'suits':45},
{'watches': 10, 'glasses': 50, 'bikes': 15, 'pants':5, 'shirts': 2, 'shoes':5, 'suits':7},
{'bikes': 20, 'pants': 30, 'watches': 35, 'glasses': 4, 'shoes':10}]

# We create a DataFrame  and provide the row index
store_items = pd.DataFrame(items2, index = ['store 1', 'store 2', 'store 3'])

# We display the DataFrame
store_items
```

bikes	glasses	pants	shirts	shoes	suits	watches
store 1	20	NaN	30	15.0	8	45.0	35
store 2	15	50.0	5	2.0	5	7.0	10
store 3	20	4.0	30	NaN	10	NaN	35

可以清晰地看出，我们创建的 DataFrame 具有 3 个 NaN 值：商店 1 中有一个，商店 3 中有两个。但是，如果我们向 DataFrame 中加载非常庞大的数据集，可能有数百万条数据，那么就不太容易直观地发现 NaN 值的数量。对于这些情形，我们结合使用多种方法来计算数据中的 NaN 值的数量。以下示例同时使用了 .isnull() 和 sum() 方法来计算我们的 DataFrame 中的 NaN 值的数量。

```py
# We count the number of NaN values in store_items
x =  store_items.isnull().sum().sum()

# We print x
print('Number of NaN values in our DataFrame:', x)
```

Number of NaN values in our DataFrame: 3

在上述示例中，.isnull() 方法返回一个大小和 store_items 一样的布尔型 DataFrame，并用 True 表示具有 NaN 值的元素，用 False 表示非 NaN 值的元素。我们来看一个示例：

```py
store_items.isnull()
```

bikes	glasses	pants	shirts	shoes	suits	watches
store 1	False	True	False	False	False	False	False
store 2	False	False	False	False	False	False	False
store 3	False	False	False	True	False	True	False

在 pandas 中，逻辑值 True 的数字值是 1，逻辑值 False 的数字值是 0。因此，我们可以通过数逻辑值 True 的数量数出 NaN 值的数量。为了数逻辑值 True 的总数，我们使用 .sum() 方法两次。要使用该方法两次，是因为第一个 sum() 返回一个 pandas Series，其中存储了列上的逻辑值 True 的总数，如下所示：

```py
store_items.isnull().sum()
```

bikes            0
glasses        1
pants           0
shirts           1
shoes          0
suits            1
watches      0
dtype: int64

第二个 sum() 将上述 pandas Series 中的 1 相加。

除了数 NaN 值的数量之外，我们还可以采用相反的方式，我们可以数非 NaN 值的数量。为此，我们可以使用 .count() 方法，如下所示：

```py
# We print the number of non-NaN values in our DataFrame
print()
print('Number of non-NaN values in the columns of our DataFrame:\n', store_items.count())
```

Number of non-NaN values in the columns of our DataFrame:
bikes            3
glasses        2
pants           3
shirts           2
shoes          3
suits            2
watches      3
dtype: int64

现在我们已经知道如何判断数据集中是否有任何 NaN 值，下一步是决定如何处理这些 NaN 值。通常，我们有两种选择，可以删除或替换 NaN 值。在下面的示例中，我们将介绍这两种方式。

首先，我们将学习如何从 DataFrame 中删除包含任何 NaN 值的行或列。如果 axis = 0，.dropna(axis) 方法将删除包含 NaN 值的任何行，如果 axis = 1，.dropna(axis) 方法将删除包含 NaN 值的任何列。我们来看一些示例：

```py
# We drop any rows with NaN values
store_items.dropna(axis = 0)
bikes	glasses	pants	shirts	shoes	suits	watches
store 2	15	50.0	5	2.0	5	7.0	10
# We drop any columns with NaN values
store_items.dropna(axis = 1)
```

bikes	pants	shoes	watches
store 1	20	30	8	35
store 2	15	5	5	10
store 3	20	30	10	35

注意，.dropna() 方法不在原地地删除具有 NaN 值的行或列。也就是说，原始 DataFrame 不会改变。你始终可以在 dropna() 方法中将关键字 inplace 设为 True，在原地删除目标行或列。

现在，我们不再删除 NaN 值，而是将它们替换为合适的值。例如，我们可以选择将所有 NaN 值替换为 0。为此，我们可以使用 .fillna() 方法，如下所示。

```py
# We replace all NaN values with 0
store_items.fillna(0)
```

bikes	glasses	pants	shirts	shoes	suits	watches
store 1	20	0.0	30	15.0	8	45.0	35
store 2	15	50.0	5	2.0	5	7.0	10
store 3	20	4.0	30	0.0	10	0.0	35

我们还可以使用 .fillna() 方法将 NaN 值替换为 DataFrame 中的上个值，称之为前向填充。在通过前向填充替换 NaN 值时，我们可以使用列或行中的上个值。.fillna(method = 'ffill', axis) 将通过前向填充 (ffill) 方法沿着给定 axis 使用上个已知值替换 NaN 值。我们来看一些示例：

```py
# We replace NaN values with the previous value in the column
store_items.fillna(method = 'ffill', axis = 0)
```

bikes	glasses	pants	shirts	shoes	suits	watches
store 1	20	NaN	30	15.0	8	45.0	35
store 2	15	50.0	5	2.0	5	7.0	10
store 3	20	4.0	30	2.0	10	7.0	35

注意 store 3 中的两个 NaN 值被替换成了它们所在列中的上个值。但是注意， store 1 中的 NaN 值没有被替换掉。因为这列前面没有值，因为 NaN 值是该列的第一个值。但是，如果使用上个行值进行前向填充，则不会发生这种情况。我们来看看具体情形：

```py
# We replace NaN values with the previous value in the row
store_items.fillna(method = 'ffill', axis = 1)
```

bikes	glasses	pants	shirts	shoes	suits	watches
store 1	20.0	20.0	30.0	15.0	8.0	45.0	35.0
store 2	15.0	50.0	5.0	2.0	5.0	7.0	10.0
store 3	20.0	4.0	30.0	30.0	10.0	10.0	35.0

我们看到，在这种情形下，所有 NaN 值都被替换成了之前的行值。

同样，你可以选择用 DataFrame 中之后的值替换 NaN 值，称之为后向填充。.fillna(method = 'backfill', axis) 将通过后向填充 (backfill) 方法沿着给定 axis 使用下个已知值替换 NaN 值。和前向填充一样，我们可以选择使用行值或列值。我们来看一些示例：

```py
# We replace NaN values with the next value in the column
store_items.fillna(method = 'backfill', axis = 0)
```

bikes	glasses	pants	shirts	shoes	suits	watches
store 1	20	50.0	30	15.0	8	45.0	35
store 2	15	50.0	5	2.0	5	7.0	10
store 3	20	4.0	30	NaN	10	NaN	35

注意，store 1 中的 NaN 值被替换成了它所在列的下个值。但是注意，store 3 中的两个 NaN 值没有被替换掉。因为这些列中没有下个值，这些 NaN 值是这些列中的最后一个值。但是，如果使用下个行值进行后向填充，则不会发生这种情况。我们来看看具体情形：

```py
# We replace NaN values with the next value in the row
store_items.fillna(method = 'backfill', axis = 1)
```

bikes	glasses	pants	shirts	shoes	suits	watches
store 1	20.0	30.0	30.0	15.0	8.0	45.0	35.0
store 2	15.0	50.0	5.0	2.0	5.0	7.0	10.0
store 3	20.0	4.0	30.0	10.0	10.0	35.0	35.0

注意，.fillna() 方法不在原地地替换（填充）NaN 值。也就是说，原始 DataFrame 不会改变。你始终可以在 fillna() 函数中将关键字 inplace 设为 True，在原地替换 NaN 值。

我们还可以选择使用不同的插值方法替换 NaN 值。例如，.interpolate(method = 'linear', axis) 方法将通过 linear 插值使用沿着给定 axis 的值替换 NaN 值。我们来看一些示例：

```py
# We replace NaN values by using linear interpolation using column values
store_items.interpolate(method = 'linear', axis = 0)
```

bikes	glasses	pants	shirts	shoes	suits	watches
store 1	20	NaN	30	15.0	8	45.0	35
store 2	15	50.0	5	2.0	5	7.0	10
store 3	20	4.0	30	2.0	10	7.0	35

注意，store 3 中的两个 NaN 值被替换成了线性插值。但是注意，store 1 中的 NaN 值没有被替换掉。因为该 NaN 值是该列中的第一个值，因为它前面没有数据，因此插值函数无法计算值。现在，我们使用行值插入值：

```py
# We replace NaN values by using linear interpolation using row values
store_items.interpolate(method = 'linear', axis = 1)
```

bikes	glasses	pants	shirts	shoes	suits	watches
store 1	20.0	25.0	30.0	15.0	8.0	45.0	35.0
store 2	15.0	50.0	5.0	2.0	5.0	7.0	10.0
store 3	20.0	4.0	30.0	20.0	10.0	22.5	35.0

和我们看到的其他方法一样，`.interpolate()` 方法不在原地地替换 NaN 值。

## 将数据加载到 DataFrame 中

在机器学习中，你很有可能会使用来自很多来源的数据库训练学习算法。pandas 使我们能够将不同格式的数据库加载到 DataFrame 中。用于存储数据库的最热门数据格式是 csv。

CSV 是指逗号分隔值，是一种简单的数据存储格式。我们可以使用 `pd.read_csv()` 函数将 CSV 文件加载到 pandas DataFrame 中。我们将 Google 股票数据加载到一个 pandas DataFrame 中。`GOOG.csv` 文件包含从雅虎金融那获取的 2004 年 8 月 19 日至 2017 年 10 月 13 日 Google 股票数据。

```py
# 我们将 Google 股票数据加载到 DataFrame 中
Google_stock = pd.read_csv('./GOOG.csv')

# 我们输出关于 Google_stock 的一些信息
print('Google_stock is of type:', type(Google_stock))
print('Google_stock has shape:', Google_stock.shape)
```

```
Google_stock is of type: class 'pandas.core.frame.DataFrame'
Google_stock has shape: (3313, 7)
```

可以看出，我们将 GOOG.csv 文件加载到了 pandas DataFrame 中，其中包含 3,313 行和 7 列数据。现在我们来看看股票数据

Google_stock
Date	Open	High	Low	Close	Adj Close	Volume
0	2004-08-19	49.676899	51.693783	47.669952	49.845802	49.845802	44994500
1	2004-08-20	50.178635	54.187561	49.925285	53.805050	53.805050	23005800
2	2004-08-23	55.017166	56.373344	54.172661	54.346527	54.346527	18393200
... ...
3311	2017-10-12	987.450012	994.119995	985.000000	987.830017	987.830017	1262400
3312	2017-10-13	992.000000	997.210022	989.000000	989.679993	989.679993	1157700
3313 rows × 7 columns

可以看出，这是一个非常庞大的数据集，pandas 自动为该 DataFrame 分配了数字行索引。pandas 还使用出现在 CSV 文件中的标签为列分配标签。

在处理这样的大型数据集时，通常有必要直接查看前几行数据，而不是整个数据集。我们可以使用 .head() 方法查看前 5 行数据，如下所示

```py
Google_stock.head()
```

Date	Open	High	Low	Close	Adj Close	Volume
0	2004-08-19	49.676899	51.693783	47.669952	49.845802	49.845802	44994500
1	2004-08-20	50.178635	54.187561	49.925285	53.805050	53.805050	23005800
2	2004-08-23	55.017166	56.373344	54.172661	54.346527	54.346527	18393200
3	2004-08-24	55.260582	55.439419	51.450363	52.096165	52.096165	15361800
4	2004-08-25	52.140873	53.651051	51.604362	52.657513	52.657513	9257400

我们还可以使用 .tail() 方法查看最后 5 行数据：

```py
Google_stock.tail()
```

Date	Open	High	Low	Close	Adj Close	Volume
3308	2017-10-09	980.000000	985.424988	976.109985	977.000000	977.000000	891400
3309	2017-10-10	980.000000	981.570007	966.080017	972.599976	972.599976	968400
3310	2017-10-11	973.719971	990.710022	972.250000	989.250000	989.250000	1693300
3311	2017-10-12	987.450012	994.119995	985.000000	987.830017	987.830017	1262400
3312	2017-10-13	992.000000	997.210022	989.000000	989.679993	989.679993	1157700

我们还可以选择使用 .head(N) 或 .tail(N) 分别显示前 N 行和后 N 行数据。

我们快速检查下数据集中是否有任何 NaN 值。为此，我们将使用 .isnull() 方法，然后是 .any() 方法，检查是否有任何列包含 NaN 值。

```py
Google_stock.isnull().any()
```

Date                  False
Open                False
High                  False
Low                   False
Close                 False
Adj Close          False
Volume             False
dtype: bool

可以看出没有任何 NaN 值。

在处理大型数据集时，通常有必要获取关于数据集的统计信息。通过使用 pandas 的 .describe() 方法，可以获取关于 DataFrame 每列的描述性统计信息。我们来看看代码编写方式：

```py
# We get descriptive statistics on our stock data
Google_stock.describe()
```

Open	High	Low	Close	Adj Close	Volume
count	3313.000000	3313.000000	3313.000000	3313.000000	3313.000000	3.313000e+03
mean	380.186092	383.493740	376.519309	380.072458	380.072458	8.038476e+06
std	223.818650	224.974534	222.473232	223.853780	223.853780	8.399521e+06
min	49.274517	50.541279	47.669952	49.681866	49.681866	7.900000e+03
25%	226.556473	228.394516	224.003082	226.407440	226.407440	2.584900e+06
50%	293.312286	295.433502	289.929291	293.029114	293.029114	5.281300e+06
75%	536.650024	540.000000	532.409973	536.690002	536.690002	1.065370e+07
max	992.000000	997.210022	989.000000	989.679993	989.679993	8.276810e+07

如果有必要，我们可以对单列应用 .describe() 方法，如下所示：

```py
# We get descriptive statistics on a single column of our DataFrame
Google_stock['Adj Close'].describe()
```

count         3313.000000
mean           380.072458
std                223.853780
min                 49.681866
25%              226.407440
50%              293.029114
75%              536.690002
max              989.679993
Name: Adj Close, dtype: float64

同样，你可以使用 pandas 提供的很多统计学函数查看某个统计信息。我们来看一些示例：

```py
# We print information about our DataFrame  
print()
print('Maximum values of each column:\n', Google_stock.max())
print()
print('Minimum Close value:', Google_stock['Close'].min())
print()
print('Average value of each column:\n', Google_stock.mean())
```

Maximum values of each column:
Date            2017-10-13
Open                        992
High                    997.21
Low                          989
Close                  989.68
Adj Close           989.68
Volume        82768100
dtype: object

Minimum Close value: 49.681866

Average value of each column:
Open            3.801861e+02
High             3.834937e+02
Low              3.765193e+02
Close            3.800725e+02
Adj Close     3.800725e+02
Volume        8.038476e+06
dtype: float64

另一个重要统计学衡量指标是数据相关性。数据相关性可以告诉我们不同列的数据是否有关联。我们可以使用 .corr() 方法获取不同列之间的关联性，如下所示：

```py
# We display the correlation between columns
Google_stock.corr()
```

Open	High	Low	Close	Adj Close	Volume
Open	1.000000	0.999904	0.999845	0.999745	0.999745	-0.564258
High	0.999904	1.000000	0.999834	0.999868	0.999868	-0.562749
Low	0.999845	0.999834	1.000000	0.999899	0.999899	-0.567007
Close	0.999745	0.999868	0.999899	1.000000	1.000000	-0.564967
Adj Close	0.999745	0.999868	0.999899	1.000000	1.000000	-0.564967
Volume	-0.564258	-0.562749	-0.567007	-0.564967	-0.564967	1.000000

关联性值为 1 表明关联性很高，关联性值为 0 告诉我们数据根本不相关。

在这门“pandas 入门”课程的最后，我们将讲解 .groupby() 方法。.groupby() 方法使我们能够以不同的方式对数据分组。我们来看看如何分组数据，以获得不同类型的信息。在下面的示例中，我们将加载关于虚拟公司的虚拟数据。

```py
# We load fake Company data in a DataFrame
data = pd.read_csv('./fake_company.csv')
```

data
Year	Name	Department	Age	Salary
0	1990	Alice	HR	25	50000
1	1990	Bob	RD	30	48000
2	1990	Charlie	Admin	45	55000
3	1991	Alice	HR	26	52000
4	1991	Bob	RD	31	50000
5	1991	Charlie	Admin	46	60000
6	1992	Alice	Admin	27	60000
7	1992	Bob	RD	32	52000
8	1992	Charlie	Admin	28	62000
可以看出，上述数据包含从 1990 年到 1992 年的信息。对于每一年，我们都能看到员工姓名、所在的部门、年龄和年薪。现在，我们使用 .groupby() 方法获取信息。

我们来计算公司每年在员工薪资上花费的数额。为此，我们将使用 .groupby() 方法按年份对数据分组，然后使用 .sum() 方法将所有员工的薪资相加。

```py
# We display the total amount of money spent in salaries each year
data.groupby(['Year'])['Salary'].sum()
```

Year
1990     153000
1991     162000
1992     174000
Name: Salary, dtype: int64

可以看出，该公司在 1990 年的薪资花费总额为 153,000 美元，在 1991 年为 162,000 美元，在 1992 年为 174,000 美元。

现在假设我们想知道每年的平均薪资是多少。为此，我们将使用 .groupby() 方法按年份对数据分组，就像之前一样，然后使用 .mean() 方法获取平均薪资。我们来看看代码编写方式

```py
# We display the average salary per year
data.groupby(['Year'])['Salary'].mean()
```

Year
1990     51000
1991     54000
1992     58000
Name: Salary, dtype: int64

可以看出，1990 年的平均薪资为 51,000 美元，1991 年为 54,000 美元，1992 年为 58,000 美元。

现在我们来看看在这三年的时间内每位员工都收到多少薪资。在这种情况下，我们将使用.groupby()方法按照Name来对数据分组。之后，我们会把每年的薪资加起来。让我们来看看结果。

```py
# We display the total salary each employee received in all the years they worked for the company
data.groupby(['Name'])['Salary'].sum()
```

Name
Alice         162000
Bob          150000
Charlie     177000
Name: Salary, dtype: int64

我们看到，Alice在公司工作的三年时间里共收到了162,000美元的薪资，Bob收到了150,000，Charlie收到了177,000。

现在让我们看看每年每个部门的薪资分配状况。在这种情况下，我们将使用.groupby()方法按照Year和Department对数据分组，之后我们会把每个部门的薪资加起来。让我们来看看结果。

```py
# We display the salary distribution per department per year.
data.groupby(['Year', 'Department'])['Salary'].sum()
```

Year     Department
1990    Admin              55000
             HR                    50000
             RD                    48000
1991    Admin              60000
             HR                    52000
             RD                    50000
1992    Admin            122000
             RD                    52000
Name: Salary, dtype: int64

我们看到，1990年，管理部门支付了55,000美元的薪资，HR部门支付了50,000，研发部门支付了48,000。1992年，管理部门支付了122,000美元的薪资，研发部门支付了52,000。

## 其他参考

- [DataFrame 数据选取，修改，切片](https://blog.csdn.net/yoonhee/article/details/76168253)
- [Dataframe筛选数据](https://jingyan.baidu.com/article/0eb457e508b6d303f0a90572.html)
