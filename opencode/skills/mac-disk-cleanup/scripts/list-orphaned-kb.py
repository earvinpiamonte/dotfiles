#!/usr/bin/env python3
import json
import os
import sys

base = os.path.expanduser("~/Library/Application Support/kiro-cli/knowledge_bases")

for agent in os.listdir(base):
    agent_dir = os.path.join(base, agent)
    ctx_file = os.path.join(agent_dir, "contexts.json")

    if not os.path.isfile(ctx_file):
        continue

    with open(ctx_file) as f:
        active = set(json.load(f).keys())

    for d in os.listdir(agent_dir):
        if d == "contexts.json":
            continue

        if d not in active:
            print(os.path.join(agent_dir, d))
