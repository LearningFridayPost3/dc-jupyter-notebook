# dc-jupyter-notebook

Changes compared to the last iteration:
* Fixed all internal links
* Changed external link for dataset. The old one was not valid anymore.
* Alert boxes do not work in colab --> Replaced them with icons and vertical lines.
* Section 3.2: Added description of int64 in comment.
* Section 3.4: Visualized train-test-split.
* Section: 4.1 The plot_tree() function expects the feature_names as a list --> Fixed.
* Section: 4.1 Set dpi=600 in plt.figure(). Otherwise resolution is too low.
* Section 4.1: Info Box --> "folgende Precision" replaced with "folgende Accuracy".
* Section 4.1: "drittletzten" replaced with "viertletzten".
* Section 4.1 and 4.2: Used same random_state = 0 for all decision tree instances. The first one had a random state of 42. Changed it to 0 --> Results changed a little bit and description of the results had to be adapted. Reason for setting the same random_state for all instances: comparability.
* Aufgabe 7: Access alpha_opt directly (from vector) instead of assigning a rounded value to alpha_opt. Otherwise the accuracy won't be the same as in the plot 'Accuracy vs alpha for training and testing sets'
