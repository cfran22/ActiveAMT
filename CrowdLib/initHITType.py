# This file is responsible for receiving data from an outside source

import os
import glob
from crowdlib_settings import defaults


# Sets all attributes of a hit_type - Defaults from crowdlib_settings used if not overridden by an init file
def init_hittype():

    init_file = glob.glob1(os.getcwd(), "*.init")  # Grabs all .init files from CWD. Should only be one!

    if len(init_file) == 0:  # init file does not exist
        raise UserWarning("{0} does not contain a HITType initialization file!".format(os.getcwd()))
    else:  # init file exists

        init_file = init_file[0]
        hit_type = defaults  # Gets all of the default values from crowdlib_settings
        opfile = open(init_file)

        print("\nInitializing HITType from: {0}\n".format(init_file))

        line = opfile.readline()
        while len(line) != 0:  # Sets all available keys from the HITTYpe.init file

            key_val_pair = line.split(':')
            key, val = key_val_pair[0], key_val_pair[1].split('\n')[0]
            hit_type[key] = val

            line = opfile.readline()

        opfile.close()

        return hit_type


