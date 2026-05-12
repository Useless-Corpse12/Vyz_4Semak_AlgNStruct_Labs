import random
import tkinter as tk

class TreeStick:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

class BinarySearchTree:
    def __init__(self):
        self.root=None

    def insert(self,data):
        if self.root is None:
            self.root=TreeStick(data)
        else:
            self._recursive_insert(data,self.root)

    def _recursive_insert(self,data,node):
        if data<node.data:
            if node.left:
                self._recursive_insert(data,node.left)
            else:
                node.left=TreeStick(data)
        elif data>node.data:
            if node.right:
                self._recursive_insert(data,node.right)
            else:
                node.right=TreeStick(data)

    def search(self,data):
        return self._recursive_search(data,self.root)

    def _recursive_search(self,data,node):
        if node is None or node.data == data:
            return node
        if data<node.data:
            return self._recursive_search(data,node.left)
        else:
            return self._recursive_search(data,node.right)

    def order(self,order_of_order=1):
        """1: прямоой, 2: симметричный, 3: обратный"""
        result=[]
        if order_of_order==1:
            self._in(self.root,result)
        elif order_of_order==2:
            self._pre(self.root,result)
        elif order_of_order==3:
            self._post(self.root,result)
        else:
            raise IndexError("Invalid orderType")
        return result

    def _in(self,node, result):
        if node:
            self._in( node.left, result)
            result.append(node.data)
            self._in( node.right, result)

    def _pre(self,node, result):
        if node:
            result.append(node.data)
            self._pre(node.left, result)
            self._pre(node.right, result)

    def _post(self,node, result):
        if node:
            self._post(node.left, result)
            self._post(node.right, result)
            result.append(node.data)

    def delete(self, data):
        self.root = self._recursive_delete(data, self.root)

    def _recursive_delete(self, data, node):
        if node is None:
            return None
        if data < node.data:
            node.left = self._recursive_delete(data, node.left)
        elif data > node.data:
            node.right = self._recursive_delete(data, node.right)
        else:
            # Узел найден
            if node.left is None:
                return node.right
            if node.right is None:
                return node.left
            # Два ребёнка: заменяем на минимальный из правого поддерева
            temp = self._min_value_node(node.right)
            node.data = temp.data
            node.right = self._recursive_delete(temp.data, node.right)
        return node

    def _min_value_node(self, node):
        while node and node.left:
            node = node.left
        return node

    def height(self):
        return self._height_recursive(self.root)

    def _height_recursive(self, node):
        if node is None:
            return 0
        left_height = self._height_recursive(node.left)
        right_height = self._height_recursive(node.right)
        return max(left_height, right_height) + 1

    def min_value(self):
        if self.root is None:
            return None
        node = self._min_value_node(self.root)
        return node.data

    def max_value(self):
        if self.root is None:
            return None
        node = self.root
        while node.right is not None:
            node = node.right
        return node.data



    def level_order(self):
        if not self.root:
            return []
        result = []
        queue = [self.root]
        while queue:
            if all(n is None for n in queue):
                break
            node = queue.pop(0)
            if node is None:
                result.append(None)
                queue.append(None)
                queue.append(None)
            else:
                result.append(node.data)
                queue.append(node.left)
                queue.append(node.right)
        while result and result[-1] is None:
            result.pop()
        return result

    def _recursive_array_stepping(self,inarr, outarr):
        if not inarr:
            return
        mid = len(inarr) // 2
        outarr.append(inarr[mid])
        self._recursive_array_stepping(inarr[:mid], outarr)
        self._recursive_array_stepping(inarr[mid + 1:], outarr)

    def non_effective_tree_balancing(self):
        sorted_arr = self.order()
        balanced_order = []
        self._recursive_array_stepping(sorted_arr, balanced_order)
        out_tree = BinarySearchTree()
        for el in balanced_order:
            out_tree.insert(el)
        del self.root
        self.root=out_tree.root
        return out_tree


########################################################################################################################
########################################################################################################################
########################################################################################################################


class HeapNode:
    def __init__(self, data, left=None, right=None, parent=None):
        self.data=data
        self.left=left
        self.right=right
        self.parent = parent

    def __str__(self):
        return f"[HeapNode: data = {self.data}, left={self.left}, right={self.right}, parent = {type(self.parent)} ]"

