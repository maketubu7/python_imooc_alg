# -*- coding: utf-8 -*-
# @Time    : 2019/10/28 10:24
# @Author  : Deng Wenxing
# @Email   : dengwenxingae86@163.com
# @File    : test.py
# @Software: PyCharm
import os
import re
import sys
from pyspark.sql import SparkSession


os.environ['SPARK_HOME'] = 'D:\\anacond_spark_env\\spark-2.4.1-bin-hadoop2.7'
sys.path.append('D:\\anacond_spark_env\\spark-2.4.1-bin-hadoop2.7\\python')

if __name__ == "__main__":

    print '21'.isdigit()