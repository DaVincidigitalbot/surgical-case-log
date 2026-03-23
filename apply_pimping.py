#!/usr/bin/env python3
"""Merge all pimping question files and apply to procedures.json"""
import json
import importlib.util
import sys

def load_module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m

# Load all question sources
m1 = load_module('q1', 'pimping_questions.py')
m2 = load_module('q2', 'pimping_q2.py')
m3 = load_module('q3', 'pimping_q3.py')
m4 = load_module('q4', 'pimping_q4.py')

# Merge all questions (later files override earlier for duplicates)
ALL_Q = {}
ALL_Q.update(m1.QUESTIONS)
ALL_Q.update(m2.QUESTIONS2)
ALL_Q.update(m3.Q3)
ALL_Q.update(m4.Q4)

print(f"Total question sets loaded: {len(ALL_Q)}")

# Validate all have exactly 5 questions
for name, qs in ALL_Q.items():
    if len(qs) != 5:
        print(f"WARNING: {name} has {len(qs)} questions (expected 5)")

# Load procedures.json
with open('procedures.json') as f:
    procedures = json.load(f)

print(f"Total procedures in JSON: {len(procedures)}")

# Apply questions
applied = 0
missing = []
for proc in procedures:
    name = proc['name']
    if name in ALL_Q:
        proc['pimpingQuestions'] = ALL_Q[name]
        applied += 1
    else:
        missing.append(name)

print(f"Applied questions to: {applied} procedures")
print(f"Missing questions for: {len(missing)} procedures")

if missing:
    print("\nMissing procedures:")
    for m in missing:
        print(f"  - {m}")

# Write back
with open('procedures.json', 'w') as f:
    json.dump(procedures, f, indent=2, ensure_ascii=False)

print(f"\nSuccessfully wrote procedures.json with pimping questions!")

# Final stats
with_q = sum(1 for p in procedures if 'pimpingQuestions' in p and p['pimpingQuestions'])
without_q = sum(1 for p in procedures if 'pimpingQuestions' not in p or not p['pimpingQuestions'])
print(f"Procedures WITH questions: {with_q}")
print(f"Procedures WITHOUT questions: {without_q}")
