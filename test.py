import argparse

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--install", required=False, help="Use this parameter to install all Discord clients.")
args = vars(ap.parse_args())
if args["install"] not in ["stable", "ptb", "canary", "development", "all", None]:
    print(f"{args['install']} is not a valid version, please use one of the following: \"stable\", \"ptb\", \"canary\", \"development\" or \"all\"")
    exit()