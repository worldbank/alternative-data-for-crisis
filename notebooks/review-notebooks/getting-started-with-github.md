# GitHub Quickstart


GitHub is a web-based platform used for version control using [Git](https://git-scm.com/). It allows multiple people to collaborate on projects, track changes, and manage code. This guide will help you get started with GitHub, covering the basics of creating repositories, committing changes, and collaborating with others.



[GitHub](https://github.com/) welcomes the largest open source communities in the world, with projects like [pandas](https://github.com/pandas-dev/pandas/), [scikit-learn](https://scikit-learn.org/stable/), [PyTorch](https://pytorch.org/), [TensorFlow](https://www.tensorflow.org/) and many more. With over 40 millions, GitHub gained such an important position thanks to its amazing collaboration tools and technologies build on top of [git](https://git-scm.com/).


GitHub is a web-based platform used for version control using Git. It allows multiple people to collaborate on projects, track changes, and manage code. This guide will help you get started with GitHub, covering the basics of creating repositories, committing changes, and collaborating with others.


# GitHub Quickstart Guide

## Introduction
This guide will help you get started with GitHub, covering the basics of setting up a GitHub Account and cloning the course repository.

## Prerequisites

Before you begin, ensure you have the following:
- A GitHub account. You can create one at [GitHub](https://github.com).
- Git installed on your local machine. You can download it from [Git](https://git-scm.com).

## Setting Up Git

### Configuring Git

After installing Git, you need to configure it with your GitHub account. Open your terminal or command prompt and run the following commands:

```sh
git config --global user.name "Your Name"
git config --global user.email "your-email@example.com"
```

## Cloning a Repository
Our course is stored on a GitHub repository on `remote`. In order to have a copy of it on your `local` machine, you need to clone it from the `remote` to `local`

1. Open the terminal/command line and navigate to the path where you want to store the course material
2. Go to `https://github.com/worldbank/alternative-data-for-crisis`, press `code` button and copy the link for cloning 
that fits your needs. 
```{figure} ../images/clone_repo.png
---
width: 700
name: clone_repo
---
How to obtain the link for clonning a repository
``` 
3. Go back to the command line, execute the below code and follow the instructions
```commandline
git clone "repository-link"
```
4. You are all set!





```{seealso}
- [Introduction to Git and GitHub](https://raw.githubusercontent.com/worldbank/DIME-Resources/master/git-2-github.pdf)
- [Using Git and GitHub](https://raw.githubusercontent.com/worldbank/DIME-Resources/master/git-3-flow.pdf)
- [Maintaining a GitHub repository](https://raw.githubusercontent.com/worldbank/DIME-Resources/master/git-4-management.pdf)
- [Initializing and Synchronizing a Git Repo with GitHub Desktop](https://raw.githubusercontent.com/worldbank/DIME-Resources/master/onboarding-3-git.pdf)
- [Using Git Flow to Manage Code Projects with GitKraken](https://raw.githubusercontent.com/worldbank/DIME-Resources/master/onboarding-4-gitflow.pdf)
```