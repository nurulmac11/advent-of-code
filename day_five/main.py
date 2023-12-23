file_path = "test_input.txt"
file_path = "input.txt"


# Function to split the file contents into sections
def split_file_data(file_content):
    sections = {}
    lines = file_content.split("\n")
    current_section = None

    for line in lines[1:]:
        if line.strip():  # Checking if the line has content
            if ":" in line:  # Assuming section names end with a colon
                current_section = line.strip()
                sections[current_section] = []
            else:
                sections[current_section].append(list(map(int, line.split())))

    return lines[0].split(":")[1].strip().split(" "), sections


def seek_hide(section, pivot):
    for limit in section:
        if pivot >= limit[1] and pivot <= limit[1] + limit[2]:
            return (limit[0] - limit[1]) + pivot
    return pivot


def seek_chunk(section, pivot1, pivot2):
    # need to sort limits by source order
    sorted_section = sorted(section, key=lambda x: x[1])
    new_pivots = []
    pivot1 = int(pivot1)
    pivot2 = int(pivot2)
    # print("sortedsection limits", sorted_section)
    # print("pivot r: ", pivot1, pivot2)
    for limit in sorted_section:
        down_limit = int(limit[1])
        up_limit = int(limit[1]) + int(limit[2])
        diff = int(limit[0]) - int(limit[1])
        intersect_start = max(pivot1, down_limit)
        intersect_end = min(pivot2, up_limit)
        if intersect_end <= intersect_start:
            continue
        # print("i start", intersect_start)
        # print("i end", intersect_end)
        # print("from -to:", down_limit, up_limit)
        # print("diff", diff)
        rp1 = pivot1
        rp2 = pivot2
        if intersect_start > pivot1 and pivot2 > intersect_start:
            recursive_tmp = seek_chunk(section, pivot1, intersect_start)
            new_pivots += recursive_tmp
            pivot1 = intersect_start
        if intersect_end < rp2 and rp1 < intersect_end:
            recursive_tmp = seek_chunk(section, intersect_end, rp2)
            new_pivots += recursive_tmp
            pivot2 = intersect_end
        if intersect_start >= pivot1 and intersect_end <= pivot2:
            new_pivots.append([pivot1 + diff, pivot2 + diff])
            break
    # print("new pivots:", new_pivots)
    # print("\n\n")
    if not new_pivots:
        return [[pivot1, pivot2]]
    return new_pivots


with open(file_path, "r") as file:
    file_content = file.read()


def create_chunks(lst, chunk_size):
    return [lst[i : i + chunk_size] for i in range(0, len(lst), chunk_size)]


# Split the file content into sections
seeds, data_sections = split_file_data(file_content)
seed_chunks = create_chunks(seeds, 2)
# print(seed_chunks)
locs = None
pivots = []
for chunk in seed_chunks:
    p1, p2 = int(chunk[0]), int(chunk[0]) + int(chunk[1])
    pivots.append([p1, p2])

new_pivots = pivots

locs = []
for sname, section in data_sections.items():
    # print(section)
    # print("pivots:", pivots)
    new_pivots = []
    for pivot in pivots:
        r = seek_chunk(section, pivot[0], pivot[1])
        new_pivots += r
    pivots = new_pivots
    # print(sname)
    # print("pivots:", new_pivots)
    # print("\n\n")
    # break
for p in new_pivots:
    locs.append(p[0])
print(f"min loc: {min(locs)}")
# print(new_pivots)
