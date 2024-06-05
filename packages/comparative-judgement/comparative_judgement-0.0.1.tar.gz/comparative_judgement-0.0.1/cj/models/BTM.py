import numpy as np

class BTMCJ:

    def __init__(self, n_items):
        self.n_items = n_items

    def check(self):
        print("BTMCJ")

    def update_p(
        self, 
        m: np.ndarray, 
        i: int, 
        p: np.ndarray
    ):
        """Updates the estimated parameters of p

        Args:
            m (np.ndarray): _description_
            i (int): _description_
            p (np.ndarray): _description_

        Returns:
            _type_: Updated p parameters before geometric mean normalisation.
        """
        part_1 = []
        part_2 = []

        for j in range(m.shape[1]):
            if m[i, j] != -1:
                part_1.append(m[i, j] * (p[j] / (p[i] + p[j])))
                part_2.append(m[j, i] * (1 / (p[i] + p[j])))
        
        part_3 = np.sum(part_1) / np.sum(part_2)

        return part_3


    def run(
        self, 
        X: list, # maybe change to np.ndarray?
            #, result_output="single"
    ):
        """Runs the BTMCJ algorithm, fitting the 
        parameters to the pairwise comparison data results.

        Args:
            X (list): Inputted data following a n by 3 format (a, b, winner).
        """

        number_of_rounds = len(X)
        m = np.asarray([[0 if i!=j else -1 
              for j in range(self.n_items)] 
                for i in range(self.n_items)])

        for _ in range(number_of_rounds):
            a = X[_][0]
            b = X[_][1]
            winner = X[_][2]

            if winner == a:
                m[a][b] += 1
            elif winner == b:
                m[b][a] += 1

        try:
            p = np.asarray([1.0] * self.n_items)

            for _ in range(10_000):
                p_previous = p.copy()
                for i in range(len(p)):
                    p[i] = self.update_p(m, i, p)

                normalising_p = pow(np.prod(p), 1/len(p))
                p = np.asarray(p) / normalising_p

                if np.all(np.abs(p - p_previous) < 1e-6):
                    self.converge = f"Converged! on round: {_}"
                    break

                # self.p_scaled = [k * 100 for k in p]
                self.final_rank = np.argsort(-np.array(p))
            
        except Exception as e:
            print(f"Error: {str(e)}")
        
        self.p = p


    def get_ranking(self):
        """Prints the final ranking of the items.
        """
        print("BTMCJ ranking:")
        for i in range(len(self.final_rank)):
            print(f"{i+1}: Item {self.final_rank[i]} - score: {self.p[self.final_rank[i]]}")