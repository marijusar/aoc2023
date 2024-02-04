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
    f = open('./test.txt') 
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


def find_new_ranges(source_range, map_ranges) :
    min_source_destination, _, range_length = source_range
    max_source_destination = min_source_destination + range_length -1
    acc = []

    for map_range in map_ranges :
        _, min_map_source, map_length = map_range
        max_map_source = min_map_source + map_length - 1
        min_new_range = None
        max_new_range = None
        if min_source_destination > min_map_source and max_source_destination > max_map_source :
            min_new_range = max_map_source
            max_new_range = max_source_destination

        if min_source_destination < min_map_source and max_source_destination < max_map_source :
            min_new_range = min_source_destination 
            max_new_range = min_map_source

        if min_new_range and max_new_range:
            range_length = max_new_range - min_new_range + 1
            acc.append([min_new_range, min_new_range, range_length])
    return acc

def find_overlapping_ranges(source_range, map_ranges) :
    min_source_destination, _, range_length = source_range
    max_source_destination = min_source_destination + range_length -1
    acc = []
    for map_range in map_ranges :
        min_map_destination, min_map_source, map_length = map_range
        max_map_source = min_map_source + map_length - 1
        if min_source_destination < min_map_source :
            acc.append(map_range)

        if max_source_destination > max_map_source :
            acc.append(map_range)

        if max_source_destination <= max_map_source and min_source_destination >= min_map_source:
            new_length = max_map_source - max_source_destination
            acc.append([min_map_destination, min_source_destination, new_length])
    return acc



def flatten_maps(z) :
    return [y for x in z for y in x]


def find_location_for_range(source_range, maps) :
    if len(maps) ==0 : 
        return [source_range]
    print(maps)


    new_ranges = find_new_ranges(source_range, maps[0])  
    overlapping_ranges = find_overlapping_ranges(source_range, maps[0])



    if len(new_ranges) > 0 :
        return flatten_maps([find_location_for_range(x, maps[1:]) for x in new_ranges])+ flatten_maps([find_location_for_range(x, maps[1:]) for x in overlapping_ranges] )
    
    return flatten_maps([find_location_for_range(x, maps[1:]) for x in overlapping_ranges] )




    

def part_two():
    maps, seeds = parse_input() 
    seeds_range = covert_seed_range_to_map(seeds)
    map_tuples = list(map(lambda x: map_range(x), maps))
    locations = [y for x in [find_location_for_range(x, map_tuples) for x in seeds_range ] for y in x]
    unique_locations = [list(i) for i in set(tuple(i) for i in locations)]
    unique_destinations = [x[0] for x in unique_locations]

    # print(seeds_range[0])
    print(min(unique_destinations))




part_two()
