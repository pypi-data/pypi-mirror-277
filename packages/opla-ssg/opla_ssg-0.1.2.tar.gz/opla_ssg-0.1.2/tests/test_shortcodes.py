import re


def test_publications_sub():
    s = (
        "Laurent Navoret. A two-species hydrodynamic model of particles "
        "interacting through self-alignment. Mathematical Models and "
        "Methods in Applied Sciences, 2012, "
        "&#x27E8;10.1142/S0218202513500036&#x27E9;. "
        "&#x27E8;hal-00924803&#x27E9;"
    )
    url = "https://hal.science/hal-00924803"

    # Replace "&#x27E8;(.*)&#x27E8;" by "[&#x27E8;(.*)&#x27E9;]({doc['uri_s']})"
    pattern1 = re.compile(r"&#x27E8;hal-(.*)&#x27E9;")
    # # Replace "&#x27E8;10.(.*)&#x27E9;." by "[&#x27E8;10.(.*)&#x27E9;.](dx.doi.org/10.(.*))"
    pattern2 = re.compile(r"&#x27E8;\b(10[.][0-9]{4,}(?:[.][0-9]+)*/(?:(?![\"&\'<>])\S)+)\b&#x27E9;")
    s = re.sub(pattern1, r"[&#x27E8;hal-\g<1>&#x27E9;]" + f"({url})", s)
    print(s)
    s = re.sub(pattern2, r"[&#x27E8;\g<1>&#x27E9;](https://dx.doi.org/\g<1>)", s)
    print(s)
    assert s == (
        "Laurent Navoret. A two-species hydrodynamic model of particles interacting through self-alignment. "
        "Mathematical Models and Methods in Applied Sciences, 2012, "
        "[&#x27E8;10.1142/S0218202513500036&#x27E9;](https://dx.doi.org/10.1142/S0218202513500036). "
        "[&#x27E8;hal-00924803&#x27E9;](https://hal.science/hal-00924803)"
    )
