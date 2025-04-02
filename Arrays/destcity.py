class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        # the array path provides a pair destination "from" and "to"
        # identify constraints
        # the implementation should check for a source and destination
        # keep track of sources and destination
        # check if  is in destination
        destination = {} # intialize a hashmap
        
        for cities in paths:
            source, output = cities # Define key and value as city A and city B
            destination[source] = output # map city A and city B
        
        end_cities = destination.values() # store city B as end
        start_cities = destination.keys() # store city A as source

        for final_dest in end_cities: # check all city B in end
            if final_dest not in start_cities: # if City B is not in source
                return final_dest # this city B is the final destination

        # time complexity: O(n) for every city in paths
        # space complexity: O(n) for every city stored in hashmap

        # alternative implementation with 2 hashset
        # hashset for source
        # hashset for end

        # alternative implementation using 1 hashset
        # dest = set() # removes duplicates
            
        # for path in paths:
        #     dest.add(path[0])
        #     # add source city to destinations

        # for path in paths:
        #     if path[1] not in dest: #if end city doesn't exist in source cities
        #         return path[1]  # that end city is the final destination

