# twopasswords’ Trust Percentiles

Note: This is a forked repo. The original repo is [here](https://github.com/gennadis/twopasswords).
*Data as of January 31, 2024*

<center><img src="./images/grade_f.svg" width="100px" height="100px"></center>

-- Above grade is based on the percentile rankings of the 3 trust component scores below, which are compared with the top 1000 most-downloaded npm libraries.

<details>
<summary><span style="font-size: 20px;"><strong>Community Activity and Integrity -- </strong>Top <strong><span style="color: blue;">1.88</span></strong> Percentile</summary>
<div>
<center><img src="./images/twopasswords/community_activity_and_integrity_component.png" width="400px" height="180px"></center><br>
Activity and usage by this project’s consumers and contributors. More people using and contributing to this project increases these metrics.<br><br>
</div>
<div>
  <strong>Usage Popularity:</strong> Top 7.5 Percentile
  <p>How much consumers use this project: stars, watches, forks, downstream dependents.</p>
</div>
<div>
  <strong>Code Contribution:</strong> Top 0.0 Percentile
  <p>Activity to add to the codebase: commits and PRs.</p>
</div>
<div>
  <strong>Contributor Participation:</strong> Top 0.0 Percentile
  <p>Activity in discussion and participation: number of contributors, comments made, quality of comments.</p>
</div>
<div>
  <strong>Contributor Growth:</strong> Top 0.0 Percentile
  <p>How the project is scaling in size: change in contributors, PRs.</p>
</div>
</details>


<details>
<summary><span style="font-size: 20px;"><strong>Maintenance and Goodwill -- </strong>Top <strong><span style="color: blue;">15.77</span></strong> Percentile</summary>
<div>
<center><img src="./images/twopasswords/maintenance_and_goodwill_component.png" width="400px" height="180px"></center><br>
Activity and involvement by this project’s maintainer(s) for the benefit of the project community. Maintainers could increase these metrics by extending documentation and being more responsive to community participation (especially issues and PRs).<br><br>
</div> 
<div>
  <strong>Issues Maintenance:</strong> Top 0.0 Percentile
  <p>How efficiently issues are addressed: issues closed and comments on issues.</p>
</div>
<div>
  <strong>Community Documentation:</strong>  Top 38.9 Percentile
  <p>Support for the community to participate: issue and PR templates, code of conduct, governance, etc.</p>
</div>
<div>
  <strong>Code Maintenance:</strong> Top 0.0 Percentile
  <p>How efficiently code changes are addressed: commits and PRs closed, commit standards.</p>
</div>
<div>
  <strong>Maintainer History:</strong> Top 24.2 Percentile
  <p>Maintainer experience: maintainers' other projects</p>
</div>
</details>


<details>
<summary><span style="font-size: 20px;"><strong>Code Quality -- </strong>Top <strong><span style="color: blue;">3.0</span></strong> Percentile</summary>
<div>
<center><img src="./images/twopasswords/code_quality_component.png" width="400px" height="180px"></center><br>
Security and scalability of the project’s code. Contributors can increase these metrics by maintaining the dependencies and setting up automated testing and procedural reviews.<br><br>
</div>   
<div>
  <strong>Dependencies Health:</strong> Top 11.5 Percentile
  <p>Mitigation of dependency vulnerability risk: dependency versions, reported vulnerabilities.</p>
</div>
<div>
  <strong>Review Coverage:</strong> Top 0.2 Percentile
  <p>Scale of manual code reviews: contributors and reviewers per code portion, commit sizes.</p>
</div>
<div>
  <strong>Testing Quality:</strong> Top 0.0 Percentile
  <p>Scale of automated tests: workflow runs, check runs, code authors.</p>
</div>
<div>
  <strong>Project Maturity:</strong> Top 0.3 Percentile
  <p>Size and age of repo: lines of code, creation time, versions.</p>
</div>
</details>




​																				[Metric Details](https://github.com/Elijahzyp/twopasswords_TrustLabel/blob/main/Trust%20Percentiles%20Template%20Metric%20Details.md)


***




# TwoPasswords

[![Pypi](https://img.shields.io/pypi/v/pyvault.svg)](https://pypi.org/project/twopasswords)
[![MIT licensed](https://img.shields.io/badge/license-MIT-green.svg)](https://raw.githubusercontent.com/gennadis/twopasswords/main/LICENSE)

TwoPasswords is a simple Python password manager, that uses Face Recognition as a second factor.
It allows you to securely save account credentials with a simple TUI interface.

![Screenshot](Screenshot.png)


## Features
- Account credentials stored locally in an encrypted SQLite database with [SQLCipher](https://www.zetetic.net/sqlcipher/)
- Passwords can be passed to Clipboard
- Passwords can be generated in [XKCD style](https://xkcd.com/936/)
- Import and Export in JSON


## Basic Usage
To start using TwoPasswords, you have to register your face and enter your new Master Password.

## Installation notes
1. TwoPasswords requires `cmake` to be installed on your machine.
```bash
pip3 install cmake
```

2. TwoPasswords requires `sqlcipher` to be installed on your machine.

On MacOS, you can install it with [brew](https://brew.sh/):
```bash
brew install sqlcipher
pip3 install sqlcipher3==0.4.5

# If you are getting an error "Failed to build sqlcipher3", you would need to fix the build flags:
SQLCIPHER_PATH="$(brew --cellar sqlcipher)/$(brew list --versions sqlcipher | tr ' ' '\n' | tail -1)"
C_INCLUDE_PATH=$SQLCIPHER_PATH/include LIBRARY_PATH=$SQLCIPHER_PATH/lib pip3 install sqlcipher3==0.4.5
```

3. Also you need to install latest ffmpeg library for a latest OpenCV version
```bash
brew install ffmpeg
```


### Installing via PyPI

```bash
pip3 install twopasswords

# Run setup
twopasswords
```

### Installing via cloning this project

```bash
# Clone project
git clone https://github.com/gennadis/twopasswords.git 
cd twopasswords

# Installation
python3 setup.py install

# Run setup
twopasswords
```
