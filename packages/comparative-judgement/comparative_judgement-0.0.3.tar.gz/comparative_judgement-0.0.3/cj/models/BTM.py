import numpy as np
from scipy.optimize import minimize

class BTMCJ:
    def __init__(self, n_items):
        self.n_items = n_items

    def run(self, X):
        number_of_rounds = len(X)
        self.m = np.asarray([[0 if i!=j else -1 
              for j in range(self.n_items)] 
                for i in range(self.n_items)])

        for _ in range(number_of_rounds):
            a = X[_][0]
            b = X[_][1]
            winner = X[_][2]

            if winner == a:
                self.m[a][b] += 1
            elif winner == b:
                self.m[b][a] += 1
        
        # Sample results matrix
        results = self.m
        items = list(range(self.n_items))

        # Create pairwise comparison data from results matrix
        comparisons = []
        for i in range(self.n_items):
            for j in range(self.n_items):
                if results[i, j] > 0:
                    comparisons.extend([(i, j)] * results[i, j])

        def bradley_terry_log_likelihood(params):
            # Convert params to strengths
            strengths = np.exp(params)  # Use exponential to ensure positive strengths
            log_likelihood = 0
            
            for winner, loser in comparisons:
                # Probability of winner beating loser
                prob = strengths[winner] / (strengths[winner] + strengths[loser])
                
                # Update log likelihood
                log_likelihood += np.log(prob)
                
            return -log_likelihood  # Return negative log likelihood for minimization

        # Initial parameters (log strengths)
        self.initial_params = np.zeros(self.n_items)

        # Optimize to find the best strengths
        self.result = minimize(bradley_terry_log_likelihood, self.initial_params, method='BFGS')

        # Get the optimized strengths
        self.optimal_params = self.result.x
        self.strengths = np.exp(self.optimal_params)

        # Map strengths back to items
        self.item_strengths = {item: strength for item, strength in zip(items, self.strengths)}

        self.rank = np.argsort(-self.optimal_params)

        # print("Item strengths:")
        # for item, strength in item_strengths.items():
        #     print(f"Item {item}: {strength:.4f}")