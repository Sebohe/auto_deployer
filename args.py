import argparse

def arg_parser():

    parser = argparse.ArgumentParser()

    parser.add_argument('-n',
                        dest="nodeURL",
                        default="http://localhost:8545",
                        type=str,
                        help="node url input"
                        )

    parser.add_argument('-s',
                        dest="sourceDir",
                        default=".",
                        type=str,
                        help="contracts source directory"
                        )

    parser.add_argument('-b',
                        dest="buildDir",
                        default="./build",
                        type=str,
                        help="compiled contracts dir"
                        )

    parser.add_argument('-c',
                        dest="compile",
                        default=False,
                        type=bool,
                        help="if flag is present program will compile the contracts"
                        )

    parser.add_argument('-d',
                        dest="deployer",
                        default="0",
                        type=str,
                        help="deployer address, can be an address or a number"
                        )
    
    parser.add_argument('-C',
                        dest="config",
                        default="project.conf",
                        type=str,
                        help="config file path"
                        )
    try:
        return parser.parse_args()
    except:
        exit(2)
