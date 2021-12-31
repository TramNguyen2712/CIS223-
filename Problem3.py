m = 2
r = 3
T = 60

v = input("Enter the velocity: ")

tension = float(m) * pow(float(v),2) / float(r)

if tension > T:
    print('Rope break and the Tension is', format(tension,'.2f'), 'newtons')

else:
    print('Rope doesnt break and Tension is', format(tension,'.2f'), 'newston')


