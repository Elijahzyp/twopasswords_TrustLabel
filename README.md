# twopasswords' Trustee Percentiles

Note: This is a forked repo. The original repo is [here](https://github.com/gennadis/twopasswords).
*Data as of January 31, 2024*

<center><img src="./images/grade_f.svg" width="100px" height="100px"></center>

-- Above grade is based on the percentile rankings of the 4 repo scores below, which are compared with the top 1000 most-downloaded npm libraries.

<details>
<summary><span style="font-size: 20px;"><strong>Maintenance -- </strong>Beats <strong><span style="color: blue;">15.8%</span></strong> Other Repos</summary>
<div>
<div align=center>
  <img src="./images/twopasswords/maintenance.png" width="500px" height="180px">
</div>
Activity and involvement by this project’s maintainer(s). Maintainers could increase these metrics by extending documentation and being more responsive to community participation (especially issues and PRs).<br><br>
</div>
<table>
  <tr>
    <td>
      <div>
        <strong>Issues Maintenance:</strong> Top 0.0 Percentile
        <p>How efficiently issues are addressed: issues closed and comments on issues.</p>
      </div>
      <div>
        <strong>Community Documentation:</strong> Top 38.9 Percentile
        <p>Support for the community to participate: issue and PR templates, code of conduct, governance, etc.</p>
      </div>
    </td>
    <td>
      <div>
        <strong>Code Maintenance:</strong> Top 0.0 Percentile
        <p>How efficiently code changes are addressed: commits and PRs closed, commit standards.</p>
      </div>
      <div>
        <strong>Maintainer History:</strong> Top 24.2 Percentile
        <p>Maintainer experience: maintainers' other projects</p>
      </div>
    </td>
  </tr>
</table>
</details>


<details>
<summary><span style="font-size: 20px;"><strong>Contribution -- </strong>Beats <strong><span style="color: blue;">0.0%</span></strong> Other Repos</summary>
<div>
<div align=center>
  <img src="./images/twopasswords/contribution.png" width="500px" height="180px">
</div>
Activity and involvement by this project’s contributors. Fostering and encouraging more contribution and participation would increase these metrics.<br><br>
</div> 
<table>
  <tr>
    <td>
      <div>
        <strong>Code Contribution:</strong> Top 0.0 Percentile
        <p>Activity to add to the codebase: commits and PRs.</p>
      </div>
      <div>
        <strong>Contributor Participation:</strong> Top 0.0 Percentile
        <p>Activity in discussion and participation: number of contributors, comments made, quality of comments.</p>
      </div>
    </td>
    <td>
      <div>
        <strong>Contributor Growth:</strong> Top 0.0 Percentile
        <p>How the project is scaling in size: change in contributors, PRs.</p>
      </div>
    </td>
  </tr>
</table>
</details>


<details>
<summary><span style="font-size: 20px;"><strong>Popularity -- </strong>Beats <strong><span style="color: blue;">7.5%</span></strong> Other Repos</summary>
<div>
<div align=center>
  <img src="./images/twopasswords/popularity.png" width="500px" height="180px">
</div>
Activity and usage by this project’s consumers. Spreading this project to more users and maintaining it over time increases these metrics.<br><br>
</div>  
<table>
  <tr>
    <td>
      <div>
        <strong>Stars and Watches:</strong> Top 6.3 Percentile
        <p>How much consumers follow this project: stargazers, watchers.</p>
      </div>
      <div>
        <strong>Forks:</strong> Top 0.6 Percentile
        <p>How much developers fork this project.</p>
      </div>
    </td>
    <td>
      <div>
        <strong>Downstream Dependents:</strong> Top 22.7 Percentile
        <p>For projects producing packages and dependencies, how many downstream projects rely on them.</p>
      </div>
      <div>
        <strong>Project Maturity:</strong> Top 0.3 Percentile
        <p>Size and age of repo: lines of code, creation time, versions.</p>
      </div>
    </td>
  </tr>
</table>
</details>


<details>
<summary><span style="font-size: 20px;"><strong>Code Quality -- </strong>Beats <strong><span style="color: blue;">3.0%</span></strong> Other Repos</summary>
<div>
<div align=center>
  <img src="./images/twopasswords/code_quality.png" width="500px" height="180px">
</div>
Security and review of the project’s code. Contributors can increase these metrics by maintaining the dependencies and setting up automated testing and procedural reviews.<br><br>
</div>   
<table>
  <tr>
    <td>
      <div>
        <strong>Dependencies Health:</strong> Top 11.5 Percentile
        <p>Mitigation of dependency vulnerability risk: dependency versions, reported vulnerabilities.</p>
      </div>
      <div>
        <strong>Review Coverage:</strong> Top 0.2 Percentile
        <p>Scale of manual code reviews: contributors and reviewers per code portion, commit sizes.</p>
      </div>
    </td>
    <td>
      <div>
        <strong>Testing Quality:</strong> Top 0.0 Percentile
        <p>Scale of automated tests: workflow runs, check runs, code authors.</p>
      </div>
    </td>
  </tr>
</table>
</details>



​																				[Metric Details](https://github.com/Elijahzyp/twopasswords_TrustLabel/blob/branch_mcpc/MCPC%20Template%20Metric%20Details.md)



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
