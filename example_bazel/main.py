import logging

from sematic import CloudResolver

from example_bazel.pipeline import pipeline

logging.basicConfig(level=logging.INFO)

if __name__ == "__main__":
    pipeline().resolve(CloudResolver())
