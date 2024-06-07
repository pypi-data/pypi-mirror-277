import metalgpu as mg
import numpy as np

interface = mg.Interface()

arr1 = np.array([1, 2, 3, 4, 5], dtype=np.float32)
buf1 = interface.array_to_buffer(arr1)

mg.sqrt(buf1)
