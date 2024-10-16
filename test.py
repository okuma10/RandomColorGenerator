# import colorsys,numpy as np, colorutils
#
# def rgb_to_hex(rgb):
#     def component_to_hex(c):
#         _hex = hex(c)[2:]
#         if len(_hex) == 1:
#             return "0" + _hex
#         else:
#             return _hex
#
#     return "#" + component_to_hex(rgb[0]) + component_to_hex(rgb[1]) + component_to_hex(rgb[2])
#
# string = ''
# for i in range(360):
#     # color =  i/360
#     # col = np.array(colorsys.hsv_to_rgb(i/360, .8, .75))*255
#     # r = int(col[0]) + 1 if col[0]-int(col[0]) >.5 else int(col[0])
#     # g = int(col[1]) + 1 if col[0]-int(col[1]) >.5 else int(col[1])
#     # b = int(col[2]) + 1 if col[2]-int(col[2]) >.5 else int(col[2])
#     col = colorutils.hsv_to_rgb((i,.8,.75))
#     r = int(col[0]) + 1 if col[0]-int(col[0]) >.5 else int(col[0])
#     g = int(col[1]) + 1 if col[1]-int(col[1]) >.5 else int(col[1])
#     b = int(col[2]) + 1 if col[2]-int(col[2]) >.5 else int(col[2])
#     test_col = colorutils.hsv_to_hex((i,.8,.75))
#     test_rgb = colorutils.hex_to_rgb(test_col)
#     test_hex = rgb_to_hex((r,g,b))
#     print(f'hsv_to_rgb:       {col}')
#     print(f"test_rgb: {test_rgb} | r,g,b={r},{g},{b} ")
#     col_hex = rgb_to_hex([r,g,b])
#     string+=f'\x1b[48;2;{r};{g};{b}m\x1b[38;2;0;0;0mhex-{col_hex} rgb-{r};{g};{b} | \x1b[0m'
#
# print(string)

f_red  = "\x1b[32;2;235;59;90m"
bld = "\x1b[1m"
rs = '\x1b[0m'

print(f"{f_red}{bld}This text is bold {rs}")
print(f"{f_red}This text is not bold {rs}")
