python kernprof.py -l $1.py
python -m line_profiler $1.py.lprof
rm $1.py.lprof

# echo $1.py

# python kernprof.py -l 0001.py
# 233168
# Wrote profile results to 0001.py.lprof
# colblitz@BlitzVM1:~/Private/projecteuler/python$ ls
# 0001.py  0001.py.lprof  kernprof.py
# colblitz@BlitzVM1:~/Private/projecteuler/python$ python -m line_profiler 0001.py.lprof
