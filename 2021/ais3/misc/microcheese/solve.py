
def splitmix64(x: int) -> int:
    U64_MASK = 0xFFFFFFFFFFFFFFFF
    x = (x + 0x9E3779B97F4A7C15) & U64_MASK
    x = ((x ^ (x >> 30)) * 0xBF58476D1CE4E5B9) & U64_MASK
    x = ((x ^ (x >> 27)) * 0x94D049BB133111EB) & U64_MASK
    return x ^ (x >> 31)


def rev_xorshift(x, shift):
    delta = shift - 64
    x = x >> delta << delta
    rev = shift
    delta -= shift
    while rev < 64:
        x += ((y << rev >> rev)^(x << (rev - shift) >> rev)) >> delta << delta
        delta -= shift
        rev += shift
    return x

def rev_odd_num(x):
    r = x
    for _ in range(1,5):
        r *= 2-r*x
    return r

def rev_splitmix64(x):
    x = rev_xorshift(x, 31)
    x *= rev_odd_num(0x94D049BB133111EB)
    x = rev_xorshift(x, 27)
    x *= rev_odd_num(0xBF58476D1CE4E5B9)
    x = rev_xorshift(x, 30)
    x -= 0x9E3779B97F4A7C15
    print(x)

def rev_hash(h, block):
    secret = h ^ splitmix64(block)
    print(secret)
    
def rev_f(h, block):
    for i in range(2):
        h, block =  

     b, h
     a1 = a ^ s64(b)
     b1 = b ^ s64(a^s64(b))
     a2 = b1
     h  = a1 ^ s64(b1)
     -----------------------





        secret, block 
     -> block, secret ^ s64(block) 
     -> secret ^ s64(block), block ^ (secret ^ s64(block)) 
     -> block ^ (secret ^ s64(block)), ((secret ^ s64(block)) ^ s64(block ^ (secret ^ s64(block))))
     -> (secret ^ s64(block)) ^ s64(block ^ (secret ^ s64(block))), ((block ^ (secret ^ s64(block))) ^ (s64((secret ^ s64(block)) ^ s64(block ^ (secret ^ s64(block))))))

     => h ^ block = secret ^ s64(block) ^ s64((secret ^ s64(block)) ^ s64(block ^ (secret ^ s64(block))))
     => h1 ^ rev64(block) = secret ^ s64((secret ^ s64(block)) ^ s64(block ^ (secret ^ s64(block))))



