import logging

from sematic import CloudRunner

from example_bazel.pipeline import pipeline

logging.basicConfig(level=logging.INFO)

if __name__ == "__main__":
    pipeline().resolve(CloudRunner())
