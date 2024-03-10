# given a array of elements recursively find all the combination 
# of these elements.
import logging
logger = logging.getLogger('logger')
logger.setLevel(logging.INFO)
hndl = logging.StreamHandler()
hndl.setLevel(logging.INFO)
mstr = logging.Formatter(fmt='%(message)s|%(name)s')
hndl.setFormatter(mstr)
logger.addHandler(hndl)

test = ['a', 'b', 'c', 'd']
# there will 2^n combinations stored in output
output = []


def get_combin(your_list):
    # base case is where len of input list is 0
    if len(your_list) == 0:
        return []
    if len(your_list) == 1:
        return your_list[-1]
    logger.warning(your_list)
    return get_combin(your_list[:-1])


def walk_list(y_list, n):
    """Walk the Complete List"""
    if n >= len(y_list):
        return
    logger.warning(y_list[n])
    walk_list(y_list, n + 1)


def walk_list_traverse(y_list):
    """Walk the Complete List"""
    lis_len = len(y_list)
    for i in range(lis_len):
        logger.info(f"Entering {i}: ")
        walk_list(y_list[i:], 0)


def fibo(num):
    if num < 2:
        return 1
    print(num)
    return fibo(num - 1) + fibo(num - 2)


# get_combin(test)
# walk_list(n=0, y_list=test)
walk_list_traverse(test)
