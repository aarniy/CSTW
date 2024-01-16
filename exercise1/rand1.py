import secrets

def randomData(size):
    with open("randfile1.bin", "wb") as f:
    	token = secrets.token_bytes(size)
    	f.write(token)
    	f.close()
    	print(token)

    return 0

randomData(1048576)
