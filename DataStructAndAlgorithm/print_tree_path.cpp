#include <iostream>
#include <vector>
using namespace std;

typedef struct BTNode
{
    int d;
    BTNode* left;
    BTNode* right;
    BTNode(int v, BTNode* l, BTNode* r)
    {
        d = v;
        left = l;
        right=r;
    }
}BTNode;

void printPath(vector<int> p)
{
    for(int i = 0; i < p.size(); i ++)
        cout<<p[i]<<" ";
    cout<<endl;
}

void getPath(BTNode* root, vector<int> p)
{
    if (root)
        p.push_back(root->d);
    if (root->left == NULL && root->right == NULL)
        printPath(p);
    if (root->left)
        getPath(root->left, p);
    if (root->right)
        getPath(root->right, p);
}


int main()
{
    vector<int> p;

    BTNode* n3 = new BTNode(3, NULL, NULL);
    BTNode* n4 = new BTNode(4, NULL, NULL);
    BTNode* n6 = new BTNode(6, NULL, NULL);
    BTNode* n7 = new BTNode(7, NULL, NULL);
    BTNode* n9 = new BTNode(9, NULL, NULL);
    BTNode* n10 = new BTNode(10, NULL, NULL);
    BTNode* n2 = new BTNode(2, n3, n4);
    BTNode* n5 = new BTNode(5, n6, n7);
    BTNode* n1 = new BTNode(1, n2, n5);
    BTNode* n8 = new BTNode(8, n9, n10);
    BTNode* n0 = new BTNode(0, n1, n8);
    getPath(n0, p);

    return 0;
}






