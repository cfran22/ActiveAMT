# This is the driver for AMT Interface

import generateHIT as __hitGen__
import initHITType as __initHT__
import awaitResponses as __respWait__
import random

__max_hits__ = 1


def main():

    random.seed(None)  # Seeded with current system time

    repeat = 'y'

    while repeat.capitalize() == 'Y':
        hit_type = __initHT__.init_hittype()
        __hitGen__.gen_hit(hit_type)
        __respWait__.update_responses()

        repeat = raw_input("\nCreate another HIT? ")

main()
