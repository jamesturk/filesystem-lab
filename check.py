import pathlib



def check_part1() -> bool:
    """
    Check if part one has been completed.
    """
    errors = []

    for directory in ["animals", "space", "space/planets", "space/comets"]:
        if not pathlib.Path(directory).is_dir():
            errors.append(f"missing directory '{directory}'")
    if pathlib.Path("./planets").is_dir():
       errors.append("extra directory 'planets' (should be inside 'space')")
    if pathlib.Path("./comets").is_dir():
        errors.append("extra directory 'comets' (should be inside 'space')")

    if errors:
        print("Part 1 Incomplete!")
        for e in errors:
            print("    " + e)
        return False

    print("Part 1 Complete!")
    return True


def check_filenames(dirname, expected) -> list[str]:
    """
    Check directory for a list of filenames, return list of errors.
    """
    errors = []
    actual = {f.name for f in pathlib.Path(dirname).glob("*")}
    for extra in  (actual - expected):
        errors.append(f"extra file {extra} in {dirname}")
    for missing in (expected - actual):
        errors.append(f"missing file {missing} in {dirname}")
    return errors


def check_part2() -> bool:
    """
    Check if part two has been completed.
    """
    exp_animals = ["aardvark.txt", "bat.txt", "bear.txt", "cat.txt", "cow.txt", "dog.txt", "dolphin.txt", "frog.txt", "horse.txt", "rhino.txt", "wolf.txt"]
    exp_planets = ["earth.txt", "mars.txt", "mercury.txt", "neptune.txt", "saturn.txt", "uranus.txt"]

    errors = check_filenames("animals", exp_animals) + check_filenames("planets", exp_planets)



if __name__ == "__main__":
    if check_part1():
        if check_part2():
            pass
