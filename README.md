アルゴリズム系の問題を解く

問題サイト
- http://java.sevendays-study.com/problem7.html

## 問題

### ピタゴラス数([pythagoras1.py](https://github.com/jagio0129/algorithm/blob/master/pythagoras1.py))
a,b,cを、いずれも1以上100以下の整数とするとき、a*a+b*b=c*cを満たす、全てのa,b,cの組み合わせ全てと、その数を求め、画面に表示しなさい。ただし、a,bの数値の組み合わせが同じものも別のものとしてもかまわない。具体的には、a=3,b=4,c=5と、a=4,b=3,c=5は別の組み合わせとする。

### ピタゴラス数2([pythagoras2.py](https://github.com/jagio0129/algorithm/blob/master/pythagoras2.py))
ピタゴラス数の結果から、重複を取り除いた組み合わせと、その数を表示するプログラムを作りなさい。具体的には、a=3,b=4,c=5と、a=4,b=3,c=5は同じものとみなす。


### 階乗を求める計算([factorial.py](https://github.com/jagio0129/algorithm/blob/master/factorial.py))
任意の数値の階乗を求めるプログラムを作りなさい。階乗とは、その数から一つずつ減らした全ての数を書けた数値のことであり、例えば、６の階乗は、６×５×４×３×２×１＝７２０となる。

### 桁数を求める計算([figure_length.py](https://github.com/jagio0129/algorithm/blob/master/figure_length.py))
1から1000までの任意の数を乱数で発生させ、その数が何桁かを表示するプログラムを作りなさい。

### いまさら世界のナベアツ計算([divisible_or_contain_three.py](https://github.com/jagio0129/algorithm/blob/master/divisible_or_contain_three.py))
1から100までの数値のうち、3で割り切れるか、数値の中に3が含まれる数値を全て表示しなさい。


### 分数の計算１([fraction1_uselib.py](https://github.com/jagio0129/algorithm/blob/master/fraction1_uselib.py))([fraction1_fullscratch.py](https://github.com/jagio0129/algorithm/blob/master/fraction1_fullscratch.py))
2つの分数同士の足し算をし、その結果を分数で表示するプログラムを作りなさい。このとき、分子、分母共に最大値が10で、最小値は分母が2、分子が１とする。それらの数値をランダムに発生させ、以下のように結果を表示させなさい。ただし、計算結果は、分子と分母がきちんと約分されていることとする。また、分子が分母の数で割り切れる場合は、整数として表示するものとする。

```
例
1/5 + 2/3 = 13/15     ← 通常のケース
2/3 + 3/8= 1.1/24     ← 帯分数になるケース

1/6 + 1/3= 1/2          ← 約分されるケース
1/2 + 1/2 = 1            ← 整数になるケース
```

### 分数の計算２([fraction2.py](https://github.com/jagio0129/algorithm/blob/master/fraction2.py))
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


### 約数([divisor.py](https://github.com/jagio0129/algorithm/blob/master/divisor.py))
乱数で１から1000の数値を発生させ、その数値の約数を小さい順に全て表示するプログラムを作りなさい。


### 完全数([perfect_number.py](https://github.com/jagio0129/algorithm/blob/master/perfect_number.py))
自分自身以外の約数の総和が自分自身に等しくなる自然数を完全数という。例えば6の約数は1,2,3でその和は6となりますので完全数である。10000以下の整数の中から、全ての完全数を探し出し表示するプログラムを作りなさい。


### 数値の分類([odd_even.py](https://github.com/jagio0129/algorithm/blob/master/odd_even.py))
長さ10の整数型の配列変数に、１から100の整数をランダムに代入し、その値を偶数と奇数に分類して、それぞれの値を入れる配列に再代入し、その値を以下の例のように表示しなさい。

```
例
1  10  22  51  3  17  21  98  100  2
偶数：10  22  98  100  2
奇数：1  51  3  17  21
```

### フィボナッチ数列([fibonacci.py](https://github.com/jagio0129/algorithm/blob/master/fibonacci.py))
1,1から始まり、前の2つの値の和を次の値とする数列のことを、フィボナッチ数列という（以下の例を参照）。このとき、40までのフィボナッチ数列を求めてint型の配列に代入し、表示しなさい。

```
例
1  1  2  3  5  8  13  …
```

### トリボナッチ数列([toribonacci.py](https://github.com/jagio0129/algorithm/blob/master/toribonacci.py))
1,1,2から始まり、前の３つの値の和を次の値とする数列のことを、トリボナッチ数列という（以下の例を参照）。このとき、30までのトリボナッチ数列を求めてint型の配列に代入し、表示しなさい。

```
例
1  1  2  4  7  13  24  …
```

### 集合([set.py](https://github.com/jagio0129/algorithm/blob/master/set.py))
長さ10の整数型の配列変数を２つ用意し、それぞれに、各要素に１から10の整数を代入し、以下のようにそれぞれの配列に共通する値の一覧のみが入った配列と、２つのうちどちらかに入る数値の一覧を小さい準に代入した配列を作りなさい。

```
例
配列1:  4  9  4  3  6  8  7  1  3  10
配列2:  7  3  10  7  5  9  4  9  9  1
共通の数：1  3  4  7  9  10
どちらか入っている数：1  3  4  5  6  7  8  9  10
```

### エラトステネスのふるい([eratosthenes.py](https://github.com/jagio0129/algorithm/blob/master/eratosthenes.py))
エラトステネスのふるいを用いて、100以下の素数を全て求めるプログラムを作ってください。（配列を用いること）“エラトステネスのふるい”とは、数値の一覧表を作り、表の中から、最初の素数である2の倍数（ただし、2を除く）を全て消去し、その次に、残った数値の中から最小の数（この場合は3）の倍数を表から全て削除していく、ということを繰り返していく方法です。表の中の一番大きな数での処理が終わった段階で残った数値が、素数になります。

この場合、１は最初から除外します。

ステップ１：１はさいしょから除外。まずは、１より大きい最初の素数である、２を残す。
2  3  4  4  5  6  …  100

ステップ２：２の倍数を全て消去
3  5  7  9  5  6  …  99

ステップ３：残った数のうち最小の数である３を残し、３の倍数を全て消去
5  7  11  13  17  6  …  97

・・・同様の処理を、100以下の全ての数に繰り返す。

`eratosthenes.py`

### 素因数分解[(factoring.py)](https://github.com/jagio0129/algorithm/blob/master/factoring.py)
2から100の乱数を発生させ、その数を素因数分解するプログラムを作成しなさい。素因数分解とは、 数値を、素数の積で表すことであり、例えば、72 = 2 × 2 × 2 × 3 × 3といったように表現することである。