class Heap:
    def __init__(self,Min = True):
        self.root=None
        self._Min=Min
        self.last = None

    def _compare(self,a,b):
        return (a < b and self._Min) or (a > b and not self._Min)

    def _height(self, node):
        if node is None:
            return 0
        return min(self._height(node.left), self._height(node.right)) + 1

    def _find_insertion_parent(self, node):
        if node.left is None or node.right is None:
            return node

        if self._height(node.right) < self._height(node.left):
            return self._find_insertion_parent(node.right)
        else:
            return self._find_insertion_parent(node.left)

    def insert(self, data):
        if self.root is None:
            self.root = HeapNode(data)
            return

        # Ищем родителя, начиная с корня
        parent = self._find_insertion_parent(self.root)
        new_node = HeapNode(data, parent=parent)

        if parent.left is None:
            parent.left = new_node
        else:
            parent.right = new_node

        self._siftup(new_node)

    def _swap_with_parent(self, child):
        parent = child.parent
        if parent is None:
            return
        grand = parent.parent
        is_left = (parent.left == child)
        sibling = parent.right if is_left else parent.left
        c_left, c_right = child.left, child.right
        child.parent = grand
        if grand is None:
            self.root = child
        elif grand.left == parent:
            grand.left = child
        else:
            grand.right = child

        if sibling:
            sibling.parent = child
        if is_left:
            child.left = parent
            child.right = sibling
        else:
            child.left = sibling
            child.right = parent

        parent.parent = child
        parent.left = c_left
        parent.right = c_right
        if c_left:
            c_left.parent = parent
        if c_right:
            c_right.parent = parent

    def _siftup(self, node):
        while node.parent is not None:
            if self._compare(node.data, node.parent.data):
                self._swap_with_parent(node)
            else:
                break

    def non_efficient_heapify(self,arr):
        for el in arr:
            self.insert(el)

    def level_order(self):
        if not self.root:
            return []
        result = []
        queue = [self.root]
        while queue:
            if all(n is None for n in queue):
                break
            node = queue.pop(0)
            if node is None:
                result.append(None)
                queue.append(None)
                queue.append(None)
            else:
                result.append(node.data)
                queue.append(node.left)
                queue.append(node.right)
        while result and result[-1] is None:
            result.pop()
        return result

    def _recursive_inorder(self,node,array):
        if node:
            self._recursive_inorder(node.left, array)
            array.append(node.data)
            self._recursive_inorder(node.right, array)

    def _find_last_node(self, node):
        if node is None:
            return None
        if node.left is None and node.right is None:
            return node
        if self._true_height(node.right) == self._true_height(node.left):
            return self._find_last_node(node.right)
        else:
            return self._find_last_node(node.left)

    def _true_height(self, node):
        if node is None:
            return 0
        return max(self._true_height(node.left), self._true_height(node.right)) + 1

    def _detach_node(self, node):
        data = node.data
        if node.parent is None:
            self.root = None
            return data
        if node.parent.left == node:
            node.parent.left = None
        else:
            node.parent.right = None
        node.parent = None
        return data

    def _siftdown(self, node):
        while node:
            target = node
            if node.left and self._compare(node.left.data, target.data):
                target = node.left
            if node.right and self._compare(node.right.data, target.data):
                target = node.right

            if target == node:
                break

            node.data, target.data = target.data, node.data
            node = target

    def delete_root(self):
        if self.root is None:
            return None

        root_data = self.root.data
        if self.root.left is None and self.root.right is None:
            self.root = None
            return root_data

        last = self._find_last_node(self.root)
        last_data = self._detach_node(last)
        self.root.data = last_data
        self._siftdown(self.root)

        return root_data

    def __repr__(self):
        print(self.level_order())



def visualize_tree(level_order_array, w=600, h=400):
    if not level_order_array or level_order_array[0] is None:
        print("Дерево пустое")
        return
    root = tk.Tk()
    root.title("BST Visualizer")
    root.geometry(f"{w}x{h}")
    canvas = tk.Canvas(root, width=w, height=h, bg='#f8f9fa')
    canvas.pack(fill=tk.BOTH, expand=True)
    def get_h(idx):
        if idx >= len(level_order_array) or level_order_array[idx] is None:
            return 0
        return 1 + max(get_h(2 * idx + 1), get_h(2 * idx + 2))
    tree_h = get_h(0)
    y_step = h / (tree_h + 2)
    def draw(idx, x, y, x_gap):
        val = level_order_array[idx]
        if val is None: return
        r = 22
        canvas.create_oval(x - r, y - r, x + r, y + r, fill='#4a90e2', outline='#2c5282', width=2)
        canvas.create_text(x, y, text=str(val), fill='white', font=('Consolas', 11, 'bold'))
        left, right = 2 * idx + 1, 2 * idx + 2
        if left < len(level_order_array) and level_order_array[left] is not None:
            canvas.create_line(x, y + r, x - x_gap, y + y_step - r, fill='#555', width=2, arrow=tk.LAST)
            draw(left, x - x_gap, y + y_step, x_gap / 2)
        if right < len(level_order_array) and level_order_array[right] is not None:
            canvas.create_line(x, y + r, x + x_gap, y + y_step - r, fill='#555', width=2, arrow=tk.LAST)
            draw(right, x + x_gap, y + y_step, x_gap / 2)
    draw(0, w / 2, y_step, w / 4)
    root.mainloop()


def bst():
    tree=BinarySearchTree()
    rnd_arr = [i for i in range(7)]
    for el in rnd_arr:
        tree.insert(el)
    visualize_tree(tree.level_order())
    print(tree.level_order())
    print(tree.order())
    print(tree.height())
    tree.non_effective_tree_balancing()
    visualize_tree(tree.level_order())
    print(tree.level_order())
    print(tree.order())
    print(tree.height())
    tree.delete(3)
    print(tree.level_order())
    print(tree.order())
    print(tree.height())
    visualize_tree(tree.level_order())
    tree.delete(1)
    print(tree.level_order())
    print(tree.order())
    print(tree.height())
    visualize_tree(tree.level_order())

def heap():
    siso = Heap()
    siso.insert(1)
    siso.insert(23)
    siso.insert(12)
    siso.insert(5)
    siso.__repr__()
    visualize_tree(siso.level_order())
    siso.non_efficient_heapify([2,11,32])
    siso.__repr__()
    visualize_tree(siso.level_order())
    siso2=Heap(Min=False)
    siso2.non_efficient_heapify(siso.level_order())
    print(siso2.level_order())
    visualize_tree(siso2.level_order())
    siso2.delete_root()
    print(siso2.level_order())
    visualize_tree(siso2.level_order())
    siso2.delete_root()
    print(siso2.level_order())
    visualize_tree(siso2.level_order())

if __name__ == "__main__":
    bst()
