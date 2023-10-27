import numpy
import matplotlib.pyplot as plt
def walsh_transform(i,num_bits):
    wht_mat = numpy.zeros((2**num_bits,2**num_bits)) # initializing the Walsh Hadamard Transform matrix
    # Iterating over all possible values of coefficients
    for a1 in range(0,2**num_bits):
        for a2 in range(0,2**num_bits):
            # Iterating over all possible values of input integers 
            for r1 in range(0,2**num_bits):
                for r2 in range(0,2**num_bits):
                    wht_mat[a1][a2] += ((-1)**((((r1+r2)>>i)&1)^(bin(a1&r1).count('1')%2)^(bin(a2&r2).count('1')%2)))
    return wht_mat

num_bits = 6

result=numpy.zeros((num_bits,2**num_bits,2**num_bits))
for i in range(num_bits):
    result[i]=walsh_transform(i,num_bits)
max_walsh_transform = numpy.max(numpy.abs(result),axis=(1,2))
# Code to plot the graph for walsh transform
plt.figure(figsize=(10,6))

x=[m for m in range(num_bits)]

plt.title('Approximating Integer Addition using LFSR')
plt.xlabel('Bit number')
plt.ylabel('Max value of the Walsh Transform')
plt.plot(x,max_walsh_transform)
plt.savefig('./plots/q1_plot.png',dpi=300)
plt.show()
print("The max walsh transform for each bit is:",max_walsh_transform)

index_arr = [numpy.unravel_index(numpy.argmax(numpy.abs(result[i])),result[0].shape) for i in range(num_bits)]

print("The max value of the walsh transform occurs at the followung indices:")
for i in range(num_bits):
    print(bin(index_arr[i]))

