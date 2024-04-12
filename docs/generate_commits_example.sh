#!/bin/bash

cd /path/to/my/project
git --no-pager log --pretty=format:"%C(cyan)%C(bold)%cd %C(reset)%s %b" --date=format:'%Y-%m-%d' --since "Feb 17 2024" > /path/to/my/output.txt