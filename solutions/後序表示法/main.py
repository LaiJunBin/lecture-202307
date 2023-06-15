n = int(input())

for _ in range(n):
    inorder = list(map(int, input().split(',')))
    preorder = list(map(int, input().split(',')))

    postorder = []
    def get_postorder(inorder, preorder):
        if len(inorder) == 0:
            return []
        
        root = preorder[0]
        root_index = inorder.index(root)
        
        left_postorder = get_postorder(inorder[:root_index], preorder[1:root_index+1])
        right_postorder = get_postorder(inorder[root_index+1:], preorder[root_index+1:])
        return left_postorder + right_postorder + [root]
        

    postorder = get_postorder(inorder, preorder)
    print(','.join(map(str, postorder)))
