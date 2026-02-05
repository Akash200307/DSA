# Last updated: 2/5/2026, 2:47:54 PM
1class Solution:
2    def merge(self,arr,low,mid,high):
3        i=low
4        j=mid+1
5        temp=[]
6        while i<=mid and j<=high:
7            if arr[i]<arr[j]:
8                temp.append(arr[i])
9                i+=1
10            else:
11                temp.append(arr[j])
12                j+=1
13        while i<=mid:
14            temp.append(arr[i])
15            i+=1
16        while j<=high:
17            temp.append(arr[j])
18            j+=1
19        
20        for i in range(low,high+1):
21            arr[i]=temp[i-low]
22        
23
24
25
26    def mergeSort(self,arr,low,high):
27
28        if low>=high:
29            return 
30        mid=(low+high)//2
31
32        self.mergeSort(arr,low,mid)
33        self.mergeSort(arr,mid+1,high)
34        self.merge(arr,low,mid,high)
35
36    def sortArray(self, nums: List[int]) -> List[int]:
37        
38        low=0
39        high=len(nums)-1
40
41        self.mergeSort(nums,low,high)
42
43        return nums
44
45