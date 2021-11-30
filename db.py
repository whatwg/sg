#!/usr/bin/env python
import json
import sys


def validate(input):
    normalized = normalize_internal(input)
    if normalized != input:
        sys.stderr.write("Input is not normalized.\n")
        sys.exit(1)

def normalize_internal(input):
    db = json.loads(input)
    string = json.dumps(normalize_db(db), ensure_ascii=False, allow_nan=False, sort_keys=False, indent=2)
    return string + "\n"

def normalize(input):
    open("db.json", "w").write(normalize_internal(input))

def normalize_db(db):
    for (name, normalize_algorithm, sort_key) in [
            ("workstreams", normalize_workstream, "name"),
            ("ideas", normalize_workstream_standard_or_idea, "name"),
            ("biblio", normalize_reference, "title")
        ]:
        db[name] = normalize_list(db[name], normalize_algorithm, sort_key)
    return db

def normalize_list(input, normalize_algorithm, sort_key):
    output = [normalize_algorithm(item) for item in input]
    output.sort(key=lambda item: item[sort_key])
    return output

def normalize_workstream(workstream):
    return {
      "id": workstream["id"],
      "name": workstream["name"],
      "scope": workstream["scope"],
      "editors": normalize_list(workstream["editors"], normalize_person, "name"),
      "standards": normalize_list(workstream["standards"], normalize_workstream_standard, "name")
    }

def normalize_person(editor):
    return {
      "name": editor["name"],
      "email": editor.get("email", None)
    }

def normalize_workstream_standard(document):
    output = normalize_workstream_standard_or_idea(document)
    output["review_draft_schedule"] = document["review_draft_schedule"]
    output["twitter"] = document["twitter"]
    return output

def normalize_workstream_standard_or_idea(document):
    return {
      "name": document["name"],
      "href": document["href"],
      "description": document["description"],
      "authors": normalize_list(document["authors"], normalize_person, "name"),
      "reference": document["reference"]
    }

def normalize_reference(reference):
    output = {
      "title": reference["title"],
      "href": reference["href"],
      "authors": normalize_list(reference["authors"], normalize_person, "name"),
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
        input = open("db.json", "r", encoding="utf-8").read()
        if command == "validate":
            validate(input)
        elif command == "normalize":
            normalize(input)
        else:
            assert False, "Unreachable code."

main()
