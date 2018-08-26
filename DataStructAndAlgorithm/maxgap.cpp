#include <iostream>

//给定一个数据，求排序后的数组的相邻元素的最大值
//利用桶排序的思想
int bucketID(int A[], int i, int len, int min, int max)
{
    return ((A[i] - min) * len) / (max - min);
}

int Max(int a, int b)
{
    return a>b?a:b;
}

int Min(int a, int b)
{
    return a>b?b:a;
}

int maxGap(int A[], int len)
{
    if (len <=1) 
    {
        return 0;
    }
    //求最大最小值
    int min = A[0];
    int max = A[0];
    for (int i = 1; i < len; i++)
    {
        min = A[i]<min?A[i]:min;
        max = A[i]>max?A[i]:max;
    }
    std::cout<<"min="<<min<<"max="<<max<<std::endl;
    //分桶，计算桶中的最大、最小值
    int *minArr = new int[len+1]();
    int *maxArr = new int[len+1]();
    bool *hasNum = new bool[len+1]();
    for (int i = 0; i < len; i++)
    {
        int bucket = bucketID(A, i, len, min, max);
        minArr[bucket] = hasNum[bucket]?Min(minArr[bucket], A[i]):A[i]; 
        maxArr[bucket] = hasNum[bucket]?Max(maxArr[bucket], A[i]):A[i]; 
        hasNum[bucket] = true;
        std::cout<<"bucket num="<<bucket<<","<<minArr[bucket]<<","<<maxArr[bucket]<<","<<hasNum[bucket]<<std::endl;
    }
    //遍历桶，计算max gap
    int maxgap = 0;
    for (int i=0; i < len+1; i++)
    {
        while (i<len+1 && hasNum[i])
            i++;
        if (i == len+1)
            return maxgap;
        int lastMax = maxArr[i-1];
        while (i<len+1 && hasNum[i]==false)
            i++;
        if (i == len +1)
            return maxgap;
        int curMin = minArr[i];
        maxgap = Max(maxgap, curMin-lastMax);
    }
    return maxgap;
}

int main()
{
    int A[] = {1, 3, 5, 9, 10};
    std::cout<<"maxgap ="<<maxGap(A, 5)<<std::endl;
    return 0;
}
