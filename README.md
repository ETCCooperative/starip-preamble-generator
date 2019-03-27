# StarIP Preamble Generator

This repository contains the necessary toolings and scripts to generate a StarIP Preamble
that is encoded with Base58 hash.

## Getting Started

*Note*: This works only with Python3

You'll need to install the latest Python (3.6+)

You'll also need to install virtualenv for testing the script

You run the script via the following command:
```sh
python3 script.py
```

This will generate the following prompt in the command-line:

```
Welcome to the StarIP Preamble Generator! 🌟🌟🌟


Please Enter A Title For Your StarIP: Atlantis
Please Enter An Author Name For Your StarIP: Yaz Khoury 
Please Enter the Discussion Email For Your StarIP: yaz@etccooperative.org
Please Select A Status From Available Options: Draft | Last Call | Accepted | Final (non-Core) | Final (Core) | Deferred: Draft
Please Enter The Type For Your StarIP: Standard Track | Informational | Meta: Standard Track 
Please Enter A Date For Your StarIP In YYYY-MM-DD Format: 2019-03-27


The StarIP Preamble Has Been Generated:


Author: Yaz Khoury
Created: '2019-03-27'
Discussions-To: yaz@etccooperative.org
Reference-Hash: BgnS
StarIP-Name: ECIP-Atlantis-VArZBgnS
Status: Draft
Title: Atlantis
Type: Meta

Preamble Has Been Saved to preamble.yaml File
```

It generates a preamble.yaml file for you containing the preamble and shortened Base58 Hash 


## Issues

- Currently, it generates preamble in alphabetical order, needs to be fixed
- Must include inputs for `Precedes` and `Supersedes`, as well as link to discussions on the StarIP
- Entire hash must be saved somewhere
- Must be able to generate the hash from a YAML input
- CLI needs to be better organized so validation checks happen after each prompt, not after all prompts have been entered
- Docker container needs to be generated
- Web UI needs to be built
- Adhere to Pristine Documentation Guide
