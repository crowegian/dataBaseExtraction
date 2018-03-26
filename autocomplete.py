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
                    "z":""}
# NEXT_ALPHA_DICT maps a given character to its next character in the alphabet. It's used
# for taking a step in the alphabetized space.
MAX_QUERY_RETURN = 5

"""
Description:
Input:
Output:
TODO:
"""


def maxPrefixPlusOne(a,b):
    """
    Description: Given two strings a and b (should be the last two names returned from a call
        to query) this function finds the maximum length prefix between a and b, and tacks on the
        next character in b. So for a = "alice" and b = "alicia" then "alici" will be returned.
        The idea is that this return will be the next step in the alphabetized space.
    Input:
        a,b (str): The strings to be compared. Should be the last two names returned from 
            a call to query.
    Output:
        currStepInAlpha (str): The maximally overlapping prefix plus one more character from b.
    TODO:
        1) When grabbing the next char in b I think you should be ok, but think more about 
            whether or not that index always exists. Should always exist.
    """
    currStepInAlpha = ""
    for charA, charB in zip(a,b):
        if charA == charB:
            currStepInAlpha += charA
        else:
            break
    # currStepInAlpha = "".join([char for char in a if char in b])# grab maximum overlap

    currStepInAlpha += b[len(currStepInAlpha)]# grab next char in b. 
    return(currStepInAlpha)


def nextStepInAlphabetizedSpace(queryStr):
    """
    Description: Changes the last character in queryStr to the next letter in the alphabet. If
        the last character is "z" then the last character is removed, and the second to last
        character is used. The step of removing characters can be repeated until queryStr == ""
    Input:
        queryStr (str): String to be used in query
    Output:
        queryStr (str): String to be used in query but moved one step forward in alphabetized space
    TODO:
    """
    queryStr = queryStr.rstrip("z")# removes trailing zs and assumes they should be replaced by
        # whitespace.
    queryStr = list(queryStr)
    if queryStr != []:
        queryStr[-1] =  NEXT_ALPHA_DICT[queryStr[-1]]         
    return("".join(queryStr))

def recursiveExtraction(allNames, query, queryStr, queryIndex, verbose = False):
    """
    Description: This function does the actual work described in extract, which serves more as a 
        wrapper. The function  uses queryStr as the input to query. queryStr serves as the 
        base case stopping condition as queryStr is edited at every call to be the next step in
        the  alphabetized space. As soon as queryStr is "" then we know we've iterated through
        the entire database.
    Input:
        allNames (list(str)): a list of database names so far. Because python lets me edit lists
            within the function I pass the same list to each call and edit it within the function
        query (API function): function to be called to query the database.
        queryStr (str): The query str currently being used. It should represent each step through
            the alphabetized space.
        queryIndex (int): This is an odd thing I have to do because if the maximum number of names
            is returned I set queryStr to a string which when used in query will return the last
            name in the previous query in the first index of the current query. There are many ways
            to solve this, but this is the most efficient. Query index allows me to chop off the
            first element in the returned list if needed.
    Output: 
        None: Nothing is returned but allNames is edited during the function calls.
    TODO:
        1) I'm a little worried that my index into names could error out if query index is 1 and 
            and empty list is returned. this shouldn't happen because if query index is 1 then we
            should always return at least one name (the one we're trying to chop off.)
    """
    if verbose:
        print("beginning Call")
        print("allNames {}, query {}, queryStr {}, queryIndex {}\n".format(allNames, query, queryStr,
                                                                         queryIndex))
    if queryStr == "":
        return(0)
    # if verbose:
    #     print(queryStr)
    names = query(queryStr)
    if verbose:
        print("query {} returned {}\n".format(queryStr, names))
    # 1/0
    allNames.extend(names[queryIndex:])
    if len(names) == MAX_QUERY_RETURN: # when the maximum number of names that can be returned
        #is returned, then there could be more names right after the last name returned.
        # print(queryStr)
        queryStr = maxPrefixPlusOne(a = names[-2], b = names[-1])
        # print(queryStr)
        # 1/0
        queryIndex = 1
    else:# if less than the maximum is returned then there are no names following the last name
        # in the alphabetized space, so we jump to the next step.
        queryStr = nextStepInAlphabetizedSpace(queryStr)
        queryIndex = 0
    if verbose:
        print("just finished call")
        print("allNames {}, query {}, queryStr {}, queryIndex {}\n".format(allNames, query, queryStr,
                                                                         queryIndex))
    recursiveExtraction(allNames, query, queryStr, queryIndex, verbose = verbose)






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
    recursiveExtraction(allNames = allNames, query = query, queryStr = "a", queryIndex = 0,
                        verbose = False)
    return(allNames)

def main():
    """Runs your solution -- no need to update (except to maybe try out different databases)."""
    # Sample implementation of the autocomplete API
    database = ["abracadara", "al", "alice", "alicia", "allen", "alter", "altercation", "bob", "element", "ello", "eve", "evening", "event", "eventually", "mallory"]
    query = lambda prefix: [d for d in database if d.startswith(prefix)][:5]
    assert extract(query) == database

main()