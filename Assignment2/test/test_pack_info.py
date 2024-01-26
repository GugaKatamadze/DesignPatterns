from pos.repository.pack_info import PackInfo


def test_pack_info() -> None:
    pack_info = PackInfo("2 kartofili fris kombo", 1, 20)

    assert pack_info.get_name() == "2 kartofili fris kombo"
    assert pack_info.get_amount() == 1
    assert pack_info.get_discount() == 20
