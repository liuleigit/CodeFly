#include<iostream>
#include<stack>
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

void pre_order_recursive(BTNode* root)
{
    if (root != NULL)
    {
        cout<<root->d<<endl;
        pre_order_recursive(root->left);
        pre_order_recursive(root->right);
    }
}

// 非递归遍历
void pre_order_no_recursive(BTNode* root)
{
   stack<BTNode*> s;
   BTNode* p = root;
   while(p != NULL || !s.empty())
   {
       while(p)
       {
           cout<<p->d<<endl;
           s.push(p);  // 核心：根节点入栈
           p = p->left;
       }
       if (!s.empty())
       {
           BTNode* tmp = s.top();
           s.pop();
           p = tmp->right;
       }
   }
}

int main()
{
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

    pre_order_recursive(n0);
    cout<<"--------"<<endl;
    pre_order_no_recursive(n0);
    delete n0;
    delete n1;
    delete n2;
    delete n3;
    delete n4;
    delete n5;
    delete n6;
    delete n7;
    delete n8;
    delete n9;
    delete n10;


}

