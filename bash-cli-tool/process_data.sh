#!/bin/bash
echo "Data Processed by Violet Pang"
DATE=`date +%Y-%m-%d`
echo "Date is: "$DATE
echo ""
echo "The name of the file is:" $1
echo ""
lines=$(wc -l < $1)
echo ""
echo "The file has" $lines "lines"
echo ""
colnames=$(head -n 1 < $1)
echo ""
echo "Column names are: "
echo ""
echo $colnames
echo ""
echo "List of items in the descending order of calories:"
sorted=$(sort -k4 -n -t, $1)
echo $sorted
