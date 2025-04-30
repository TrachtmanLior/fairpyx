from fairpyx.algorithms.leximin_primal import leximin_primal

def test_simple_allocation():
    demands = {
        1: (1, {'a'}),
        2: (1, {'b'}),
        3: (1, {'a', 'b'})
    }
    capacities = {'a': 1, 'b': 1}
    result = leximin_primal(demands, capacities)
    assert isinstance(result, dict)
    assert abs(sum(result.values()) - 1) < 1e-6

def test_empty_input():
    demands = {}
    capacities = {}
    result = leximin_primal(demands, capacities)
    assert result == {}

def test_overconstrained():
    demands = {
        1: (1, {'a'}),
        2: (1, {'a'}),
        3: (1, {'a'})
    }
    capacities = {'a': 2}
    result = leximin_primal(demands, capacities)
    assert isinstance(result, dict)

def test_randomized_properties():
    import random
    N = 10
    demands = {i: (1, {'a', 'b'}) for i in range(1, N + 1)}
    capacities = {'a': 5, 'b': 5}
    result = leximin_primal(demands, capacities)
    assert abs(sum(result.values()) - 1) < 1e-6
