#!/bin/bash

hdfs dfs -rm -r products/outputCCStripes

yarn jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-*.jar \
-D mapreduce.job.name="Products CCPStripes Job via Streaming" \
-files `pwd`/map.py,`pwd`/reduce.py \
-input products/input/ \
-output products/outputCCStripes/ \
-mapper `pwd`/map.py \
-reducer `pwd`/reduce.py

hdfs dfs -cat products/outputCCStripes/part-00000
