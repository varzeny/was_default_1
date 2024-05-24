import json, os


path1 = os.path.dirname( __file__ )
path2 = os.path.dirname( path1 )

path3 = os.path.dirname( os.path.dirname( __file__ ) )


if __name__ == "__main__":
    print( path3 )