load("@rules_sematic//:pipeline.bzl", "sematic_pipeline")
load(
    "@rules_python//python:defs.bzl",
    "py_library",
)
load("@dependencies//:requirements.bzl", "requirement")

py_library(
    name = "main_lib",
    srcs = [
        "main.py",
        "pipeline.py",
    ],
    deps = [
        requirement("sematic"),
    ],
)

sematic_pipeline(
    name = "main",
    registry = "<your-container-registry>",
    repository = "<your-container-repo>",
    deps = [
        ":main_lib",
    ],
)
