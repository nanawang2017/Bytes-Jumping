'''
要求输入www.toutiao.com.cn输出cn.com.toutiao.www,空间复杂度为O(1)，时间复杂度为最小
'''
s='www.toutiao.com.cn'
print(id(s))
s=s.split('.')
s=s[::-1]
print(s)
s='.'.join(s)
print(s)
print(id(s))

