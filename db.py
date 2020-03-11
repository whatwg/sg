#!/usr/bin/env python
import json
import sys


def validate(input):
    normalized = normalize_internal(input)
    if normalized != input:
        sys.stderr.write("Input is not normalized.\n")
        sys.exit(0)

def normalize_internal(input):
    db = json.loads(input)
    string = json.dumps(normalize_db(db), ensure_ascii=False, allow_nan=False, sort_keys=False, indent=2)
    return string + "\n"

def normalize(input):
    open("db.json", "w").write(normalize_internal(input))

def normalize_db(db):
    i = 0
    for workstream in db["workstreams"]:
        db["workstreams"][i] = normalize_workstream(workstream)
        i += 1

    i = 0
    for idea in db["ideas"]:
        db["ideas"][i] = normalize_workstream_standard_or_idea(idea)
        i += 1

    i = 0
    for reference in db["biblio"]:
        db["biblio"][i] = normalize_reference(reference)
        i += 1

    return db

def normalize_workstream(workstream):
    return {
      "id": workstream["id"],
      "name": workstream["name"],
      "scope": workstream["scope"],
      "editors": [normalize__person(editor) for editor in workstream["editors"]],
      "standards": [normalize_workstream_standard_or_idea(standard) for standard in workstream["standards"]]
    }

def normalize__person(editor):
    email = None
    if "email" in editor:
        email = editor["email"]
    return {
      "name": editor["name"],
      "email": email
    }

def normalize_workstream_standard_or_idea(document):
    return {
      "name": document["name"],
      "href": document["href"],
      "description": document["description"],
      "authors": [normalize__person(author) for author in document["authors"]],
      "reference": document["reference"]
    }

def normalize_reference(reference):
    output = {
      "title": reference["title"],
      "href": reference["href"],
      "authors": [normalize__person(author) for author in reference["authors"]],
      "reference": reference["reference"]
    }
    if "obsoletedBy" in reference:
        output["obsoletedBy"] = reference["obsoletedBy"]
    return output


def usage():
    sys.stderr.write(
        """Usage: %s [command]

Commands:

* validate  -- Checks that db.json is normalized.
* normalize -- Normalizes db.json.

""" % sys.argv[0]
    )
    sys.exit(0)

def main():
    command = None
    try:
        command = sys.argv[1]
    except IndexError:
        usage()

    if command not in ["validate", "normalize"]:
        usage()
    else:
        input = open("db.json", "r").read()
        if command == "validate":
            validate(input)
        elif command == "normalize":
            normalize(input)
        else:
            assert False, "Unreachable code."

main()
