scoring = {
    'Яблочко': 50,
    'Зеленое_кольцо': 25,
    'Внешнее_кольцо': {
        1: 8,
        2: 6,
        3: 42,
        4: 10,
        5: 23,
        6: 11,
        7: 50,
        8: 3,
        9: 29,
        10: 14,
        11: 38,
        12: 5,
        13: 19,
        14: 47,
        15: 26,
        16: 31,
        17: 2,
        18: 45,
        19: 9,
        20: 50
    },
    'Внутреннее_кольцо': {
        1: 2,
        2: 9,
        3: 56,
        4: 33,
        5: 18,
        6: 50,
        7: 4,
        8: 29,
        9: 11,
        10: 37,
        11: 5,
        12: 24,
        13: 48,
        14: 10,
        15: 31,
        16: 22,
        17: 45,
        18: 13,
        19: 27,
        20: 3
    }
}

def score(ring: str, score=None):
    if ring in ['Яблочко', 'Зеленое_кольцо']:
        return scoring[ring]
    return scoring[ring][score]