def get_first_occurence(arr,idx,key):
    if arr[idx]==key:
        return get_first_occurence(arr,idx-1,key)
    else:
        return idx+1


def bs(arr,low,high,key):
    if high < low:
        if arr[low-1] != key:
            return -1 
        return low
        
    mid = int(low + (high-low)/2)
    if key == arr[mid]:
        return get_first_occurence(arr,mid,key)
    elif key < arr[mid]:
        return bs(arr,low,mid-1,key)
    else:
        return bs(arr,mid+1,high,key)

def binary_search(keys, query):
    # write your code here
    high = len(keys)-1
    low = 0
    return bs(keys,low,high,query)


if __name__ == '__main__':
    num_keys = int(input())
    input_keys = list(map(int, input().split()))
    assert len(input_keys) == num_keys

    num_queries = int(input())
    input_queries = list(map(int, input().split()))
    assert len(input_queries) == num_queries

    for q in input_queries:
        print(binary_search(input_keys, q), end=' ')
