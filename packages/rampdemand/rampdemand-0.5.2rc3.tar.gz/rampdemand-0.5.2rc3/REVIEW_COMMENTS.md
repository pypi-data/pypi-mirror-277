Reviewer 1
The readme proposes to create a python environment with python=3.8. This python version is soon outdated. Is the software supporting newer python versions? If yes, I would suggest updating the python version in the Readme.

--> PR merged, waiting for reviewer OK

After having followed the installation instructions, which work fine, I had a look at the example at https://github.com/RAMP-project/RAMP?tab=readme-ov-file#building-a-model-with-a-python-script. What I find confusing is that I cannot display the household_1 object. The error message is clear (there are no appliances), but for newbies this might be confusing. Also empty objects which seems to be that basic to the whole software should be displayable.

--> PR merged, waiting for reviewer OK



Reviewer 2
1. In the "Using real calendar days to generate profiles" example, it walks through how to use the CLI to generate a number of profiles. I tried to use the excel file generated from the "Using tabular inputs to build a model" as an input, but received a matplotlib error for the second plot. The command I ran and the error I received is shown below. I can attach the full trace back if that helps. Not sure if I am just misunderstanding what my input file should be?

$ ramp -i example_excel_usecase.xlsx -n 10
ValueError: x and y must have same first dimension, but have shapes (1440,) and (1,)

--> easy fix, but using the old_post_process is a bit annoying

- `Profile_formatting`, `Profile_cloud_plot` and `Profile_series_plot` are used in the example files, in `old_post_process`, and in `parallel_processing.ipynb`
- `export_series` is only used in `old_post_process`
- `old_post_process` is only used in `run_usecase`

--> PR almost done



I couldn't find where package dependencies are listed. When I tried to run tests, I got a ModuleNotFoundError: No module named 'scipy' error. The only place I saw dependences was in the ramp/__init__.py file, but scipy is not listed. If I pip install scipy into my environment and run pytest tests/ I get a ModuleNotFoundError: No module named 'nbconvert'. I had to pip install nbconvert as well to get tests to run. Clarifying the dependencies for using vs. developing would help!

--> tests/requirements.txt is there

If I run tests (with the extra pip installs), I get one failure:

FAILED tests/test_switch_on.py::TestRandSwitchOnWindow::test_coincidence_normality_on_peak - AssertionError: The 'coincidence' values are not normally distributed.

assert 0.029748765751719475 > 0.05

--> look into stochastic testing



Fabian Hoffman


General checks

    Some of the authors do not appear in the contributions list of the Github repository. Could you clarify their role? https://github.com/RAMP-project/RAMP/graphs/contributors

    --> addressed by Flomb, reviewer did not mention if it was ok

    JOSS asks for reproducibility of the figure in the paper (Data Sharing & Reproducibility). Is the code online somewhere? I could not see it in the joss_paper branch of the repo.

    --> in review PR 149, reviewer not notified yet

Functionality

    1 The readme proposes to create a python environment with python=3.8. This python version is soon outdated. Is the software supporting newer python versions? If yes, I would suggest updating the python version in the Readme.

    --> in review PR 123, merged, waiting for OK of reviewer

    2 After having followed the installation instructions, which work fine, I had a look at the example at https://github.com/RAMP-project/RAMP?tab=readme-ov-file#building-a-model-with-a-python-script. What I find confusing is that I cannot display the household_1 object. The error message is clear (there are no appliances), but for newbies this might be confusing. Also empty objects which seems to be that basic to the whole software should be displayable.

    --> in review PR 122, merged, waiting for OK of reviewer

Documentation

The Readthedocs documentation is great with all its examples. Two minor remarks.

    1 there are some examples which do not have an intro at the beginning, like the fixed flat-appliance example. These are however very valuable to understand the context.

    --> in review PR 124, waiting for OK of reviewer

    2 the navigation on the left sidebar (with the partial TOC) is a bit counter-intuitive, I find. I am getting lost easily without knowing where I am. If you agree, I would suggest increasing the scope of the sidebar's TOC.

    --> in review PR 137, merged, waiting for OK of reviewer

    3. What is the test coverage of the project? Since there are not that many, it would be good to check that minimum coverage is realised.

    --> in review PR 136, waiting for OK of reviewer

Being made:
COVERALLS_REPO_TOKEN=U3Usaub3EU93XohuATzZ0BA7hkBZWR4Tp

    4. I cannot find a contribution guideline as required by JOSS.

    --> addressed by Flomb

Software paper

    The State of the field is not realised. It would be interesting what other alternative software is there and how it compares.

    --> still open, the only object opened from this reviewer

Trevor B

