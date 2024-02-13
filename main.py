from Tree.Tree import Tree, tree_from_list, find_way


nodes = input('Введите значения вершин через запятую: ').split(',')
root = tree_from_list(nodes)
sum_input = int(input())
answer = find_way(root, sum_input)
if not answer:
    print('Нет подходящего пути')
else:
    print(answer)

