二叉树的最大深度
=========================


    3
   / \
  4   20
     /  \
    15   7
         
```shell
  
maxDepth(3-root) 
=
max( maxDepth(4-sub), maxDepth(20-sub) ) + 1
=
max( 1, max( maxDepth(15-sub), maxDepth(7-sub) ) ) + 1） + 1
=
max( 1, max( 1, 1) + 1) + 1
=
max( 1, 2) + 1
=
2 + 1
=
3
  
``` 
