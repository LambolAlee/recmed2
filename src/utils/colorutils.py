import re

from PySide6.QtGui import QColor


regex_qcolor = re.compile(r"""
    ^
    (?:
        (?:\#[0-9a-fA-F]{3})  # 3位十六进制颜色代码
        |
        (?:\#[0-9a-fA-F]{6})  # 6位十六进制颜色代码
        |
        (?:[a-zA-Z]+)         # 颜色名称
    )
    $
""", re.VERBOSE)

regex_func_rgb = re.compile(r"""
    ^
    rgb\s*
    \(
        \s*([0-9]+)\s*,    # 红色值
        \s*([0-9]+)\s*,    # 绿色值
        \s*([0-9]+)\s*     # 蓝色值
    \)
    $
""", re.VERBOSE)

regex_hex_rgba = re.compile(r"^\#[0-9a-fA-F]{8}$")

regex_func_rgba = re.compile(r"""
    ^
    rgba?\s*
    \(
        \s*([0-9]+)\s*,    # 红色值
        \s*([0-9]+)\s*,    # 绿色值
        \s*([0-9]+)\s*,    # 蓝色值
        \s*([0-9]+)\s*     # 透明度值
    \)
    $
""", re.VERBOSE)


def string2QColor(string: str, alpha: bool) -> QColor:
    string = string.strip()

    if regex_qcolor.match(string):
        return QColor(string)

    m = regex_func_rgb.match(string)
    if m:
        return QColor(int(m.group(1)), int(m.group(2)), int(m.group(3)))

    if alpha:
        if regex_hex_rgba.match(string):
            return QColor(string)

        m = regex_func_rgba.match(string)
        if m:
            return QColor(int(m.group(1)), int(m.group(2)), int(m.group(3)), int(m.group(4)))
    
    return QColor(-1, -1, -1)


def colorLumaF(color: QColor) -> float:
    return 0.30 * color.redF() + 0.59 * color.greenF() + 0.11 * color.blueF();
