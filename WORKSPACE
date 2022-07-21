workspace(name = "example_bazel")

load("@bazel_tools//tools/build_defs/repo:http.bzl", "http_archive")

## PYTHON RULES

http_archive(
    name = "rules_python",
    sha256 = "9fcf91dbcc31fde6d1edb15f117246d912c33c36f44cf681976bd886538deba6",
    strip_prefix = "rules_python-0.8.0",
    url = "https://github.com/bazelbuild/rules_python/archive/refs/tags/0.8.0.tar.gz",
)

## Canonical host toolchain

load("@rules_python//python:repositories.bzl", "python_register_toolchains")

python_register_toolchains(
    name = "python3_9",
    python_version = "3.9",
)

load("@python3_9//:defs.bzl", "interpreter")
load("@rules_python//python:pip.bzl", "pip_parse")

pip_parse(
    name = "dependencies",
    python_interpreter_target = interpreter,
    requirements_lock = "//:requirements.txt",
)

load("@dependencies//:requirements.bzl", "install_deps")

install_deps()

http_archive(
    name = "io_bazel_rules_docker",
    sha256 = "b1e80761a8a8243d03ebca8845e9cc1ba6c82ce7c5179ce2b295cd36f7e394bf",
    urls = ["https://github.com/bazelbuild/rules_docker/releases/download/v0.25.0/rules_docker-v0.25.0.tar.gz"],
)

load(
    "@io_bazel_rules_docker//repositories:repositories.bzl",
    "repositories",
)

repositories()

load("@bazel_tools//tools/build_defs/repo:git.bzl", "git_repository")

git_repository(
    name = "rules_sematic",
    branch = "neutralino1/kubernetes-execution",
    remote = "git@github.com:sematic-ai/sematic.git",
    strip_prefix = "bazel",
)

load("@rules_sematic//:pipeline.bzl", "base_images")

base_images()
