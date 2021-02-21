set terminal postscript color enhanced
set size ratio 0.3333 0.8,0.8
# set pointsize 0.48
set output 'tmpplot2.ps'
set rmargin 2
set tmargin 1
set key at 850,275 Left font ",10" reverse
# unset key

set xlabel 'z (m)'
set ylabel 'x (m)'
set xtics 200
set ytics 100

#plot [-600:600][-200:200] "./Longitudinal_motion.txt" u 5:3 w lp lw 1 lt 1 pt 1 ps 0.3 lc rgb "red" title "JLEIC electron collider ring", \
#"./jleic_p_ring_v16_sideways.srv" u 5:3 w lp lw 1 lt 1 pt 2 ps 0.3 lc rgb "blue" title "JLEIC ion collider ring"

#plot [-600:600][-200:200] "./jleic_e_ring_v16.1_FODO_v1_rbend_allSolOn.srv" u 5:3 w lp lw 1 lt 1 pt 1 ps 0.3 lc rgb "red" title ""

plot [-500:500][-200:200] "./jleic_e_ring_v16.2_v2.4_detsoloff.srv" u 5:3 w lp lw 1 lt 1 pt 2 ps 0.3 lc rgb "blue" title ""

set xlabel 'z (m)'
set ylabel 'y (m)'
set xtics 200
set ytics 0.4

plot [-500:500][-0.4:1.5] "./jleic_e_ring_v16.2_v2.4_detsoloff.srv" u 5:4 w lp lw 1 lt 1 pt 2 ps 0.3 lc rgb "blue" title ""

exit
