# Vistaprint Project
**Goal**: Recommendation system for customers based on their previous engagements with Vistaprint.
The goal is to create an improved relevant and personalized experience for customers.

## Paths to follow:
These questions act as guidelines as to how we can create a system
that is able to forecast the users needs, thereby creating a more
personalized experience:
* How does the customer interact with the product?
* What features are indicative of what a customer would interact with?
  (user features)
* What design traits or features are more popular than others?
  (design features)
* Combine user features(purchase patterns, etc.), design features,
  and interaction features to gain insight to personalizing the user
  experience.

These questions aid us in the design of this customer recommendation
system for Vistaprint.  

## Current Goals
* Categorize the ComboID's based on design features
* Find most important features
* Run PCA on features to determine principal components
* Run model with our principle components

## Trouble-Shooting Technical Problems
These notes are for problems and solutions encountered with
our software tools. We primarily would use Spyder in Anaconda,
but you are welcome to use any python or R interpreter.

First off, we need to access the data. The data is stored as a paraquet file, which is a good extension
for handling hugee datasets.

To open this:
* Go to your terminal
* Enter: `conda info --envs (displays list of anaconda environments)`
* Enter: `source activate [the name of your conda environment]`
* Once the environment is active. You would see the name next to the
command prompt.
* Enter: `update pandas`
* Once that is done, enter: `conda install pyarrow -c conda-forge`
* Once that is done, enter: `conda install fastparquet -c conda-forge`
