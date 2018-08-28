#include <iostream>
#include <queue>
using namespace std;
// 非完全二叉树，输入根节点指针及k，输出第k层节点编号。 编号按照从上往下、从左往右递增

typedef struct BTNode{
    float data;
    BTNode *lchild;
    BTNode *rchild;
    BTNode(float d, BTNode* lc, BTNode* rc){data=d;lchild=lc;rchild=rc;}
}BTNode;

typedef struct NodeDepIndex{
    BTNode *node;
    int depth;
    int idx;
    NodeDepIndex(BTNode *n, int d, int i){node=n;depth=d; idx=i;}
}NodeDepIndex;

void getLastLayerIndex(BTNode* root, int k)
{
    if (root == NULL)
        return;
    int curDep = 1;
    int curIdx = 0;
    queue<NodeDepIndex*> q;
    q.push(new NodeDepIndex(root, curDep, curIdx));

    while(!q.empty())
    {
        NodeDepIndex* curNode = q.front();
        curDep = curNode->depth;
        if (curDep == k)
        {
            cout<<curNode->idx<<endl;
        }
        else
        {
            BTNode* curN = curNode->node;
            if (curN->lchild != NULL)
                q.push(new NodeDepIndex(curN->lchild, 1+curDep, ++curIdx));
            if (curN->rchild != NULL)
                q.push(new NodeDepIndex(curN->rchild, 1+curDep, ++curIdx));
        }
        q.pop();
    }
}

int main()
{
    BTNode* n7 = new BTNode(0.7, NULL, NULL);
    BTNode* n6 = new BTNode(0.6, NULL, NULL);
    BTNode* n5 = new BTNode(0.5, n6, n7);
    BTNode* n4 = new BTNode(0.4, NULL, NULL);
    BTNode* n3 = new BTNode(0.3, NULL, NULL);
    BTNode* n2 = new BTNode(0.2, n4, n5);
    BTNode* n1 = new BTNode(0.1, n2, n3);

    getLastLayerIndex(n1, 4);
    delete n1;
    delete n2;
    delete n3;
    delete n4;
    delete n5;
    delete n6;
    delete n7;


    return 0;
}
