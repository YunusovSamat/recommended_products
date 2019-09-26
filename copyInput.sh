#!/bin/bash

hdfs dfs -rm -r products

hdfs dfs -mkdir products
hdfs dfs -mkdir products/input

hdfs dfs -put orders01 products/input/
hdfs dfs -put orders02 products/input/

