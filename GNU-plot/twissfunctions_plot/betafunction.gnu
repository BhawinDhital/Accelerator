set terminal pngcairo 
#set terminal postscript color enhanced
#set terminal png size 1024,768
set output 'betafunction.png'
#set xlabel '{/*2 Path length (m)}'
#set ylabel '{/Symbol b} function (m)}'
#set xlabel 'Path length (m)'
set ylabel '{/Symbol b} function (m)'
set key box vertical width 2 height 1 maxcols 1 spacing 2
set style line 1 linecolor rgb '#0060ad' linetype 1 linewidth 2
set style line 2 linecolor rgb '#ff0000' linetype 1 linewidth 2
set style line 3 linecolor rgb '#00ff00' linetype 1 linewidth 2
#set key font ",10"


plot "twiss.txt" u 1:2 with lines linestyle 1 title '{/Symbol b}_x', \
        '' u 1:3 with lines linestyle 2 title '{/Symbol b}_y'
