# Describe Recursion

recursive definitions

labeling parts

- base case
- turn-around
- recursive case
- break-down
- recursion
- build-up

basic recursion template

```py
def _func_name_(__: __) -> __:
    is_base_case = __ # must use argument(s)
    if is_base_case:
        turn_around = __
        return turn_around
    else:
        break_down = __ # must use argument(s)
        recursion = _func_name_(break_down)
        build_up = __ # must use recursion
        return build_up
```


  ```py
  def reverse_string(to_reverse: str) -> str:
    """
    empty string    ->  empty string
    non-empty str ->  ƒ(string without first char) + first char
    """
    is_base_case = len(to_reverse) == 0 # must use argument(s)
    if is_base_case:
        turn_around = ''
        return turn_around

    break_down = to_reverse[1:] # must use argument(s)
    recursion = reverse_string(break_down)
    build_up = recursion + to_reverse[0] # must use recursion
    return build_up
  ```

  ```py
  def reverse_string(to_reverse: str) -> str:
    """
    empty string    ->  empty string
    non-empty str ->  ƒ(string without first char) + first char
    """
    if len(to_reverse) == 0: # base case
        return '' # turn-around

    # recursion, break-down, build-up
    return reverse_string(to_reverse[1:]) + to_reverse[0]
  ```

- exercises: the same

