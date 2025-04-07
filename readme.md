## desc

creates, maintains, and modifies a user's contact list through the command line and a json file.

this is a python remake of a C++ program I made a few years ago.

## requirements

- python3

## to run

- clone the repo
- then in the root of repo:

```bash
cd contacts
python contacts_main.py
```

## to test
- in the root of the dir, run:

```bash
python -m unittest discover tests
```

## to do
- add contact type selection, so there;s no user input
- add regex to make sure that it's a valid email
- add a char limit on all inputs
- add a "date added" field
- add a "date last modified" field
- add an optional birthday thing
- add functioning edit contact menu
- add separate class for input validation