# This file is responsible for generating HITs and pushing them to AMT

import crowdlib as cl
import random


# Generates the actual HIT(s)
def gen_hit(hit_type_info, num_hits=1):

    hit_type = cl.create_hit_type(
        title=(hit_type_info["title"]),
        description=hit_type_info["description"],
        reward=float(hit_type_info["reward"]),
        time_limit=eqval(hit_type_info["time_limit"]),
        keywords=hit_type_info["keywords"].split(','),
        qualification_requirements=hit_type_info["qualification_requirements"],
        autopay_delay=eqval(hit_type_info["autopay_delay"])
    )

    hit_ids = open("activeHITs.txt", "a")

    random.seed(None)  # Seeded with current system time

    for i in range(0, num_hits):
        hit = hit_type.create_hit([cl.text_field("TestField{0}".format(random.randint(0, 50)), "q1")])
        print("Generating HIT: {0}".format(hit.id))
        hit_ids.write(hit.id + '\n')
        print("Writing {0} to {1}\n".format(hit.id, hit_ids.name))

    hit_ids.close()


# Converts string representations of equations and evaluates them - Only multiplication chains as they are most common
def eqval(str_val):

    if isinstance(str_val, basestring):

        operands = str_val.split('*')
        val = 1

        for operand in operands:
            val *= int(operand)

        return val

    else:
        return str_val
