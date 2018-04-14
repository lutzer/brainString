# @Author: Lutz Reiter [http://www.lu-re.de] <lutz>
# @Date:   2018-04-13T15:34:51+02:00
# @Project: Brain String
# @Last modified by:   lutz
# @Last modified time: 2018-04-13T15:41:03+02:00

import numpy as np

# converts rgb color values from 0-255 to 0-1
def convertColor(colorRgb):
    return np.array(colorRgb)/255.0