General Checks

    Same question as @FabianHofmann; is there code where I can reproduce Figure 1?

    --> in review PR 149, reviewer not notified yet

    Your reference of "Generating high-resolution multi-energy load profiles for remote areas with an open-source stochastic model" is a 2019 paper in Energy describing the first version of RAMP and validating its functionality, I believe? If so, can you please describe (high level) how this paper is different from the one mentioned? This doesn't necessarily need to go in the paper, just for my reference clarifying the differences please. (Sidenote; I know other packages like pyam are published in different journals - ORE and JOSS in that case - so Im not trying to attack this submission or anything! Just trying to understand the differences.)

    --> addressed by Flomb

Functionality

--> all done


Documentation

    1 In the Quick Start section, appliances are added through the method User.Appliance(...). Later on in the examples section, appliances are added through the method User.add_appliance(...). Based on the API reference, the Appliance(...) method should only be used for when working with legacy code? If users are encouraged to use the add_appliance(...) method, updating docs to reflect this would be good! (Same issue also appears in "Appliances with multiple cycles" example)

    --> PR 142, merged, OK of Reviewer :)


    2 I find it a little confusing how the documentation site contribution guidelines and file CONTRIBUTING.md in the repository don't match?

    --> https://github.com/RAMP-project/RAMP/pull/138, merged, OK of Reviewer :)

    3 It may be worth noting in the contributing guidelines that developers should follow Black formatting, and contributions will be checked for it with your actions (although, I do see you have the Black badge on the README.md). Alternatively, having a pre-commit file, or specifying in the contributing guidelines how to install Black in VSCode (or similar) to autolint contributions would be good!

    --> still needed to be done

    4 In contributions guidelines, it may be good to specify what to include in a new issue ticket and PR (or even create templates for these)? For example, for a new issue, do you want to know OS the user is running, version of RAMP they are running, ect.

    --> https://github.com/RAMP-project/RAMP/pull/135, merged, OK of Reviewer :)

    5 In contribution guidelines on the doc site, you mention contributors should perform qualitative testing only. On the repository CONTRIBUTING.md file, it mentions to also run tests via pytest. Please clarify what tests contributors should be running.

    --> RAMP-project/RAMP#129 (already merged, just need reviewer to confirm ok)

    6 At the bottom of the introduction page, there is a note that says "This project is under active development!". Can you please clarify what the active development means? Just want to ensure this does not mean we can't trust the results. (Sorry, I know this one is a little pedantic!)

    --> addressed by Flomb?

    7 The examples are great at walking the reader through the many different functions of RAMP! However, I think in the first example it would be beneficial to explicitly write out what all the different arguments in the User(...) and add_appliance(...) calls are doing. This can maybe be done through a top level description like in some of your other examples (as also suggested by @FabianHofmann). At first, especially for the add_appliance(...) method, it wasn't necessarily clear to me what the different arguments did. While I eventually did find the info I was looking for in the Appliance.__init__ API ref, this was not the first place I intuitively thought to look for the information (which was the add_appliance(...) method API ref).

      --> RAMP-project/RAMP#142, merged, OK of Reviewer :)

Software Paper

    1 I agree with @FabianHofmann; a comparison of similar software/tools is needed.

    --> still open

    2 Expanding on your sentence of RAMP "features several degrees of customisations" to explicitly describe some of these customizations would be great I think! For example, being able to generate different loads for different uses (EVs, hot water, cooking ect..) is a valuable point for readers, I believe.

    --> still open



# Reviewer one (FH)

## Software Paper

The State of the field is not realised. It would be interesting what other alternative software is there and how it compares.

--> still open, the only object opened from this reviewer

# Reviewer 2 (TB)

## Documentation

3. It may be worth noting in the contributing guidelines that developers should follow Black formatting, and contributions will be checked for it with your actions (although, I do see you have the Black badge on the README.md). Alternatively, having a pre-commit file, or specifying in the contributing guidelines how to install Black in VSCode (or similar) to autolint contributions would be good!

--> still needed to be done by PF


6. At the bottom of the introduction page, there is a note that says "This project is under active development!". Can you please clarify what the active development means? Just want to ensure this does not mean we can't trust the results. (Sorry, I know this one is a little pedantic!)


## Software Paper

1. I agree with @FabianHofmann; a comparison of similar software/tools is needed.

--> still open

2. Expanding on your sentence of RAMP "features several degrees of customisations" to explicitly describe some of these customizations would be great I think! For example, being able to generate different loads for different uses (EVs, hot water, cooking ect..) is a valuable point for readers, I believe.

--> still open


TODO anyways --> update CHANGELOG

1)
Make a release branch out of joss-paper (or just update the files there),
Then release it and merge into main.

Once done, rebase develop onto joss-paper/release branch so that all the commits made in the meantime appear made afterwards

2) Rebase joss-paper onto developp (only conflicts in multi-cycle ipynb --> already solved), check tests pass locally and everything

Advantage: 
- this saves us the work of making another small release after the joss one
- there are some bugfixes (list them)
Disadvantage: this includes commits which were not reviewed by joss