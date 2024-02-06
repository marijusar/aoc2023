def find_destination_number(map, source_number):
    for the_range in map :
        destination_range_start, source_range_start, range_length = [int(x) for x in the_range.split(" ")]
        
        # Check whether source number is within the range
        if source_number >= source_range_start and source_number <= source_range_start + range_length - 1 :
            # If yes, then we should calculate the offset between source number and source_range_start, so we can 
            # calculate the destination_number using than offset.
            offset = source_number - source_range_start
            return destination_range_start + offset

            

    return source_number

def parse_maps(maps, seed) :
    source_number = seed
    for map in maps :
        # new source number is the destination number for next map
        destination_number = find_destination_number(map, source_number)
        source_number = destination_number

    return source_number

    
def parse_input() :
    f = open('./input.txt') 
    txt = f.read()
    sections = txt.split("\n\n") 
    seeds = [int(x) for x in sections[0].split(":")[1].strip().split(' ')]
    maps =  [x.strip().split("\n")[1:] for x in sections[1:len(sections)]]
    
    return [maps, seeds]


def part_one() :
    maps, seeds = parse_input()

    locations = []

    for seed in seeds :
        location = parse_maps(maps, seed)
        locations.append(location)

    print(min(locations))
    



# part_one()

def covert_seed_range_to_map(seeds) :
    mapped_seeds = []
    for i  in range(0, len(seeds), 2):
        mapped_seeds.append([seeds[i], seeds[i], seeds[i+1]])
    return mapped_seeds

def map_range(range_map) :
    mapped_ranges = []
    for map_entry in range_map :
        tuple = [int(x) for x in map_entry.split(" ")]
        mapped_ranges.append(tuple)
    return mapped_ranges


def intersecting_ranges(seed_range, almanac_map):
    acc = []
    destination_range_start, _ , range_length = seed_range
    destination_range_end = destination_range_start + range_length -1
    for alamanac_entry in almanac_map :

        _, alamanac_source_range_start, alamanac_range_length = alamanac_entry

        almanac_source_range_end = alamanac_source_range_start + alamanac_range_length

        if destination_range_end < alamanac_source_range_start :
            continue

        if destination_range_start > almanac_source_range_end :
            continue

        acc.append(alamanac_entry)

    return acc



def child_is_partial_range(child_range, parent_range) :
    child_destination_start, _, child_range_length = child_range
    child_destination_end = child_destination_start + child_range_length
    _, parent_source_start, parent_range_length = parent_range
    parent_source_end = parent_source_start + parent_range_length

    if parent_source_start <= child_destination_start and parent_source_end >= child_destination_end :
        return True

    return False

def construct_non_overlapping_range(map_range) :
        destination_range_start, _ , range_length = map_range
        
        return [destination_range_start, destination_range_start, range_length]

def construct_new_range_from_fully_overlapping_range(seed_range, almanac_range) :
    seed_destination_start, _, seed_range_length = seed_range
    seed_destination_end = seed_destination_start + seed_range_length
    almanac_destination_start, almanac_source_start, almanac_range_length = almanac_range
    almanac_source_end = almanac_source_start + almanac_range_length

    new_range_source_start = seed_destination_start
    new_range_range_length = seed_range_length
    offset = seed_destination_start - almanac_source_start
    new_range_desination_start = almanac_destination_start + offset
    return [new_range_desination_start, new_range_source_start, new_range_range_length]

def construct_new_range_from_non_fully_overlapping_range(seed_range, almanac_range):
    seed_destination_start, _, seed_range_length = seed_range
    seed_destination_end = seed_destination_start + seed_range_length
    almanac_destination_start, almanac_source_start, almanac_range_length = almanac_range
    almanac_source_end = almanac_source_start + almanac_range_length

    if seed_destination_start < almanac_source_start and seed_destination_end > almanac_source_end :
        seed_left_offset = almanac_source_start - seed_destination_start
        seed_left_range = [seed_destination_start, seed_destination_start, seed_left_offset]
        seed_right_offset = seed_destination_end - almanac_source_end
        seed_right_range = [almanac_source_end, almanac_source_end, seed_right_offset]

        return [seed_left_range, almanac_range, seed_right_range]

    if seed_destination_start < almanac_source_start :
        seed_left_offset = almanac_source_start - seed_destination_start
        seed_left_range = [seed_destination_start, seed_destination_start, seed_left_offset]
        remaining_offset = seed_range_length - seed_left_offset
        remaining_almanac_range = [almanac_destination_start, almanac_source_start, remaining_offset]
        return [seed_left_range, remaining_almanac_range]

    if seed_destination_end > almanac_source_end :
        seed_right_offset = seed_destination_end - almanac_source_end
        seed_right_range = [almanac_source_end, almanac_source_end, seed_right_offset]
        remaining_almanac_offset = seed_range_length - seed_right_offset
        new_almanac_destination_start = almanac_destination_start + seed_right_offset - 1
        new_almanac_range = [new_almanac_destination_start, seed_destination_start, remaining_almanac_offset]

        return [new_almanac_range, seed_right_range]


