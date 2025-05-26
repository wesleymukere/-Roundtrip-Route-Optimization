 def calculate_optimal_roundtrip(self):
        """Compute the shortest roundtrip using cached distance matrix"""
        counties = self.counties
        best_route = None
        min_distance = float('inf')
