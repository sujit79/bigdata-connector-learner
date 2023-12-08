import sys
from  bigdata_connector_learner import get_data_frame

def test_main():
    arguments = sys.argv[1:]
    print("Arguments to the Program are : ", *arguments)
   
    if(len(arguments) != 3) :
        print("Need Arguments in the following sequence .. verb, url, body")
        sys.exit()

    return get_data_frame(arguments[0], arguments[1], arguments[2])

