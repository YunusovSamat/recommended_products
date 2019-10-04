#!/bin/bash

hdfs dfs -rm -r products/output

yarn jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-*.jar \
-D mapreduce.job.name="Products Job via Streaming" \
-files `pwd`/map.py,`pwd`/reduce.py \
-input products/input/ \
-output products/output/ \
-mapper `pwd`/map.py \
-combiner `pwd`/reduce.py \
-reducer `pwd`/reduce.py

hdfs dfs -cat products/output/part-00000
