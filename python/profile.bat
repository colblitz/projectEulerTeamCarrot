python kernprof.py -l %1
python -m line_profiler %1.lprof
del %1.lprof
pause