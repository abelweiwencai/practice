# https://www.runoob.com/linux/linux-shell-variable.html

# 单引号字符串的限制：
### 单引号里的任何字符都会原样输出，单引号字符串中的变量是无效的；
### 单引号字串中不能出现单独一个的单引号（对单引号使用转义符后也不行），但可成对出现，作为字符串拼接使用。


# 双引号的优点：
### 双引号里可以有变量
### 双引号里可以出现转义字符



# 反引号括起来的字符串被shell解释为命令行，在执行时，shell首先执行该命令行，
# 并以它的标准输出结果取代整个反引号（包括两个反引号）部分
# 反引号还可以嵌套使用。但需注意，嵌套使用时内层的反引号必须用反斜杠（\）将其转义
# ``反引号是老的用法，$()是新的用法  backquote  backtick

# sh -x test.sh 加上-x相当于 debug

# 字符串
s="you are hot"
# get the length of string
s_len=${#s}
echo $s_len

# substract string
sub_str=${s:1:4}
echo $sub_str

# find sub string
# echo `expr index "$s" io`

# 数组
l_list=(1 2 3 4)
echo $l_list
echo ${l_list[2]}
echo ${l_list[@]}  # 用@获取所有元素
# shell 括号 https://www.jb51.net/article/123081.htm

# 流程控制

a=20
b=20

if [ $a == $b ]
then
    echo "a 等于 b"
elif [ $a -gt $b ]
then 
    echo "a 大于 b"
elif [ $a -lt $b ]
then
    echo "a 小与 b"
else
    echo "没有匹配的状态"
fi

echo 'for for for for for for for '

for loop in 1 2 3 4 5 'a' 'b' c 'i am a long str'
do 
    echo "the value is: $loop"
done