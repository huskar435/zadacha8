input_data = open("input.txt","r")
data = input_data.read()
data = data.split()
a = int(data[0])
b = int(data[1])
c = int(data[2])
a <= 10 ** 2
b <= 10 ** 2
c <= 10 ** 6
if (a * b == c):
   p = 'YES' 
else:
   p = 'NO'
output_data = open("output.txt","w")
output_data.write(p)
input_data.close()
output_data.close()     