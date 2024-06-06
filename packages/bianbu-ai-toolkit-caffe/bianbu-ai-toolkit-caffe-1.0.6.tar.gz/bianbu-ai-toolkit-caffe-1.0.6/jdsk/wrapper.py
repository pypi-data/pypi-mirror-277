def get_args_parser():
    """Parse commandline."""
    import argparse
    parser = argparse.ArgumentParser(description="Spacemit AI Toolkit(Version: 2024/01/15)",
                                     formatter_class=argparse.RawDescriptionHelpFormatter, epilog="")

    # Note:
    # 1. It seems that `required` isn't a keyword argument for py3.6;
    subparsers = parser.add_subparsers(dest='command', help='')

    subparser_convert = subparsers.add_parser('convert')
    # add subparser for different model type
    subparser_convert_framework = subparser_convert.add_subparsers(dest='framework', help='')
    from jdsk.converter.argsparser import get_argsparser_onnx, get_argsparser_tf
    # add onnx parser
    subparser_convert_onnx = subparser_convert_framework.add_parser('onnx')
    subparser_convert_onnx = get_argsparser_onnx(subparser_convert_onnx)
    subparser_convert_onnx.add_argument("--config", "-c", type=str, default=None, help="config file path for calibration")
    # add tf parser
    subparser_convert_tf1 = subparser_convert_framework.add_parser('tf1')
    subparser_convert_tf1 = get_argsparser_tf(subparser_convert_tf1)
    subparser_convert_tf1.add_argument("--config", "-c", type=str, default=None, help="config file path for calibration")
    subparser_convert_tf2 = subparser_convert_framework.add_parser('tf2')
    subparser_convert_tf2 = get_argsparser_tf(subparser_convert_tf2)
    subparser_convert_tf2.add_argument("--config", "-c", type=str, default=None, help="config file path for calibration")
    # add paddle parser
    from jdsk.converter.paddle2jdsk import arg_parser as get_argsparser_paddle
    subparser_convert_paddle = subparser_convert_framework.add_parser('paddle')
    subparser_convert_paddle = get_argsparser_paddle(subparser_convert_paddle)
    subparser_convert_paddle.add_argument("--config", "-c", type=str, default=None, help="config file path for calibration")
    # add caffe parser
    # Note: To support caffe => coreml => onnx, one needs to resolve the package version conflicts.
    from jdsk.converter.argsparser import get_argsparser_caffe
    subparser_convert_caffe = subparser_convert_framework.add_parser('caffe')
    subparser_convert_caffe = get_argsparser_caffe(subparser_convert_caffe)
    subparser_convert_caffe.add_argument("--config", "-c", type=str, default=None, help="config file path for calibration")

    from jdsk.simulator.test import get_argsparser_test
    subparser_simulate = subparsers.add_parser('simulate')
    subparser_simulate = get_argsparser_test(subparser_simulate)

    subparser_helper = subparsers.add_parser('helper')
    # add subparser for different features
    subparser_helper_feature = subparser_helper.add_subparsers(dest='feature', help='')
    # add feature: check_precision
    from jdsk.helper.check_precision import get_argsparser_precision
    subparser_helper_precision = subparser_helper_feature.add_parser('precision')
    subparser_helper_precision = get_argsparser_precision(subparser_helper_precision)
    # add feature: show_npfile
    from jdsk.helper.cnpy_helper import get_argsparser_cnpy
    subparser_helper_npfile = subparser_helper_feature.add_parser('npfile')
    subparser_helper_npfile = get_argsparser_cnpy(subparser_helper_npfile)
    # add feature: show_detail
    from jdsk.helper.model_helper import get_argsparser_detail
    subparser_helper_detail = subparser_helper_feature.add_parser('info')
    subparser_helper_detail = get_argsparser_detail(subparser_helper_detail)
    # add feature: create_test_data
    from jdsk.helper.create_test_dir import get_argsparser_tensor_proto
    subparser_helper_test_data = subparser_helper_feature.add_parser('test')
    subparser_helper_test_data = get_argsparser_tensor_proto(subparser_helper_test_data)

    return parser


def main():
    parser = get_args_parser()

    import sys
    if 1 == len(sys.argv):
        parser.print_help()
    else:
        args = parser.parse_args()
        if args.command == "convert":
            if args.framework == "onnx":
                from jdsk.converter.onnx2jdsk import convert
            elif args.framework in ["tf1", "tf2"]:
                from jdsk.converter.tf2jdsk import convert
            elif args.framework == "paddle":
                from jdsk.converter.paddle2jdsk import convert
            elif args.framework == "caffe":
                from jdsk.converter.caffe2jdsk import convert
            else:
                subparsers = parser._get_positional_actions()[0]
                subparsers.choices['convert'].print_help()
                sys.exit(1)
                #raise RuntimeError("Unsupported framework {}".format(args.framework))
            convert(args)
        elif args.command == "simulate":
            from jdsk.simulator.test import test as simulate
            simulate(args)
        elif args.command == "helper":
            if args.feature == "precision":
                from jdsk.helper.check_precision import check_precision as feature
            elif args.feature == "npfile":
                from jdsk.helper.cnpy_helper import show_npfile as feature
            elif args.feature == "info":
                from jdsk.helper.model_helper import show_detail as feature
            elif args.feature == "test":
                from jdsk.helper.create_test_dir import create_test_data as feature
            else:
                subparsers = parser._get_positional_actions()[0]
                subparsers.choices['helper'].print_help()
                sys.exit(1)
                #raise RuntimeError("Unsupported feature {}".format(args.feature))
            feature(args)
        else:
            pass


if __name__ == "__main__":
    import sys, os
    parent = os.path.dirname(os.path.realpath(__file__))
    sys.path.append(os.path.join(parent, ".."))

    main()
