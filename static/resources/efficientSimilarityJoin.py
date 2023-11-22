from pyspark.sql.session import SparkSession
from pyspark import SparkContext, SparkConf
import sys
from operator import add
import math
import time
import sys


start = time.time()

file1_path = sys.argv[1]
file2_path = sys.argv[2]
tau = float(sys.argv[3])
out_path = sys.argv[4]

conf = SparkConf().setAppName("project3")
sc = SparkContext(conf=conf)


def get_prefix(line):
    FileID, Id, element = line
    # p = |x|−⌈t·|x|⌉+1
    headline = element[0:len(line[2])-math.ceil(tau*len(line[2]))+1]
    temp = []
    for h in headline:
        temp.append((h,(FileID, Id, element)))

    return temp


def jaccars_sim(l):
    l_ = list(l[1])
    temp_ = []
    for first_count in range(0, len(l_)):
        fileId1, Id1, items1 = l_[first_count]
        for second_count in range(first_count+1, len(l_)):
            fileId2, Id2, items2 = l_[second_count]
            # fileID不一样才计算
            # Jaccard constraint:只有 t · |x| ≤ |y| 才有可能 J(x, y) ≥ t 
            if fileId1 != fileId2 and tau * len(items1) <= len(items2) and tau * len(items2) <= len(items1):
                intersection = set(items1) & set(items2)
                union = set(items1) | set(items2)
                score = len(intersection) / len(union)
                if score >= tau:
                    temp_.append(((Id1, Id2), round(score, 6)))
    return temp_



file1 = sc.textFile(file1_path)
file2 = sc.textFile(file2_path)
# （fileID，ID，items）
f1 = file1.map(lambda x: x if x[-1] != ' ' else x[:-1]).map(lambda line: line.split(" ")).map(lambda x: (1, int(x[0]), set(map(int,x[1:]))))
f2 = file2.map(lambda x: x if x[-1] != ' ' else x[:-1]).map(lambda line: line.split(" ")).map(lambda x: (2, int(x[0]), set(map(int,x[1:]))))
f1.cache()
f2.cache()
f1f2 = f1.union(f2)
'''Stage 1: Order tokens by frequency'''
# 全局wordcount
f1f2 = f1f2.flatMap(lambda x: x[2]).map(lambda x: (x, 1))
f1f2 = f1f2.reduceByKey(add)
f1f2.cache()
# 将wordcount变为字典，共享变量，让所有分区都能访问
wordcount = f1f2.collectAsMap()
bc_wordcount = sc.broadcast(wordcount)

# 将所有items进行排序，先按照count大小排序，如果一样则按本身大小排序
f1_ = f1.map(lambda x: (x[0], x[1], sorted(x[2], key=lambda x:(bc_wordcount.value[x], x))))
f2_ = f2.map(lambda x: (x[0], x[1], sorted(x[2], key=lambda x:(bc_wordcount.value[x], x))))
# 计算items的prefix长度p，并取前p个tokens,每个token后面跟上原有（fileID，ID，items）
f1_ = f1_.flatMap(get_prefix)
f2_ = f2_.flatMap(get_prefix)
f1f2_ = f1_.union(f2_)
f1f2_.cache()
'''Stage 2: Finding “similar” id pairs (verification)'''
# 进行jaccars similarity计算
group_f1f2_ = f1f2_.groupByKey().flatMap(jaccars_sim)
'''Stage 3: remove duplicates'''
# 去重排序
out = group_f1f2_.distinct().sortByKey()
# 格式化输出
out.map(lambda x: f'({x[0][0]},{x[0][1]})\t{x[1]}').coalesce(1).saveAsTextFile(out_path)
sc.stop

end = time.time()
print('------------------------------------')
print('Use time:', end-start, "s")