def is_seed_range_left_padded(seed_range, almanac_range):
    seed_destination_start, _ , range_length = seed_range
    _ , almanac_source_start, _  = almanac_range
        
    return seed_destination_start < almanac_source_start

# case 1 seed_range overlaps with almanac range fully
# case 2 seed_range overlaps 
def construct_new_range_from_multiple_overlapping_ranges(seed_range, almanac_ranges):
    def sort_by_destination(almanac_range) :
        return almanac_range[1]
    sorted_ranges = sorted(almanac_ranges, key=sort_by_destination)
    seed_range_copy = seed_range.copy()
    new_ranges = []
    seed_destination_start, seed_source_start, seed_range_length = seed_range
    seed_destination_end = seed_destination_start + seed_range_length


    for almanac_range in sorted_ranges :
        if len(seed_range_copy) == [] :
            return new_ranges
        almanac_destination_start, almanac_source_start, almanac_range_length = almanac_range
        almanac_source_end = almanac_source_start + almanac_range_length

        #If seed_range start off left of the range intersections
        if seed_range_copy[0] < almanac_source_start :
            left_pad_offset = almanac_source_start - seed_destination_start
            new_ranges.append([seed_destination_start, seed_destination_start, left_pad_offset])
            new_range_length = seed_range_length - left_pad_offset
            seed_range_copy = [almanac_source_start, seed_source_start, new_range_length]

        # If seed range starts at range intersection
        if almanac_source_start == seed_range_copy[0] :

            # if seed_range ends before almanac range
            if seed_range_copy[2] <= almanac_range_length :
                new_ranges.append([almanac_destination_start, almanac_source_start, seed_range_copy[2]])
            # if seed range spans beyond almanac range
            else :
                new_ranges.append([almanac_destination_start, almanac_source_start, almanac_range_length])
                new_offset = seed_range_copy[2] - almanac_range_length
                seed_range_copy = [almanac_source_end, almanac_source_end, new_offset]


        # If seed range start after range intersection

        if seed_range_copy[0] > almanac_source_start :
            left_pad_offset = seed_range_copy[0] - almanac_source_start
            if sorted_ranges[len(sorted_ranges) -1][0] == almanac_destination_start and almanac_source_end <= seed_range_copy[0] :
                new_ranges.append(seed_range_copy)
                return new_ranges


            if seed_range_copy[0] + seed_range_copy[2] < almanac_source_end :
                new_alamanac_range_length = almanac_source_start + almanac_range_length - seed_range_copy[0] 
                new_ranges.append([almanac_destination_start + left_pad_offset, seed_range_copy[0], new_alamanac_range_length])
                new_source_start = seed_range_copy[0] + new_alamanac_range_length
                seed_range_copy = []

            else :
                # if seed_range_copy[0] >= almanac_source_end :
                #     new_ranges.append(seed_range_copy)
                # is last range
                if sorted_ranges[len(sorted_ranges) -1][0] == almanac_destination_start :
                    new_ranges.append([almanac_destination_start, almanac_source_start, almanac_range_length])
                    new_range_start = almanac_destination_start + almanac_range_length
                    new_range_length = seed_range_copy[2] - almanac_range_length
                    new_ranges.append([new_range_start, new_range_start, new_range_length])
                    seed_range_copy = []
                else :
                    remaining_offset = almanac_source_start + almanac_range_length - seed_range_copy[0] 
                    new_ranges.append([almanac_destination_start + left_pad_offset, seed_range_copy[0], remaining_offset])
                    remaining_seed_range_offset = seed_range_copy[2] - remaining_offset
                    seed_range_copy = [almanac_source_end, almanac_source_end ,remaining_seed_range_offset]
    return new_ranges


def locations_for_ranges(seed_ranges, maps) :
    if len(maps) == 0 :
        return seed_ranges

    new_ranges = []
    for seed_range in seed_ranges :
        intersectors = intersecting_ranges(seed_range, maps[0])

        if len(intersectors) == 0 :
            non_overlapping_range = construct_non_overlapping_range(seed_range)
            new_ranges.append(non_overlapping_range)
            continue
        if len(intersectors) == 1 :
            is_partial_range = child_is_partial_range(seed_range, intersectors[0])
            if is_partial_range :
                new_range = construct_new_range_from_fully_overlapping_range(seed_range, intersectors[0])
                new_ranges.append(new_range)
                continue
            else :
                multiple_new_ranges = construct_new_range_from_non_fully_overlapping_range(seed_range, intersectors[0])
                for i in multiple_new_ranges :
                    new_ranges.append(i)
        if len(intersectors) > 1 :
            overlapping_ranges = construct_new_range_from_multiple_overlapping_ranges(seed_range, intersectors)
            for i in overlapping_ranges :
                new_ranges.append(i)
                

    return locations_for_ranges(new_ranges, maps[1:])


def part_two():
    maps, seeds = parse_input() 
    seeds_range = covert_seed_range_to_map(seeds)
    map_tuples = list(map(lambda x: map_range(x), maps))
    locations = locations_for_ranges(seeds_range, map_tuples)
    destinations = [x[0] for x in locations]

    print(min(destinations))



part_two()
# Fuck yes, this was very hard...
