# 题目：长度为n的数组中，总是存在一个断点（下标记为i），数组中断点前面的数字是有序的，断点后的数字也是有序的，
# 且断点后边的数字总是小于前面的数字。如果直接把断点后边的数字移动到数组的前边，那么这个数组将是有序的，
# 具体描述如下所示。求这个数组中的第n/2大的数。


def second_large(arr):
    split = len(arr)
    for i in range(len(arr) - 1):
        if arr[i + 1] < arr[i]:
            split = i

    print('断点：{},{}'.format(split,arr[split]))
    second_of_length = len(arr) //2
    print('second_of_length:',second_of_length)
    if (second_of_length > split):
        s= len(arr) - (second_of_length - split - 1)
    else:
        s= split-second_of_length+1
    print('n/2大所在的坐标：{}'.format(s))
    return arr[s]

if __name__ == '__main__':
    a=[2,3,4,5,1]
    s=second_large(a)
    print(s)
