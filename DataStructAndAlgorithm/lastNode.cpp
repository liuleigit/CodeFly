#include <iostream>
//打印完全二叉树的最后一个节点的值
using namespace std;

typedef struct BTNode
{
    int data;
    BTNode* lchild;
    BTNode* rchild;
    BTNode(int d, BTNode* l, BTNode* r){data=d;lchild=l;rchild=r;}
}BTNode;

int getLast(BTNode* root, int totalDepth, int curDepth)
{
    if (root == NULL)
        return 0;
    if (curDepth == totalDepth)
    {
        cout<<root->data<<endl;
        return 1;
    }
    BTNode* orgRoot = root;
    int tmpDepth = curDepth;
    while (root->lchild)
    {
        tmpDepth++;
        root = root->lchild;
    }
    if (tmpDepth != totalDepth)
        return 0;

    root = orgRoot;
    int bGet = 0;
    if(root->rchild)
        bGet = getLast(root->rchild, totalDepth, curDepth+1);
    if (bGet == 1)
        return 1;
    else
        return getLast(root->lchild, totalDepth, curDepth+1);
}


int main()
{
    BTNode* n6 = new BTNode(6, NULL, NULL);
    BTNode* n5 = new BTNode(5, NULL, NULL);
    BTNode* n4 = new BTNode(4, NULL, NULL);
    BTNode* n3 = new BTNode(3, n6, NULL);
    BTNode* n2 = new BTNode(2, n4, n5);
    BTNode* n1 = new BTNode(1, n2, n3);

    BTNode* root = n1;
    int totalDepth = 1;
    while(root->lchild)
    {
        totalDepth++;
        root = root->lchild;
    }
    getLast(n1, totalDepth, 1);
    
    return 0;
}






