# This file is responsible for waiting on responses from each hit

from __future__ import print_function
import crowdlib as cl
import time

hit_ids = []


def update_responses():

    load_active_hits()
    await_responses()


def load_active_hits():

    id_file = open("activeHITs.txt", "r+")
    print("Opening {0}".format(id_file.name))
    print("Awaiting responses to HITs...\n")

    id_nl = id_file.readline()
    while len(id_nl) != 0:
        hit_id = id_nl.split('\n')[0]
        hit_ids.append(hit_id)

        id_nl = id_file.readline()

    id_file.seek(0)
    id_file.truncate()  # After the HIT ids are extracted, nuke the file for the next iteration
    id_file.close()


def await_responses():

    print("HIT ID:\t\t\t\t\t\t\t\t\tResult:")

    for hit_id in hit_ids:
        hit = cl.get_hit(hit_id)
        print("{0}\t\t\t".format(hit.id), end="")
        while hit.is_available:
            time.sleep(2)
        for answer in hit.answers:
            print(answer.text)

    hit_ids.pop()

