NEXT_ALPHA_DICT = { "a":"b",
                    "b":"c",
                    "c":"d",
                    "d":"e",
                    "e":"f",
                    "f":"g",
                    "g":"h",
                    "h":"i",
                    "i":"j",
                    "j":"k",
                    "k":"l",
                    "l":"m",
                    "m":"n",
                    "n":"o",
                    "o":"p",
                    "p":"q",
                    "q":"r",
                    "r":"s",
                    "s":"t",
                    "t":"u",
                    "u":"v",
                    "v":"w",
                    "w":"x",
                    "x":"y",
                    "y":"z",
                    "z":"",}
# NEXT_ALPHA_DICT maps a given character to its next character in the alphabet. It's used
# for taking a step in the alphabetized space.



def recursiveExtraction(allNames, queryStr):
    """
    Description: This function does the actual work described in extract, which serves more as a 
        wrapper. The function  uses queryStr as the input to query. queryStr serves as the 
        base case stopping condition as queryStr is edited at every call to be the next step in
        the  alphabetized space. As soon as queryStr is "" then we know we've iterated through
        the entire database.
    Input:
        allNames (list(str)): a list of database names so far. Because python lets me edit lists
            within the function I pass the same list to each call and edit it within the function
        queryStr (str): The query str currently being used. It should represent each step through
            the alphabetized space. 
    Output: 
        None: Nothing is returned but allNames is edited during the function calls.
    TODO:
    """
    return(0)






def extract(query):
    """extract takes in a `query` API function (which returns the first 5 usernames, lexicographically sorted,
    that start with a prefix) and returns the sorted list of all usernames in the database.

    For example, the `query` function in provided in `main` works as follows:
    
    query("a") #=> ["abracadara", "al", "alice", "alicia", "allen"]
    query("ab") #=> ["abracadara"]

    The following implementation would pass the assertion in `main`, but is not a correct solution since it
    works only for that example `query`:

    def extract(query):
        return query("ab") + query("al") + query("altercation") + query("b") + query("el") + query("ev") + query("m")

    Your goal is to write an `extract` method that is correct for any provided `query`.
    """
    # YOUR CODE HERE
    allNames = []
    recursiveExtraction(allNames, queryStr)
    return(allNames)

def main():
    """Runs your solution -- no need to update (except to maybe try out different databases)."""
    # Sample implementation of the autocomplete API
    database = ["abracadara", "al", "alice", "alicia", "allen", "alter", "altercation", "bob", "element", "ello", "eve", "evening", "event", "eventually", "mallory"]
    query = lambda prefix: [d for d in database if d.startswith(prefix)][:5]
    assert extract(query) == database

main()