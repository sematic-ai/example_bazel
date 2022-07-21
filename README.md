# Example repo for the `sematic_pipeline` Bazel rule

This repo is an example of how to use the `sematic_pipeline` Bazel rule.

See the [Sematic
documentation](https://docs.sematic.dev/execution-modes#dependency-packaging)
for more details.

## Usage

In this repo, the following should run a remote pipeline (given all steps in
docs have been completed):

```
$ bazel run //example_bazel:main
```