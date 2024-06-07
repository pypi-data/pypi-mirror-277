from interface_class import Interface
import operators as ops
import numpy as np

interface = Interface()

arr = np.array([i/10 for i in range(10)], dtype=np.float32)

buff1 = interface.array_to_buffer(arr)

ops.tan(buff1)

print(buff1.contents)

