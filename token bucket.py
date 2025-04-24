def token_bucket(requests, rate, bucket_size):
    tokens = 0
    for i, req in enumerate(requests):
        tokens = min(bucket_size, tokens + rate)
        print(f"\nTime {i+1}: Tokens available: {tokens}")
        if req <= tokens:
            tokens -= req
            print(f"Accepted packet of size {req}")
        else:
            print(f"Packet of size {req} dropped")

token_bucket([1, 2, 5, 1, 3], rate=2, bucket_size=4)

OUTPUT:

Time 1: Tokens available: 2
Accepted packet of size 1

Time 2: Tokens available: 3
Accepted packet of size 2

Time 3: Tokens available: 3
Packet of size 5 dropped

Time 4: Tokens available: 4
Accepted packet of size 1

Time 5: Tokens available: 4
Accepted packet of size 3
