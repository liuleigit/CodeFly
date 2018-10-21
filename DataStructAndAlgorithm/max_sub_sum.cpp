#include <iostream>
#include <vector>
using namespace std;

vector<int> maxSubSum(int A[], int len)
{
    vector<int> max_sub;
    max_sub.push_back(A[0]);
    for (int i = 1; i < len; ++i)
    {
        max_sub.push_back(max(A[i], max_sub[i-1]+A[i]));
    }
    return max_sub;
}

int main()
{
    int A[7] = {-1, 2, 6, -10, 15,3,-80};
    vector<int> max_sub;
    max_sub = maxSubSum(A, 7);
    for (int i = 0; i < 7; i++)
    {
        std::cout<<max_sub[i]<<std::endl;
    }


    return 0;
}
