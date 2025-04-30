from typing import List

# even_list 함수
def even_list(int_list: List[int]) -> List[int]:
    """
    Determines if a number is even and returns an even list.
    """
    # TODO: Implement even_list
    pass

# sum_of_squares_of_even 함수
def sum_of_squares_of_even(even_int_list: List[int]) -> int:
    """
    Computes the sum of the squares of even numbers in the list.
    """
    # TODO: Implement sum_of_squares_of_even 
    pass

# 메인 함수
def main():
    int_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    even_int_list = even_list(int_list)
    output = sum_of_squares_of_even(even_int_list)
    print(output)

if __name__ == "__main__":
    main()