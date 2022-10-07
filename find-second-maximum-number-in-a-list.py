
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    converted_arr=list(arr)

    eliminateDuplicate=set(converted_arr)
    MAX=max(eliminateDuplicate)
    
    eliminateDuplicate.remove(MAX)
    MAX=max(eliminateDuplicate)
    print(MAX)

