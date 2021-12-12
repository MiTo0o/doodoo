from setuptools import setup

setup(
  name="doodoo",
  version="0.02",
  description="The new pop(0)",
  url="https://github.com/MiTo0o",
  author="MiTo",
  author_email="derzanchiang1800@gmail.com",
  license="MIT",
  packages=["doodoo"],
  zip_safe=False,
  long_description="""
# doodoo
________
Don't like using .pop(0) because it looks weird? .pop(0) feels weird to
type out for a queue?

LOOK NO FURTHER

The doodoo package contains a poop() function which does the same thing as
.pop(0). BUTTTTTTT since your digestive system is basically a queue (First
In First Out) it only makes sense to use poop(queue) instead of queue.pop(0)
  """,
  long_description_content_type='text/markdown'
)