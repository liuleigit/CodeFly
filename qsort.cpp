#include <iostream>
#include <stdio.h>
void qsort(int A[], int l, int r)
{
    if (l >= r)
        return;
    int m = l - 1;
    for(int i = l; i <= r; ++i) //最后A[r]同样会执行交换
    {
        if (A[i] <= A[r])
        {
            //使得m后面一个元素是大于等于A[r]的值
            std::swap(A[++m], A[i]);
        }
    }
    qsort(A, l, m - 1);
    qsort(A, m + 1, r);
}

int main()
{
    int a[5] = {6, 2, 3, 9, 7};
    qsort(a, 0, 5);
    for (int i = 0; i < 5; i++)
        std::cout<<a[i]<<" ";
    std::cout<<std::endl;


    return 0;
}



