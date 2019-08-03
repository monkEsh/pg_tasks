import re


class Task1:
    """
    You are given a string S which consists of digits from 0 to 9 and two integer R and A.
    There are two operations which you can do on a string.
    1. Rotate
    2. Add
    You can use Rotate operation to rotate a string clockwise by R positions. For example if
    R=1 , string &quot;581&quot; will become &quot;158&quot; .
    Also you can use Add operation to add number A to all odd indexes of string ( 0 based
    indexing). For example if A=3 , then string &quot;781&quot; will become &quot;711&quot;. Digits post 9 are
    cycled back to zero.
    You can use any of the two operation any number of times in any order to return the
    lexicographical smallest string.
    """
    rotations = None
    addition = None
    num_arr = []

    def __init__(self,
                 rotation,
                 addition,
                 num_arr=[]):
        """

        :param rotation:
        :param addition:
        :param num_arr:
        """
        self.rotation = rotation
        self.addition = addition
        self.num_arr = num_arr

    def rotate(self):
        """

        :return:
        """
        new_list = self.num_arr[:self.rotation]
        old_list = self.num_arr[self.rotation:]
        self.num_arr = old_list + new_list
        return self.num_arr

    def add_at_odd(self):
        """

        :return:
        """
        new_list = self.num_arr[::-1]
        temp_list = [0] * len(new_list)

        for idx, val in enumerate(new_list):
            if idx % 2 != 0:
                new_val = val + self.addition
                temp_list[idx] = new_val % 10
            else:
                temp_list[idx] = val
        return temp_list[::-1]


class Tasks3:
    """
    Given a string S, count minimum no. of swaps needed to regroup 0&#39;s and 1&#39;s.
    After all swaps final string will look like all 0&#39;s followed by all 1&#39;s or all 1&#39;s
    followed by all 0&#39;s.
    Swap operation swaps two adjacent characters (01 -&gt; 10, 10 -&gt; 01, 00 -&gt; 00
    and 11 -&gt; 11).
    """
    num_array = None
    count_0_1 = None
    count_1_0 = None

    def __init__(self,
                 num_array):
        self.num_array = num_array
        self.len_array = len(self.num_array)
        self.count_0_1 = self.find_min_swap(left=0,
                                            right=1)
        self.count_1_0 = self.find_min_swap(left=1,
                                            right=0)

    def find_min_swap(self,
                      left,
                      right):
        """

        :param left:
        :param right:
        :return:
        """
        no_of_iterations = [left] * self.len_array
        count = 0

        no_of_iterations[self.len_array - 1] = 1 - self.num_array[self.len_array - 1]
        for i in range(self.len_array - 2, -1, -1):
            no_of_iterations[i] = no_of_iterations[i + 1]
            if self.num_array[i] == left:
                no_of_iterations[i] = no_of_iterations[i] + 1

        for i in range(0, self.len_array):
            if self.num_array[i] == right:
                count = count + no_of_iterations[i]

        return count


class Tasks4:
    """
    Given n pairs of parentheses, write a function to generate all combinations of well-
    formed parentheses of length 2*n.
    For example, given n = 3, a solution set is:
    "((()))", "(()())", "(())()", "()(())", "()()()"
    """
    out = []

    def parenthesis(self,
                    in_str,
                    n):
        """

        :param in_str:
        :param n:
        :return:
        """
        if n > 0:
            self._print_parenthesis(is_str=in_str,
                                    pos=0,
                                    n=n,
                                    open_b=0,
                                    close_b=0)

    def _print_parenthesis(self,
                           is_str,
                           pos,
                           n,
                           open_b,
                           close_b):
        """

        :param is_str:
        :param pos:
        :param n:
        :param open_b:
        :param close_b:
        :return:
        """
        if close_b == n:
            out_str = ""
            for i in is_str:
                out_str = out_str + i
            self.out.append(out_str)
        else:
            if open_b > close_b:
                is_str[pos] = ")"
                self._print_parenthesis(is_str,
                                        pos+1,
                                        n,
                                        open_b,
                                        close_b+1)
            if open_b < n:
                is_str[pos] = "("
                self._print_parenthesis(is_str,
                                        pos+1,
                                        n,
                                        open_b+1,
                                        close_b)


def format_string(line,
                  line_len):
    """

    :param line:
    :param line_len:
    :return:
    """
    formatted_line = []
    status = True

    start = 0
    end = len(line)
    while status:
        next_line = ""
        in_status = True
        while in_status:
            temp_line = ""
            if len(next_line) != 0:
                temp_line = next_line + " " + line[start]
            else:
                temp_line = line[start]
            if len(temp_line) == line_len:
                start = start + 1
                text = add_blank_space(temp_line,
                                       expected_size=line_len)
                formatted_line.append(text)
                next_line = ""
                temp_line = ""
                in_status = False
            elif len(temp_line) > line_len:
                temp_line = ""
                text = add_blank_space(next_line,
                                       expected_size=line_len)
                formatted_line.append(text)
                next_line = ""
                in_status = False
            else:
                next_line = temp_line
                start = start + 1

            if start >= end:
                text = add_blank_space(next_line,
                                       expected_size=line_len)
                formatted_line.append(text)
                in_status = False
                status = False

    return formatted_line


def add_blank_space(in_str,
                    expected_size):
    """

    :param in_str:
    :param expected_size:
    :return:
    """
    if in_str.count(" ") == 0:
        in_str = in_str + " "
        spaces_count = 1
    else:
        spaces_count = in_str.count(" ")
    result = in_str
    str_len = len(in_str)

    required_spaces = expected_size - str_len + spaces_count
    splits = split(x=required_spaces,
                   n=spaces_count)
    splits.reverse()
    len_s = len(splits)
    rev_result = result[::-1].replace(" ", " " * splits[-1], 1)
    result = rev_result[::-1].replace(" ", " " * splits[0], len_s-1)
    return result


def split(x, n):
    """

    :param x:
    :param n:
    :return:
    """
    split_list = []
    if x < n:
        print(-1)

    elif x % n == 0:
        for i in range(n):
            split_list.append(x // n)
    else:
        zp = n - (x % n)
        pp = x // n
        for i in range(n):
            if i >= zp:
                split_list.append(pp+1)
            else:
                split_list.append(pp)
    return split_list
