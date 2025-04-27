#!/usr/bin/env -S perl -pi
BEGIN {
    exit if scalar @ARGV == 0;
    $version =
`curl 'https://gitlab.com/api/v4/projects/41218592/repository/tags?per_page=1' | jq -r '.[].name'`;
    chomp $version;
}

s/(?<=^    rev: )\S+/$version/;
s/(?<=^set\(VERSION )\S+/$version/;
s/(?<=astyle==)[^"]+/$version/;
s/(?<=version = ")[^"]+/$version/;
s/(?<=^          tagging_message: )\S+/$version/;
