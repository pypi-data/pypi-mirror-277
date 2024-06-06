import argparse


def get_argsparser_onnx(parser = None, epilog = None):
    """Parse commandline."""
    if parser is None:
        parser = argparse.ArgumentParser(description="Toolkit to convert onnx graphs to {}(version {}).".format("JDSK", "0.0.2"),
                                         formatter_class=argparse.RawDescriptionHelpFormatter, epilog=epilog)
    parser.add_argument("--input", type=str, required=True, help="input onnx model path")
    parser.add_argument("--output", type=str, required=True, help="output jdsk model path")
    parser.add_argument("--checker", help="enable onnx.checker.check_model", action="store_true")
    parser.add_argument("--onnxsim", help="enable onnxsim(https://github.com/daquexian/onnx-simplifier) to simplify the onnx model", action="store_true")
    parser.add_argument("--verbose", "-v", default=0, help="verbose message, option is additive", action="count")
    # Experimental: extract subgraph or override input/output shapes(to convert graph from dynamic to static mostly)
    parser.add_argument("--inputs", type=str, default=None, help="expected input tensor names with shapes(option)")
    parser.add_argument("--outputs", type=str, default=None, help="expected output tensor names with shapes(option)")
    parser.add_argument("--free_dim_param", "-f", type=str, nargs='+', default=[], help="[dimension_name:override_value] specify a value(must > 0) to override a free dimension by name(dim.dim_param).")
    parser.add_argument("--free_dim_denotation", "-F", type=str, nargs='+', default=[], help="[dimension_denotation:override_value] specify a value(must > 0) to override a free dimension by denotation(dim.denotation).")
    return parser


def get_argsparser_tf(parser = None, epilog = None):
    """Parse commandline."""
    if parser is None:
        parser = argparse.ArgumentParser(description="Toolkit to convert tensorflow graphs to {}(version {}).".format("JDSK", "0.0.1"),
                                         formatter_class=argparse.RawDescriptionHelpFormatter, epilog=epilog)
    parser.add_argument("--input", type=str, help="input from graphdef")
    parser.add_argument("--graphdef", type=str, help="input from graphdef")
    parser.add_argument("--saved-model", type=str, help="input from saved model")
    parser.add_argument("--tag", type=str, help="tag to use for saved_model")
    parser.add_argument("--signature_def", type=str, help="signature_def from saved_model to use")
    parser.add_argument("--concrete_function", type=int, default=None,
                        help="For TF2.x saved_model, index of func signature in __call__ (--signature_def is ignored)")
    parser.add_argument("--checkpoint", type=str, help="input from checkpoint")
    parser.add_argument("--keras", type=str, help="input from keras model")
    parser.add_argument("--tflite", type=str, help="input from tflite model")
    parser.add_argument("--tfjs", type=str, help="input from tfjs model")
    parser.add_argument("--large_model", default=False, help="use the large model format (for models > 2GB)", action="store_true")
    parser.add_argument("--output", type=str, required=True, help="output model file")
    parser.add_argument("--inputs", type=str, help="model input_names (optional for saved_model, keras, and tflite)")
    parser.add_argument("--outputs", type=str, help="model output_names (optional for saved_model, keras, and tflite)")
    parser.add_argument("--ignore_default", help="comma-separated list of names of PlaceholderWithDefault "
                                                 "ops to change into Placeholder ops")
    parser.add_argument("--use_default", help="comma-separated list of names of PlaceholderWithDefault ops to "
                                              "change into Identity ops using their default value")
    parser.add_argument("--rename-inputs", help="input names to use in final model (optional)")
    parser.add_argument("--rename-outputs", help="output names to use in final model (optional)")
    parser.add_argument("--use-graph-names", default=False, help="(saved model only) skip renaming io using signature names",
                        action="store_true")
    parser.add_argument("--opset", type=int, default=None, help="opset version to use for onnx domain")
    parser.add_argument("--dequantize", help="remove quantization from model. Only supported for tflite currently.",
                        action="store_true")
    parser.add_argument("--custom-ops", help="comma-separated map of custom ops to domains in format OpName:domain. "
                                             "Domain 'ai.onnx.converters.tensorflow' is used by default.")
    parser.add_argument("--extra_opset", default=None,
                        help="extra opset with format like domain:version, e.g. com.microsoft:1")
    parser.add_argument("--load_op_libraries", type=str,
                        help="comma-separated list of tf op library paths to register before loading model")
    #parser.add_argument("--target", default=",".join([]), choices=['rs4', 'rs5', 'rs6', 'caffe2', 'tensorrt', 'nhwc'],
    #                    help="target platform")
    parser.add_argument("--continue_on_error", default=False, help="continue_on_error", action="store_true")
    parser.add_argument("--verbose", "-v", default=0, help="verbose output, option is additive", action="count")
    parser.add_argument("--debug", default=False, help="debug mode", action="store_true")
    parser.add_argument("--output_frozen_graph", type=str, help="output frozen tf graph to file")
    # experimental
    parser.add_argument("--inputs-as-nchw", default=None, help="transpose inputs as from nhwc to nchw")
    parser.add_argument("--outputs-as-nchw", default=None, help="transpose outputs as from nhwc to nchw")
    return parser


def get_argsparser_caffe(parser = None, epilog = None):
    """Parse commandline."""
    if parser is None:
        parser = argparse.ArgumentParser(description="Toolkit to convert caffe graphs to {}(version {}).".format("JDSK", "0.0.1"),
                                         formatter_class=argparse.RawDescriptionHelpFormatter, epilog=epilog)
    parser.add_argument("--input", type=str, required=True, help="input caffe model path(basename)")
    parser.add_argument("--output", type=str, required=True, help="output jdsk model path")
    parser.add_argument("--verbose", "-v", default=0, help="verbose message, option is additive", action="count")
    return parser
