# -*- coding: utf-8 -*-
# @Time    : 2019/10/28 10:24
# @Author  : Deng Wenxing
# @Email   : dengwenxingae86@163.com
# @File    : spark_test1.py
# @Software: PyCharm
import os, sys
import re
from pyspark.sql import SparkSession
from pyspark.sql.functions import udf
from pyspark.sql.types import IntegerType

spark = SparkSession.builder.getOrCreate()

os.environ['SPARK_HOME'] = "D:\\anacond_spark_env\\spark-2.4.1-bin-hadoop2.7"
sys.path.append("D:\\anacond_spark_env\\spark-2.4.1-bin-hadoop2.7\\python\\py4j-0.10.7-src.zip")
sys.path.append("D:\\anacond_spark_env\\spark-2.4.1-bin-hadoop2.7\\python")

def filnum(data):
    data = str(data)
    if data.isdigit():
        return 1
    else:
        return 0

spark.udf.register('is_num', filnum, IntegerType())


if __name__ == "__main__":

    df_array = []
    years = []
    air_quality_data_folder = "E:\imooc_learn\python_imooc_alg\pyspark_source\data"
    df_union = None
    for file in os.listdir(air_quality_data_folder):
        if '2018' not in file:
            year = re.findall("\d{4}", file)
            years.append(year[0])
            # print file
            file_path = os.path.join(air_quality_data_folder, file)
            df = spark.read.csv(file_path, header="true")
            # df.show()
            if df_union:
                df_union = df_union.unionAll(df)
            else:
                df_union = df
    df_union.show(50)
    df1 = df_union.withColumn('date', df_union['yyyymm'].substr(0, 7))
    df_final = df1.filter(df1['date'].isdigit())
    df_final2 = df_final.withColumn('month',df_final['date'].substr(5,2))
    df_final3 = df_final2.selectExpr('month','PM10')
    df_final4 = df_final3.groupBy(df_final3['month']).agg({'PM10': 'avg'})
    for data in sorted(df_final4.collect(), key=lambda data: data[0]):
        print data[0] + ': ' + ('||' * int(data[1]))