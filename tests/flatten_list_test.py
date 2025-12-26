from typing import List, Any

def flatten_list(nested_list: list) -> list:
    result: List[Any] = []

    def _flatten(lst):
        for item in lst:
            if isinstance(item, list):
                _flatten(item)
            else:
                result.append(item)

    _flatten(nested_list)
    return result


if __name__ == "__main__":
    print(flatten_list([1, 2, 3]))
    print(flatten_list([1, [2, 3], [4, [5]]]))
    print(flatten_list([]))
    print(flatten_list([[[1]]]))
    print(flatten_list([1, [2, [3, [4]]]]))
