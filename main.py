#Tri Bulles

def bubble_sort(arr):
  """Trie une liste en utilisant l'algorithme du tri à bulles."""
  n = len(arr)
  for i in range(n):
    for j in range(0, n-i-1):
      if arr[j] > arr[j+1]:
        arr[j], arr[j+1] = arr[j+1], arr[j]
  return arr

# Exemple d'utilisation :
numbers = [64, 34, 25, 12, 22, 11, 90]
sorted_numbers = bubble_sort(numbers)
print(sorted_numbers)