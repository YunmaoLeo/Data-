#coding=utf-8
def HeapSort(a):
  N = len(a)
  for k in range(N//2,0,-1): #从数组的中间开始往左遍历 构造堆 ，因为右半边是最下面一层子节点
    sink(a, k ,N)
  while (N > 1):
    exch(a, 1, N)
    N = N -1 
    sink(a, 1, N)

def sink(pq, k, n):
  while(2*k <= n): # N = len(dp)
    j = 2*k
    if (j<n and pq[j-1]<pq[j+1-1]):  # 判断子结点左边的大还是右边的大，如果是右边的大就进行 加一
      j += 1
    if (not pq[k-1]<pq[j-1]): # 如果父结点大于子节点，就break，结束
      break
    exch(pq,k,j) #否则进行交换，让k和j的值交换，然后把指针移动到j上
    k = j

def exch(pq, i, j):
  pq[i-1],pq[j-1]=pq[j-1],pq[i-1]

x = [100,19,12,4,3,2,5,6,3,4,6,7,123,3,4,5]

HeapSort(x)
print(x)