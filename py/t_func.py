def func1(statement):
    if isinstance(statement, dict):
        # statement = {
        #     'a': {'a': 1, 'b': 2, 'c': 3},
        #     'b': {'a': 1, 'b': 2, 'c': 3},
        #     'c': {'a': 1, 'b': 2, 'c': 3}
        # }
        statement = statement
        statement['a']['a'] = 'aaa'  # 没有重新深复制的话，修该嵌套的内容，会影响外部的
    if isinstance(statement, str):
        statement = statement.split(',')
    print('statement in func1', statement)
    statement = {'a': 1, 'b': 2, 'c': 3}
    print('statement in func1', statement)


if __name__ == '__main__':
    statement = 'a,a,a,a,a,a,'
    func1(statement)
    print('main statement', statement)
    statement = {
        'a': {'a': 1, 'b': 2, 'c': 3},
        'b': {'a': 1, 'b': 2, 'c': 3},
        'c': {'a': 1, 'b': 2, 'c': 3}
    }

    func1(statement)
    print('main statement', statement)
