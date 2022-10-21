load("@rules_python//python/pip_install:requirements.bzl",  "compile_pip_requirements")

# requirements.update will compile requirements.in and put the result in requirements.txt
compile_pip_requirements(
    name="requirements",
    extra_args=["--allow-unsafe"],
    visibility = ["//visibility:private"],
    requirements_in = ":requirements.in",
    requirements_txt = ":requirements.txt",
)
