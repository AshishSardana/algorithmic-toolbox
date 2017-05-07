# Uses python3
import sys

def optimal_weight(W, weights):
    # write your code here
    result = 0
    value = []
    for i in range(0, W + 1):
      value.append(list((0 for j in range((len(weights) + 1)))))

    for i in range(1, (len(weights) + 1)):
      for weight in range(1, (W + 1)):
        value[weight][i] = value[weight][i - 1]
        if weight >= weights[i - 1]:
          item_weight = weights[i - 1]
          item_value = weights[i - 1]
          val = value[weight - item_weight][i - 1] + item_value
          if value[weight][i] < val:
            value[weight][i] = val

    result = value[W][len(weights)]
    return result

def print_value(value):
  for row in value:
    print(row)

if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    # W, n = 12, 3
    # W, n = 20, 4
    # w = [5, 7, 12, 18]
    print(optimal_weight(W, w))