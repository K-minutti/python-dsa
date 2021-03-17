def find_shortest_path(x_crd, y_crd, map):
  width = len(map[0])
  height = len(map)
  board = [[None for i in range(width)] for i in range(height)]
  board[x_crd][y_crd] = 1
  queue = [(x_crd, y_crd)]

  while queue:
    x, y = queue.pop(0)
    for i in [[1,0], [-1,0], [0,-1], [0,1]]:
      next_x, next_y = x + i[0], y +i[1]
      if 0 <= next_x < height and 0 <= next_y < width:
        if board[next_x][next_y] is None:
          board[next_x][next_y] = board[x][y] + 1
          if map[next_x][next_y] == 1:
            continue
          queue.append((next_x, next_y))
  return board


def solution(map):
  width = len(map[0])
  height = len(map)
  top_down = find_shortest_path(0,0, map)
  bottom_up = find_shortest_path(height - 1, width -1, map)

  min_total = (20*20)+1

  for i in range(height):
    for j in range(width):
      if top_down[i][j] and bottom_up[i][j]:
        min_total = min(top_down[i][j] + bottom_up[i][j] -1, min_total) 
  return min_total

maze_two = [[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]]

print(solution(maze_two)) #out 11