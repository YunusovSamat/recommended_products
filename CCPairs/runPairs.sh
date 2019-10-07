#!/bin/bash

hdfs dfs -rm -r products/output

yarn jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-*.jar \
-D mapreduce.job.name="Products CCPairs Job via Streaming" \
-files `pwd`/map.py,`pwd`/reduce.py \
-input products/input/ \
-output products/outputCCPairs/ \
-mapper `pwd`/map.py \
-combiner `pwd`/reduce.py \
-reducer `pwd`/reduce.py

hdfs dfs -cat products/outputCCPairs/part-00000
