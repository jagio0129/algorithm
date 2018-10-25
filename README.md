アルゴリズム系の問題を解く

問題サイト
- http://java.sevendays-study.com/problem7.html

## 問題

### ピタゴラス数
a,b,cを、いずれも1以上100以下の整数とするとき、a*a+b*b=c*cを満たす、全てのa,b,cの組み合わせ全てと、その数を求め、画面に表示しなさい。ただし、a,bの数値の組み合わせが同じものも別のものとしてもかまわない。具体的には、a=3,b=4,c=5と、a=4,b=3,c=5は別の組み合わせとする。

`pythagoras1.py`

### ピタゴラス数2
ピタゴラス数の結果から、重複を取り除いた組み合わせと、その数を表示するプログラムを作りなさい。具体的には、a=3,b=4,c=5と、a=4,b=3,c=5は同じものとみなす。

`pythagoras2.py`

### 階乗を求める計算
任意の数値の階乗を求めるプログラムを作りなさい。階乗とは、その数から一つずつ減らした全ての数を書けた数値のことであり、例えば、６の階乗は、６×５×４×３×２×１＝７２０となる。

`factorial.py`

### 桁数を求める計算
1から1000までの任意の数を乱数で発生させ、その数が何桁かを表示するプログラムを作りなさい。

`figure_length.py`

### いまさら世界のナベアツ計算
1から100までの数値のうち、3で割り切れるか、数値の中に3が含まれる数値を全て表示しなさい。

`divisible_or_contain_three.py`

### 分数の計算１
2つの分数同士の足し算をし、その結果を分数で表示するプログラムを作りなさい。このとき、分子、分母共に最大値が10で、最小値は分母が2、分子が１とする。それらの数値をランダムに発生させ、以下のように結果を表示させなさい。ただし、計算結果は、分子と分母がきちんと約分されていることとする。また、分子が分母の数で割り切れる場合は、整数として表示するものとする。

```
例
1/5 + 2/3 = 13/15     ← 通常のケース
2/3 + 3/8= 1.1/24     ← 帯分数になるケース

1/6 + 1/3= 1/2          ← 約分されるケース
1/2 + 1/2 = 1            ← 整数になるケース
```

`fraction1_uselib.py`
`fraction1_fullscratch.py`

### 分数の計算２
分数の計算1のプログラムを発展させ、以下のように改良しなさい。ただし、計算前の二つの数値は、約分されていなくても良いものとする。また、表示方法は例に倣いなさい。
(1)2つの分数の分子、分母共に１から10までの乱数とする。
(2)分子が分母より大きい場合は、帯分数として表す。
(3)分子が分母で割り切れる場合は、整数として表す。

```
例
1.1/3 + 2.1/2 = 3.5/6
2/3 + 3/8= 1.1/24

1 + 1/3= 1.1/3
2/3 + 9/12
```

`fraction2.py`