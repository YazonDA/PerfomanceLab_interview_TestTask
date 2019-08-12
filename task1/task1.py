import sys
import numpy

file_path = sys.argv[1]
w_arr = numpy.fromfile(file_path, sep='\n')

print(f'{numpy.percentile(w_arr, q = 90):.2f}')
print(f'{numpy.median(w_arr):.2f}')
print(f'{numpy.amax(w_arr):.2f}')
print(f'{numpy.amin(w_arr):.2f}')
print(f'{numpy.mean(w_arr):.2f}')
