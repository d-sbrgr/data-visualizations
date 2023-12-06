"""
Builds the data story.
"""


def main():
    import os
    import sys
    import shutil
    import sphinx.cmd.build

    PATH_TRUNK = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    PATH_BUILD_ROOT = os.path.join(PATH_TRUNK, "data_story")

    backup = os.path.abspath(os.getcwd())
    try:
        os.chdir(PATH_BUILD_ROOT)

        os.environ["PYTHONPATH"] = os.path.join(PATH_TRUNK)

        shutil.rmtree(os.path.join(PATH_BUILD_ROOT, "_build"), True)

        sys.exit(
            sphinx.cmd.build.main(["-b", "html", PATH_BUILD_ROOT, "_build/html", "-W"])
        )
    finally:
        os.chdir(backup)


if __name__ == "__main__":
    main()

