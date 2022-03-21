def lowestCommonAncestor(root, p, q):
    curr = root

    while curr:
        if p.val > curr.val and q.val > curr.val:
            curr = curr.right
        elif p.val < curr.val and q.val < curr.val:
            curr = curr.left
        else:
            return curr

print(lowestCommonAncestor([6, 2, 8, 0, 4, 7, 9, null, null, 3, 5], 2, 8))

# TreeNode{val: 6, left: TreeNode{val: 2, left: TreeNode{val: 0, left: None, right: None}, right: TreeNode{val: 4, left: TreeNode{val: 3, left: None, right: None}, right: TreeNode{val: 5, left: None, right: None}}}, right: TreeNode{val: 8, left: TreeNode{val: 7, left: None, right: None}, right: TreeNode{val: 9, left: None, right: None}}}
# TreeNode{val: 2, left: TreeNode{val: 0, left: None, right: None}, right: TreeNode{val: 4, left: TreeNode{val: 3, left: None, right: None}, right: TreeNode{val: 5, left: None, right: None}}}
