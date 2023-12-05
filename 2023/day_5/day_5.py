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


def get_location_2(seed, maps):
    source = seed
    for map in maps:
        for map_dest, map_source in map:
            if source >= map_source[0] and source <= map_source[1]:
                diff = source - map_source[0]
                dest = map_dest[0] + diff
                source = dest
                break
    return source


def find_overlapping_range(range1, range2):
    n1, n2 = range1
    m1, m2 = range2

    if n2 < m1 or m2 < n1:
        return None  # No overlap

    overlap_start = max(n1, m1)
    overlap_end = min(n2, m2)

    return (overlap_start, overlap_end)


def nth_lowest_in_map(map, n):
    dests = [m[0][0] for m in map]
    lowest = [i for _, i in sorted(zip(dests, map))]
    return lowest[n]


def find_from_source(map, start_dest, start_source):
    for map_dest, map_source in map:
        if find_overlapping_range((start_dest, start_source), (map_dest, map_source)):
            return map_dest, map_source
    return start_dest, start_source


def get_lowest_location(seed_ranges, maps):
    rank = 0
    path = []

    maps = list(maps.values())
    start_dest, start_source = nth_lowest_in_map(maps[-1], rank)
    path.append((start_dest, start_source))

    for map in reversed(maps[:-1]):
        start_dest, start_source = find_from_source(map, start_dest, start_source)
        path.append((start_dest, start_source))

    path = list(reversed(path))
    # See which seed range this is
    seed_range = None
    for sr in seed_ranges:
        if find_overlapping_range(path[0][1], sr):
            seed_range = sr

    min_loc = 1e10
    count = 0
    this_seed = seed_range[0]
    while this_seed <= seed_range[1]:
        print(count)
        loc = get_location_2(this_seed, maps)
        if loc < min_loc:
            min_loc = loc
        this_seed += 1
        count += 1

    return min_loc


def get_lowest_location_2(seed_range, maps):
    maps = list(maps.values())

    source_range = seed_range
    for map in maps:
        for map_dest, map_source in map:
            overlap = find_overlapping_range(map_source, source_range)
            if overlap:
                overlap_size = overlap[1] - overlap[0]
                source_range = (map_dest[0] + overlap_size, map_dest[1])

    return source_range[0]


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
    locations = []
    for seed_range in seed_ranges:
        locations.append(get_lowest_location_2(seed_range, maps))
    answer = min(locations)
    print(f"PT 2 ANSWER: {answer}")


if __name__ == "__main__":
    #    with open("2023/day_5/test_input.txt", "r") as f:
    with open("2023/day_5/input.txt", "r") as f:
        input = f.readlines()
    # main_1(input)
    main_2(input)
