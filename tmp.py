t_toatl = 3000 # µs
rise_time = 75 # µs

t_shousha = t_toatl
for i in range(10):
    t_shousha -= rise_time * 2

if t_shousha > 0:
    print(t_shousha)
    print("OK")
else:
    print(t_shousha)
    print("NG")