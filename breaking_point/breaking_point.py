import timeit


def find_breaking_point(f1, f2, input_generator, start=1, step=1,
                        limit=1000000, trial_count=1000, repeat_count=3):
    """
    Find size of input arguments (n0) for which f2(n0) is faster than f1(n0).
    -  f1, f2 - functions to test.
    -  input_generator - function that receives current size of input arguments and returns input data in form of tuple with first item - list of non-keyword arguments and second item - dict of keyword arguments.
    -  start - initial input data size.
    -  step - iteration step.
    -  limit - maximum size of input data.
    -  trial_count - count of executions of f1/f2 on each iteration.
    -  repeat_count - to repeat trials several times and use average performance value.

    returns n0 - size of input data for which f2(n0) is faster than f1(n0)
            or None if reaches limit.
    """
    for n in xrange(start, limit+1):
        curr_input = input_generator(n)
        # Test first function
        f1_results = timeit.repeat(lambda: f1(*curr_input[0], **curr_input[1]),
                                   repeat=repeat_count, number=trial_count)
        f1_avg = sum(f1_results) / len(f1_results)
        # Test second function
        f2_results = timeit.repeat(lambda: f2(*curr_input[0], **curr_input[1]), repeat=repeat_count, number=trial_count)
        f2_avg = sum(f2_results) / len(f2_results)
        # Compare performance
        if f2_avg < f1_avg:
            return n
    return None

