import re

NUMBER_REGEX = re.compile(r"\d+")
NUMBER_REGEX_3 = re.compile(r"\d+ \d+ \d+")
MAP_REGEX = re.compile(r"map:")


def get_location(seed, maps):
    source = seed
    for map in maps.values():
        for map_dest, map_source, r in map:
            if source >= map_source and source <= map_source + r:
                diff = source - map_source
                dest = map_dest + diff
                source = dest
                break
    return source


def n_in_range(n, r):
    if n >= r[0] and n <= r[1]:
        return n - r[0]
    return False


def lookup_dest_to_source(map, dest):
    for map_dest_r, map_source_r in map:
        offset = n_in_range(dest, map_dest_r)
        if offset is not False:
            return map_source_r[0] + offset
    return dest


def make_maps(input, pt2=False):
    maps = {}
    map_index = -1
    for line in input:
        if MAP_REGEX.search(line):
            map_index += 1
            maps[map_index] = []
            continue

        if NUMBER_REGEX_3.search(line):
            dest, source, r = NUMBER_REGEX.findall(line)
            if pt2:
                maps[map_index].append(((int(dest), int(dest) + int(r)), (int(source), int(source) + int(r))))
            else:
                maps[map_index].append((int(dest), int(source), int(r)))
    return maps


def main_1(input):
    seeds = NUMBER_REGEX.findall(input[0])
    maps = make_maps(input[2:])
    locations = []
    for seed in seeds:
        locations.append(get_location(int(seed), maps))
    answer = min(locations)
    print(f"PT 1 ANSWER: {answer}")


def main_2(input):
    seeds = NUMBER_REGEX.findall(input[0])
    seed_ranges = []
    for i in list(range(len(seeds)))[::2]:
        seed_ranges.append((int(seeds[i]), int(seeds[i]) + int(seeds[i + 1])))
    maps = make_maps(input[2:], pt2=True)

    start_dest = 0
    seed_found = False
    while not seed_found:
        if start_dest % 1000 == 0:
            print(start_dest)

        # Traverse through the maps
        d = start_dest
        for map in list(maps.values())[::-1]:
            d = lookup_dest_to_source(map, d)

        # Check if the seed value returned exists in the seed ranges
        for seed_range in seed_ranges:
            if n_in_range(d, seed_range):
                seed_found = True
                break
        start_dest += 1

    print(f"PT 2 ANSWER: {start_dest-1}")


if __name__ == "__main__":
    with open("2023/day_5/input.txt", "r") as f:
        input = f.readlines()
    # main_1(input)
    main_2(input)
