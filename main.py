import numpy as np


def get_input():
    hue   = [0,0]
    sat   = [0,0]
    val = [0,0]

    presets ={'Jewel' : {'S':[73, 83],
                          'V':[56, 76]},
              'Pastel': {'S':[14, 21],
                          'V':[89, 96]},
              'Earth' : {'S':[36, 41],
                          'V':[36, 77]},
              'Neutral' : {'S':[1, 10],
                            'V':[70, 99]},
              'Flourecent' : {'S':[63, 100],
                                'V':[82, 100]},
              }

    no_colours = int(input("How many colors you need: "))

    hue[0]   = input("Enter Hue Min Range[0-360] (leave empty if none) ")
    if hue[0] == "": hue[0] = 0
    else: hue[0] = int(hue[0])
    hue[1]   = input("Enter Hue Max Range[0-360] (leave empty if none) ")
    if hue[1] == "": hue[1] = 360
    else: hue[1] = int(hue[1])

    yes_inp = ["Y","y"]
    use_presets = True if input("Use presets for Saturation and brightness?[Y/N] ") in yes_inp else False

    if not use_presets:
        sat[0]   = input("Enter Saturation Min Range[0-100] (leave empty if none) ")
        if sat[0] == "": sat[0] = 0.0
        else: sat[0] = float(int(sat[0])/100)
        sat[1]   = input("Enter Saturation Max Range[0-100] (leave empty if none) ")
        if sat[1] == "": sat[1] = 1.0
        else: sat[1] = float(int(sat[1])/100)

        val[0] = input("Enter Lightness Min Range[0-100] (leave empty if none) ")
        if val[0] == "": val[0] = 0.0
        else: val[0] = float(int(val[0])/100)
        val[1] = input("Enter Lightness Max Range[0-100] (leave empty if none) ")
        if val[1] == "": val[1] = 1.0
        else: val[1] = float(int(val[1])/100)
    else:
        print(f"Presets are:")
        for key in presets.keys():
            print(f"- {key}")
        preset = input("Enter Preset name: ")
        print(f"You chose {preset} Sat{presets[preset]['S'][0]}-{presets[preset]['S'][1]} , Val{presets[preset]['V'][0]}-{presets[preset]['V'][1]}")
        sat[0]=presets[preset]['S'][0]/100
        sat[1]=presets[preset]['S'][1]/100
        val[0]=presets[preset]['V'][0]/100
        val[1]=presets[preset]['V'][1]/100

    return [hue,sat,val], no_colours



def get_random_hsv_list(ihsv, no_colours):
    hsv_list = []
    for i in range(no_colours):
        random_h = np.random.randint(ihsv[0][0],ihsv[0][1])
        random_s = np.random.uniform(ihsv[1][0],ihsv[1][1])
        random_v = np.random.uniform(ihsv[2][0],ihsv[2][1])

        hsv_list.append([random_h,random_s,random_v])

    return hsv_list



def rgb_to_hex(rgb):
    def component_to_hex(c):
        _hex = hex(c)[2:]
        if len(_hex) == 1:
            return "0" + _hex
        else:
            return _hex

    return "#" + component_to_hex(rgb[0]) + component_to_hex(rgb[1]) + component_to_hex(rgb[2])



def hsv_to_rgb(rhsv):

    rgb_list=[]
    hex_list=[]


    for h,s,v in rhsv:
        def f(n):
            a = s * np.min([v, 1 - v])
            k = (n + h / 60) % 6

            return v - v*s*np.max([np.min([k, 4-k, 1]),0])

        rgb = [int(f(5)*255),int(f(3)*255),int(f(1)*255)]
        rgb_list.append(rgb)
        hex_list.append(rgb_to_hex(rgb))

    return  rgb_list, hex_list




if __name__ == '__main__':

    ihsv,no_colors=get_input()
    rhsv=get_random_hsv_list(ihsv,no_colors)
    rgb_list,hex_list = hsv_to_rgb(rhsv)


    for i,rgb in enumerate(rgb_list):
        print(f'\x1b[48;2;{rgb[0]};{rgb[1]};{rgb[2]}m\x1b[38;2;0;0;0m Color {i+1}: {hex_list[i]} \x1b[0m')

