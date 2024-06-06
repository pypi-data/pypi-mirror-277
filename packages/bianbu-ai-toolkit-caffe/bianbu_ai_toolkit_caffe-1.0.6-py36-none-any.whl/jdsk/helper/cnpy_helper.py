# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.
#
# Copyright (c) 2023, spacemit.com, Inc. All Rights Reserved
#
# =============================================================
#
# Author: hongjie.qin@spacemit.com
# Brief:  Commandline tool to have a quick glance at npy/npz format data file
# History:
# 2023/09/19  v0.0.1  init/create

import argparse

__version__ = "0.0.1"

def get_argsparser_cnpy(parser = None, epilog = None):
    """Parse commandline."""
    if parser is None:
        parser = argparse.ArgumentParser(description="Toolkit to have a quick glance at npy/npz format data file.",
                                         formatter_class=argparse.RawDescriptionHelpFormatter, epilog=epilog)
    parser.add_argument("file", type=str, help="npy/npz data file path")
    return parser


def show_npfile(args):
    import numpy as np
    data = np.load(args.file)
    if isinstance(data, np.lib.npyio.NpzFile):
        for k, v in data.items():
            print("key: {}, word size: {}, num_vals: {}, shape: {}".format(
                k, v.nbytes // v.size if v.nbytes else 0, v.size, ",".join(map(str, v.shape))))
    elif isinstance(data, np.ndarray):
        print("word size: {}, num_vals: {}, shape: ({})".format(
            data.nbytes // data.size if data.nbytes else 0, data.size, ",".join(map(str, data.shape))))
    else:
        raise ValueError("Unknown object type {}".format(type(data)))


def main():
    parser = get_argsparser_cnpy(epilog="")
    args = parser.parse_args()
    show_npfile(args)


if __name__ == "__main__":
    main()