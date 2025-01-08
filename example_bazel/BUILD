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
    registry = "us-central1-docker.pkg.dev/core-400321/main",
    repository = "airtrain-pipeline",
    deps = [
        ":main_lib",
    ],
)
