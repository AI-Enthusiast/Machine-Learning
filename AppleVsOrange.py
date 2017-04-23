from sklearn import tree

# A data set of [a,b] where 'a' is the weight of the fruit
# and 'b' is the whether it is bumpy(0) or smooth(1)
features = [[140,1],[130,1],[150,0], [170,0]]
# a data set the corresponds to the field 'features' and
# represents whether the fruit is an orange (0) or an apple(1)
lables = [0,0,1,1]
clf = tree.DecisionTreeClassifir()
clf = clf.fit(features,lables)
print (clf.prdict[[160,0]])
