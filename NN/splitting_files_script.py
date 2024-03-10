import splitfolders

parent_path = 'Dataset'

splitfolders.ratio(parent_path, output="splittedfolder", seed=213, ratio=(.8, .1, .1))