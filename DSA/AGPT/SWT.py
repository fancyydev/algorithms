#En cuentra la suma del tamaño de k entre los subsecuentes de la lista
def max_sum_subarray_of_size_k(k, arr):
    window_sum, max_sum, window_start = 0, 0, 0

    for window_end in range(len(arr)):
        window_sum += arr[window_end]  # Add the next element
        
        if window_end >= k - 1:  # Check if the window size has been reached
            max_sum = max(max_sum, window_sum)
            window_sum -= arr[window_start]  # Slide the window forward
            window_start += 1

    return max_sum

a = [9,4,4,4,6]
print(max_sum_subarray_of_size_k(3, a))