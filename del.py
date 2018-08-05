# del
def main():
    pass
    inp=input().split()
    num=list(inp[0])
    ind=int(inp[1])
    for i in range(ind+1):
        del num[:i]
    print(''.join(num))
if __name__ == '__main__':
    main()
