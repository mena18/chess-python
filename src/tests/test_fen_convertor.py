from settings import FenConvertor


def test_fen_converstions():
    assert FenConvertor.from_fen_to_pos("e4") == (4, 4)
    assert FenConvertor.from_fen_to_pos("e2") == (6, 4)
    assert FenConvertor.from_fen_to_pos("d1") == (7, 3)
    assert FenConvertor.from_fen_to_pos("a7") == (1, 0)
    assert FenConvertor.from_fen_to_pos("c8") == (0, 2)


def test_pos_conversions():
    assert FenConvertor.from_pos_to_fen((4, 4)) == "e4"
    assert FenConvertor.from_pos_to_fen((6, 4)) == "e2"
    assert FenConvertor.from_pos_to_fen((7, 3)) == "d1"
    assert FenConvertor.from_pos_to_fen((1, 0)) == "a7"
    assert FenConvertor.from_pos_to_fen((0, 2)) == "c8"
