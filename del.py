# del
def main():
    pass
    inp=input().split()
    num=list(inp[0])
    ind=int(inp[1])
    rmv=int(ind)
    del num[:rmv]
    print(''.join(num))
if __name__ == '__main__':
    main()

