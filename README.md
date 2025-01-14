# Example Bazel-based Sematic pipeline

This repo is an example of how to use the `sematic_pipeline` Bazel rule.

See the [Sematic
documentation](https://docs.sematic.dev/cloud-execution/container-images#bazel)
for more details.

## Usage

In this repo, the following should run a remote pipeline (given all steps in
the docs have been completed):

```
$ bazel run //example_bazel:main
```

## Requirements
To update requirements, first update requirements.in and then use:

```
$ bazel run //:requirements.update
```

