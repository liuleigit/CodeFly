//
// Created by didi on 2018/8/12.
//

#include "iostream"

//堆排序(本文以最大堆为例)
/*
 * 用数组实现的二叉堆有以下性质：
性质一：索引为i的左孩子的索引是 (2*i+1);
性质二：索引为i的左孩子的索引是 (2*i+2);
性质三：索引为i的父结点的索引是 floor((i-1)/2)
 */

/*******调整函数*******/
// 从最后一个非叶子节点开始，调整每个***********/
//非叶子节点：1、将叶子节点值调整为max(叶节点，左孩子，右孩子）
//         2、如果将左(右）孩子赋给了叶子节点，则需要递归调用，调整左孩子的子树
//只负责将节点的值大于孩子值，不负责左右孩子的大小关系

void adjustNode(int A[], int start, int end)
{
    if (2*start+1>end)
        return;
    if ((2*start+2 <= end) && (A[2*start + 2] > A[2*start + 1]) && (A[2*start+2]>A[start]))
    {
            std::swap(A[2*start+2], A[start]);
            adjustNode(A, 2*start+2, end);
    }
    else if (A[2*start+1]>A[start])
    {
            std::swap(A[2*start+1], A[start]);
            adjustNode(A, 2*start+1, end);
    }

    return;
}

void adjustHeap(int arr[], int len)
{
    for (int i = (len -1 - 1)/2; i >= 0; i--)
    {
        adjustNode(arr, i, len-1);
    }

    return;
}

/***** 排序阶段 *****/
//heap排序后，顶点元素是最大的，将顶点元素与最后一个元素交换后，调整除了
//最后一个元素之外的树结构
void swapMax(int A[], int end)
{
    std::swap(A[0], A[end]);
    adjustHeap(A, end);
}

/***** sort *****/
void heapSort(int A[], int len)
{
    adjustHeap(A, len);
    for (int i = len -1 ; i >= 1; i--)
        swapMax(A, i);
}


int main()
{
    //int A[] = {2,8,3,6,10,5,4};int len = 7;
    int A[] = {2,8,3,6,10,5,4,7,4,11,12,20,100};int len = 13;
    //int A[] = {2,8,3}; int len=3;
    heapSort(A,len);
    for (int i = 0; i < len; i++)
        std::cout<<A[i]<<std::endl;
}

