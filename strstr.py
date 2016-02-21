# -*- coding: utf-8 -*-


def is_win(ls, use_pair=False):
    """
    :param ls:
    :param use_pair: 是否使用过对子。
    :return:
    """
    # 如果牌数小于或者等于两张，两种情况算和牌:
    # 1: 没有牌了
    # 2: 是个对子。
    length = len(ls)
    if length <= 2:
        assert length != 1 # 这种就是相公了。
        return not ls or len(set(ls)) == 1
    pair, straight = False, False
    if not use_pair:
        pair = ((ls[0] == ls[1]) and is_win(ls[2:], True))
    # 这里有个判断, 如果只剩两张牌而又不是对子肯定不算和牌。跳出是防止下面数组越界。
    # 首张牌用以三张, 剩下的牌是否能和牌。
    trips = (ls[0] == ls[1] == ls[2]) and is_win(ls[3:], use_pair)
    digit = get_digit(ls[0])
    # 如果首张牌用以顺子, 那么不能是字并且不能比7大。(最大的顺子只到7,8,9)
    # todo 这里应该有更好的方法。 得到去掉第一个顺子后的列表。
    if digit <= 7 and ls[0][0] != 'D':
        # 顺子的第二张牌
        second = incr_one(ls[0])
        # 顺子的第三张牌
        third = incr_one(second)
        if second in ls and third in ls:
            new_list = del_once(list(ls[1:]), second)
            new_list = del_once(new_list, third)
            # 去掉用以顺子的三张牌后是否能和牌。
            straight = is_win(new_list, use_pair)
    return pair or trips or straight

def get_digit(item):
    """
        item: 麻将牌
        :return 输出点数
    """
    return int(item[1])

def incr_one(item):
    """
        item : 麻将牌
        :return 返回该表示法下下一张牌
    """
    assert get_digit(item) < 9 and item[0] != 'D'
    return item[0] + str(int(item[1]) + 1)

def del_once(ls, item):
    """
    :param ls: 列表
    :param item: 要删除的元素
    :return: 删除后的列表
    """
    assert item in ls
    item_index = ls.index(item)
    return ls[:item_index] + ls[item_index+1:]
