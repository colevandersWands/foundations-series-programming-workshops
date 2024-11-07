def recursion_tracer(func):
    """
    Decorates recursive functions with visualization capabilities
    """

    depth = -1
    indent = '. '

    def wrapped(*args, **kwargs):
        nonlocal depth, indent
        if depth < 0:
            print('\n')

        depth += 1

        # Visualize current stack frame
        print(f"{indent * depth}{func.__name__}({', '.join(map(str, args))})")

        result = func(*args, **kwargs)

        # Visualize return
        print(f"{indent * depth}{result} <-")

        depth -= 1
        if depth < 0:
            print('\n')
        
        return result

    return wrapped
