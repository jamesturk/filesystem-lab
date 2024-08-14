from os import walk
import pathlib


def print_errors(num, errors):
    if errors:
        print(f"Part {num} Incomplete!")
        for e in errors:
            print("    " + e)
        return False

    print(f"Part {num} Complete!")
    return True


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

    return print_errors(1, errors)


def check_filenames(dirname, expected) -> list[str]:
    """
    Check directory for a list of filenames, return list of errors.
    """
    errors = []
    actual = {f.name for f in pathlib.Path(dirname).glob("*")}
    for extra in actual - expected:
        errors.append(f"extra file {extra} in {dirname}")
    for missing in expected - actual:
        errors.append(f"missing file {missing} in {dirname}")
    return errors


def check_part2() -> bool:
    """
    Check if part two has been completed.
    """
    exp_animals = {
        "aardvark.txt",
        "bat.txt",
        "bear.txt",
        "cat.txt",
        "cow.txt",
        "dog.txt",
        "dolphin.txt",
        "frog.txt",
        "horse.txt",
        "rhino.txt",
        "monkey.txt",
    }
    exp_planets = {
        "earth.txt",
        "mars.txt",
        "mercury.txt",
        "neptune.txt",
        "saturn.txt",
        "uranus.txt",
        "jupiter.txt",
    }
    exp_comets = {
        "p-1-halley.txt",
        "p-12-pons-brooks.txt",
        "p-2-enke.txt",
        "p-6-dArrest.txt",
        "p-8-tuttle.txt",
        "p-10-tempel2.txt",
        "p-13-olbers.txt",
        "p-4-faye.txt",
        "p-7-pons-winnecke.txt",
        "p-9-tempel1.txt",
        "p-14-wolf.txt"
    }

    errors = check_filenames("animals", exp_animals) + check_filenames(
        "space/planets", exp_planets
    ) + check_filenames("space/comets", exp_comets)

    wolf_error = any(["wolf" in e for e in errors])

    if wolf_error:
        print("Hint: wolf.txt needs to be renamed to p-14-wolf.txt!")

    return print_errors(2, errors)


if __name__ == "__main__":
    if check_part1():
        if check_part2():
            pass
