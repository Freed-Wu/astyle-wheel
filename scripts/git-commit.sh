#!/usr/bin/env bash
cd "$(dirname "$(readlink -f "$0")")/.." || exit 1

version="$(curl 'https://gitlab.com/api/v4/projects/41218592/repository/tags?per_page=1' | jq -r '.[].name')"
perl -pi -e's/(?<=^version = ")[^"]+(?="$)/'"$version/" pyproject.toml
[ -n "$(git diff)" ] || exit
perl -pi -e's/(?<=^    rev: )\S+/'"$version/" README.md
perl -pi -e's/(?<=^set\(VERSION )\S+)/'"$version/" CMakeLists.txt

git add pyproject.toml README.md CMakeLists.txt
git config --global user.name 'Github Actions'
git config --global user.email '41898282+github-actions[bot]@users.noreply.github.com'
git commit -m ":bookmark: Dump version to $version"
git tag "$version"
git remote set-url origin "https://x-access-token:$GH_TOKEN@github.com/$GITHUB_REPOSITORY"
git push
git push --tags
