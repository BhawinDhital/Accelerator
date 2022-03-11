set terminal pngcairo
set output 'dispersionfunction.png'
#set xlabel '{/*2 Path length (m)}'
#set ylabel '{/Symbol b} function (m)}'
set xlabel 'Path length (m)'
set ylabel 'Dispersion (m)'
set key box vertical width 2 height 1 maxcols 1 spacing 2
set style line 1 linecolor rgb '#0060ad' linetype 1 linewidth 2
set style line 2 linecolor rgb '#ff0000' linetype 1 linewidth 2
set style line 3 linecolor rgb '#00ff00' linetype 1 linewidth 2
#set key font ",10"


plot "twiss.txt" u 1:4 with lines linestyle 1 title 'D_x', \
        '' u 1:5 with lines linestyle 2 title 'D_y'
