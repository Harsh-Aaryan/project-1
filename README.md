# Programming assignment 01
Generate the hailstone sequence according to the [Collatz function](https://en.wikipedia.org/wiki/Collatz_conjecture)

### Problem description
Write a function that generates a sequence of integers according to the Collatz function for a given input.
Examine how your algorithm works and speed it up to beat my implementation!  
Note: stop when your algorithm reaches 1, as continuing creates an infinite loop.

### inputs
A list of integers to generate the hailstone sequence for.

### outputs
The sequence of integers generated by the Collatz function for a given input. Including the initial input and the final output of 1.  
Example: 
```py
collatz_verifier([1, 2, 5])
'[[1], [2, 1], [5, 16, 8, 4, 2, 1]]'
```

### Submitting the assignment
All you have to do is `git add`, `git commit`, and `git push` your code!

### Running the autograder
See graph slide deck for links! Below are your options for running the autograder.

Option 1) Use Docker (If you are ssh'ing into the campus machines, you have to do this)  
If you are on Windows or your own linux install, it may just be easiest to run the docker container with the following command (after you install docker): `sudo docker run --interactive --tty --rm --mount type=bind,source="$(pwd)"/,target=/your_code git-docker-classes.mst.edu/containers/container nu`  
Your code is in the `your_code` directory.  
Note that you will have to remove `sudo` for windows

If you are on a non-x86_64 processor (ie M1, M2, etc. Macs) you have to build the docker image locally. Enter the `container` directory and execute

`sudo docker build --tag container .`

Then, you can run the image you built locally.
From the root directory of your assignment Git repository,
or any directory you would like to mount in a container, execute:
`sudo docker run --interactive --tty --rm --mount type=bind,source="$(pwd)"/,target=/your_code container nu`  
Your files will be mounted inside the container,
in the following directory:
`cd your_code/`

If you are on a campus linux machine follow these steps:  
If you use `ssh` (via putty or otherwise) to access the campus Linux machines,
then you will need to run a rootless container option.
First type `cd` to head to your home directory, then type:

`singularity shell docker://git-docker-classes.mst.edu/containers/container`

or:

`apptainer shell docker://git-docker-classes.mst.edu/containers/container`

After that, your entire home directory should be accessible from the container.

Option 2) Use a VM  
Review this page from Dr. Taylor's website: https://www.cnsr.dev/index/Classes/DataStructuresLab/Content/00-VirtualMachines.html
Download some sort of virtualization software such as VirtualBox. Next, download a linux distribution .iso file such as https://labs.fedoraproject.org/en/security/. Next create a virtual machine, install fedora on it, install git, clone the repo, and start the assignment. This seems like a good guide https://itsfoss.com/install-fedora-in-virtualbox/

Option 3) Use the browser
This is the unofficial and less educational way to complete the assignment. Since it is a small assignment it will probably work well, but will likely be annoying for you. If this is the way you want to go, just: open the collatz_verifier.py file, click edit in IDE in top right, make your changes, and press commit to main in the bottom left.



### code specifications
Your function should not accept input via std-io nor produce output via std-io. 
Instead, leave that job for main.

# General information regarding this repository

## Coding
Tips for coding.

### What to name my files?
We give you empty files corresponding to those you should complete!

### Where to code?
We assume you're on a Linux machine, and can install all the software needed by this auto-grader.
We also have a docker container for you.
See the syllabus for more details.

### How to get this code?
Find the blue botton that says "clone", on the home page of this repository.

If you have an ssh key set up:
`git clone --recurse-submodules git@...`

If you don't have an ssh set up, or know what that is:
`git clone --recurse-submodules https://..`

### Where to read this file?
This file is nicely displayed in the Gitlab web interface, but you can read it wherever.

### What to install?
See the script's warnings.

### How to code?
Using this script, we strongly encourage you to program incrementally. 
Program code required by the unit tests, in the requested order. 
In general, don't procede to a later function if you are not passing the first one.
If you get stuck, instead of moving on, get help!
See the syllabus for extended coding tips.

## Auto-grader
### How to run the auto-grader on your machine?
Run the following in the root directory of your repository:
`./grade.sh`

## How to run the auto-grader on Gitlab-CI?
Make sure all your files are added, committed, and pushed to the appropriate branch (see Git section below).
Navigate to the Gitlab web interface to confirm these changes exist on the server.

## How to make sure I'm getting points?
* Click on CI/CD -> Jobs -> the latest job.
* Is it passing, green, etc? 
* What grade does it say you have?
* Whatever grade the latest job says, is what we think you have!

## std-io tests: differences between your std-out and the desired std-out
See: `your_diffs/` and `your_outputs` to determine what went wrong. 
We run these diffs automatically, so you may not need to manually inspect these files.

## Unit tests: we're micromanaging your functions!
See the unit tests themselves, and run them in your favorite debugger:
`unit_tests/`

## Git
Git happens...

### add, commit, push
From within your git repository (folder), add, commit, and push all the non-generated files. 
This means add your cpp and png files, but not a.out, etc.
Verify you can see the files on git-classes in the web interface.
If you can see the correct files on git-classes in your master branch, your submission is complete.
Make sure all the requested files are in the root directory of the repository unless otherwise specified.

## Errors
You should not change any of the grading files themselves. 
If you do, you will see a warning, and it will give you a 0.
If you accidentally did that:
`git checkout firstfourcharactersoflastcommitbyus graderfileyoubroke`

### Is the auto-grader broken?
Is the error you're encountering our fault or yours?
Either may be possible, while the latter is a bit more likely.
Double-check all the diffs, and step through all code to see.
If you think you found a bug, please let us know!

## When is this due?
See the syllabus!

## grade.sh: this automated grading framework
For more details on the generalized auto-grader, see:
https://gitlab.com/classroomcode/grade-sh/grade-sh
