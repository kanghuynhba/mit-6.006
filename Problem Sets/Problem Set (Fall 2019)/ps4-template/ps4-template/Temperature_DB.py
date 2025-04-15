from Binary_Tree_Set import BST_Node, Binary_Tree_Set
# ----------------------------------- #
# DO NOT REMOVE THIS IMPORT STATEMENT # 
# DO NOT MODIFY IMPORTED CODE         #
# ----------------------------------- #


class Temperature_DB_Node(BST_Node):
    def subtree_update(A):
        super().subtree_update()
        A.max_temp=A.item.temp
        A.min_date=A.item.key
        A.max_date=A.item.key
        if A.left: 
            A.max_temp=max(A.max_temp, A.left.max_temp)
            A.min_date=min(A.min_date, A.left.min_date)
            A.max_date=max(A.max_date, A.left.max_date) 
        if A.right:
            A.max_temp=max(A.max_temp, A.right.max_temp)
            A.min_date=min(A.min_date, A.right.min_date)
            A.max_date=max(A.max_date, A.right.max_date)
        # ------------------------------------ #
        # YOUR CODE IMPLEMENTING PART (A) HERE #
        # ------------------------------------ #

    def subtree_max_in_range(A, d1, d2):
        # ------------------------------------ #
        # YOUR CODE IMPLEMENTING PART (C) HERE #
        # ------------------------------------ #
        def dfs(A, d1, d2, max_temp):
            if A is None:
                return max_temp
            if A.max_date<d1 or d2<A.min_date:
                return max_temp
            if d1<=A.item.key and A.item.key<=d2:
                if max_temp is None or max_temp.item.temp<A.item.temp:
                    max_temp=A
            d1=max(d1, A.min_date)
            d2=min(d2, A.max_date)
            max_temp=dfs(A.left, d1, d2, max_temp)
            max_temp=dfs(A.right, d1, d2, max_temp)
            return max_temp
        max_temp=None
        max_temp=dfs(A, d1, d2, max_temp)
        if max_temp is None:
           return None
        return max_temp.item.temp
    

# ----------------------------------- #
# DO NOT MODIFY CODE BELOW HERE       # 
# ----------------------------------- #
class Measurement:
    def __init__(self, temp, date):
        self.key  = date
        self.temp = temp

    def __str__(self): 
        return "%s,%s" % (self.key, self.temp)

class Temperature_DB(Binary_Tree_Set):
    def __init__(self): 
        super().__init__(Temperature_DB_Node)

    def record_temp(self, t, d):
        try:
            m = self.delete(d)
            t = max(t, m.temp)
        except: pass
        self.insert(Measurement(t, d))

    def max_in_range(self, d1, d2):
        return self.root.subtree_max_in_range(d1, d2)
