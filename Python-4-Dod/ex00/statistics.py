def ft_statistics(*args, **kwargs) -> None:
    """
    Docstring for ft_statistics
    
    :param args: Description
    :type args: Any
    :param kwargs: Description
    :type kwargs: Any
    """
    # print("args: ", args)
    # print("kwargs: ", *kwargs)
    def quick_sort(to_sort):
        if len(to_sort) <= 1:
            return to_sort
        pivot = to_sort[len(to_sort) // 2]  # //2 =>Division entiere (3//2 = 1)
        left = [x for x in to_sort if x < pivot]
        middle = [x for x in to_sort if x == pivot]
        right = [x for x in to_sort if x > pivot]
        return quick_sort(left) + middle + quick_sort(right)

    def f_mean(args):
        mean = 0
        for x in args:
            mean += x
        mean = mean / len(args)
        print("mean :", mean)
        return mean

    def f_median(args):
        median_list = quick_sort(list(args))
        print("median :", f"{median_list[len(median_list) // 2]:.1f}")

    def f_quartile(args):
        quartile_list = quick_sort(list(args))
        quartile_list = [quartile_list[len(quartile_list) // 4], quartile_list[len(quartile_list) // 4 * 3]]
        print("quartile :", [f"{n:.1f}" for n in quartile_list])

    def f_std(args):
        print("std")
        pass

    def f_var(args):
        mean = f_moy(args)
        var_list = list(args)
        var_list = [(x - mean) * (x - mean) for x in args]
        mean = f_moy(args)
        print("var :", mean)
        pass

    func = {'mean': f_mean,
            'median': f_median,
            'quartile': f_quartile,
            'std': f_std,
            'var': f_var}
        # To do check if args only numbers
    for x in kwargs:
        try:
            func[kwargs[x]](args)
        except Exception:
            print("ERROR")

    # except Exception as e:
    #     print("AssertionError: ", e)

