import sys
import guitarpro as gp

def parse_gp(file_path):
    # Parse gp and extract a list of notes.

    parsed_file = gp.parse(file_path)

    #ToDo: Extract notes.

    # First test on extracting notes. (FAIL)

    gp_reader = gp.GPFileBase(open(file_path, 'r'))

    while 1:

        try:
            print gp_reader.read('s', 1)
        except:
            print "End of file."
            break


if __name__ == "__main__":
    
    if len(sys.argv) > 1:

        parse_gp(sys.argv[1])
    
    else:

        input_file = "data/iron_maiden-flight_of_icarus.gp4"
        parse_gp(input_file)
    