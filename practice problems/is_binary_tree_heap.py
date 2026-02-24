class Solution:
    #Your Function Should return True/False
    def isHeap(self, root):
        # code Here
        temp=root
        def A(root):
            if root==None:
                return 0
            return 1+A(root.left)+A(root.right)
        def B(root,i,cnt):
            if root==None:
                return True
            if i>=cnt:
                return  False
            return (B(root.left,2*i+1,cnt) and B(root.right,2*i+2,cnt))
        def f(root):
            if root==None:
                return True
            if root.left:
                if root.data<root.left.data:
                    return False
                if f(root.left)==False:
                    return False
            if root.right:
                if root.data<root.right.data:
                    return False
                return f(root.right)
            return True
        cnt=A(root)
        root=temp
        if B(root,0,cnt)==False:
            return False
        root=temp
        return f(root)