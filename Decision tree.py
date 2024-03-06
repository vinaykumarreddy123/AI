# Define a Node class to represent each node in the decision tree
class Node:
    def __init__(self, feature=None, threshold=None, left=None, right=None, value=None):
        self.feature = feature        # Index of the feature to split on
        self.threshold = threshold    # Threshold value for the split
        self.left = left              # Left subtree
        self.right = right            # Right subtree
        self.value = value            # Value if the node is a leaf

# Define a function to train the decision tree classifier
def train_decision_tree(X, y):
    # Define a function to calculate the Gini impurity
    def calculate_gini_impurity(labels):
        classes = set(labels)
        impurity = 1
        for cls in classes:
            p_cls = sum(labels == cls) / len(labels)
            impurity -= p_cls ** 2
        return impurity

    # Define a function to find the best split for the dataset
    def find_best_split(X, y):
        best_gini = float('inf')
        best_feature = None
        best_threshold = None

        for feature in range(X.shape[1]):
            thresholds = set(X[:, feature])
            for threshold in thresholds:
                left_indices = X[:, feature] < threshold
                right_indices = ~left_indices

                left_gini = calculate_gini_impurity(y[left_indices])
                right_gini = calculate_gini_impurity(y[right_indices])

                gini = (sum(left_indices) / len(y)) * left_gini + (sum(right_indices) / len(y)) * right_gini

                if gini < best_gini:
                    best_gini = gini
                    best_feature = feature
                    best_threshold = threshold

        return best_feature, best_threshold

    # Define a function to recursively build the decision tree
    def build_tree(X, y):
        if len(set(y)) == 1:
            return Node(value=y[0])

        best_feature, best_threshold = find_best_split(X, y)
        left_indices = X[:, best_feature] < best_threshold
        right_indices = ~left_indices

        left_tree = build_tree(X[left_indices], y[left_indices])
        right_tree = build_tree(X[right_indices], y[right_indices])

        return Node(feature=best_feature, threshold=best_threshold, left=left_tree, right=right_tree)

    return build_tree(X, y)

# Define a function to make predictions with the decision tree classifier
def predict(tree, X):
    def predict_single(node, sample):
        if node.value is not None:
            return node.value
        if sample[node.feature] < node.threshold:
            return predict_single(node.left, sample)
        else:
            return predict_single(node.right, sample)

    return [predict_single(tree, sample) for sample in X]

# Dummy dataset
X_train = [
    [2.0, 3.0],
    [1.0, 4.0],
    [3.0, 2.0],
    [4.0, 1.0]
]
y_train = [0, 0, 1, 1]

# Train the decision tree
tree = train_decision_tree(X_train, y_train)

# Make predictions
X_test = [
    [2.5, 2.5],
    [3.5, 3.5]
]
predictions = predict(tree, X_test)
print("Predictions:", predictions)
