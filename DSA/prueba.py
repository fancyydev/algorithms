a = "00:00:00AM"
print(a[2:])
a = {'key':1, "hey":2}
if 'key' not in a:
    print('o yeah')
    
def lonelyinteger(a):
    result = 0
    for num in a:
        result ^= num  # Aplica XOR a todos los elementos
    return result

print(lonelyinteger([1,2,3,4,5,1,2,3,4,5,6,7]))