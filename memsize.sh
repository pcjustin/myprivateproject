# Description: Calculus data and bss
# Arthor: Justin Lu
#!/bin/sh
size $1 > output
total_line=`size $1 | wc -l`
echo "line: $total_line"
cal_data=0
cal_bss=0
for i in $(seq 1 $total_line)
do
    data=`sed '1d' output | sed -n "$i p" | awk '{print $2}'`
    cal_data=$((10#${cal_data}+10#${data}))
    bss=`sed '1d' output | sed -n "$i p" | awk '{print $3}'`
    cal_bss=$((10#${cal_bss}+10#${bss}))
done
echo "data: $cal_data bss: $cal_bss"
