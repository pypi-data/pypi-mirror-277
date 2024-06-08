#!/usr/bin/env python3
import os
import re
import sys
import shutil
import argparse

def progstring(x):
    edge = len(x) - len(x.lstrip())
    x = x.split("\n")
    for idx, _ in enumerate(x):
        x[idx] = x[idx][edge-1:]
    return "\n".join(x)

def stubwheel(args):
    os.makedirs('temp', exist_ok=True)
    stub = \
        f"""
        from setuptools import setup, find_packages
        setup(
            name='{args.name}',
            version='{args.version}',
            url='{args.url}',
            author='{args.author}',
            author_email='{args.email}',
            description='{args.desc}',
            long_description='{args.name} {args.desc}',
            long_description_content_type='text/markdown'
        )
        """
    stub = progstring(stub)
    with open(f"temp/setup.py", 'w') as f:
        f.write(stub)
    os.system("cd temp && python setup.py sdist bdist_wheel && twine check dist/* && twine upload dist/*")
    shutil.rmtree('temp')

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--name',    type=str, required=True,   help='package name (required)')
    parser.add_argument('--version', type=str, default='0.0.0', help='package version (optional)')
    parser.add_argument('--url',     type=str, default='',      help='package url (optional)')
    parser.add_argument('--author',  type=str, default='',      help='author name (optional)')
    parser.add_argument('--email',   type=str, default='',      help='author email (optional)')
    parser.add_argument('--desc',    type=str, default='',      help='package description (optional)')
    args = parser.parse_args()
    stubwheel(args)

if __name__ == "__main__":
    sys.exit(main())