"""
Type descriptions of Twitterverse and Query dictionaries
(for use in docstrings)

Twitterverse dictionary:  dict of {str: dict of {str: object}}
    - each key is a username (a str)
    - each value is a dict of {str: object} with items as follows:
        - key "name", value represents a user's name (a str)
        - key "location", value represents a user's location (a str)
        - key "web", value represents a user's website (a str)
        - key "bio", value represents a user's bio (a str)
        - key "following", value represents all the usernames of users this
          user is following (a list of str)

Query dictionary: dict of {str: dict of {str: object}}
   - key "search", value represents a search specification dictionary
   - key "filter", value represents a filter specification dictionary
   - key "present", value represents a presentation specification dictionary

Search specification dictionary: dict of {str: object}
   - key "username", value represents the username to begin search at (a str)
   - key "operations", value represents the operations to
     perform (a list of str)

Filter specification dictionary: dict of {str: str}
   - key "following" might exist, value represents a username (a str)
   - key "follower" might exist, value represents a username (a str)
   - key "name-includes" might exist, value represents a str
     to match (a case-insensitive match)
   - key "location-includes" might exist, value represents a str
     to match (a case-insensitive match)

Presentation specification dictionary: dict of {str: str}
   - key "sort-by", value represents how to sort results (a str)
   - key "format", value represents how to format results (a str)

"""

# Write your Twitterverse functions here


def process_data(twitter_data_file):
    """ (file open for reading) -> Twitterverse dictionary

    Read twitter_data_file and return the data in the file in
    the Twitterverse dictionary format.

    """

    # Stores the entire file in a single string.
    file_as_string = twitter_data_file.read()
    user_info = {}
    user_data_end = 0

    # Iterate over file_as_string and slice the string to obtain data
    # for each user.
    while user_data_end < len(file_as_string):
        username = file_as_string[user_data_end :
                                  file_as_string.index('\n', user_data_end + 1)]
        user_data_start = user_data_end + len(username) + 1
        endbio_index = file_as_string.index("ENDBIO", user_data_start)
        user_data_end = file_as_string.index("END", endbio_index + 7) + 4
        user_data = file_as_string[user_data_start : user_data_end]
        user_info[username] = get_user_info(user_data)

    return user_info


def get_user_info(user_data):
    """ str -> dict

    Slice user_data into different substrings and return data_dictionary for
    the particular user.

    >>> get_user_info("tomCruise\nTom Cruise\nLos Angeles, CA\nhttp://www.tom\
                      cruise.com\nOfficial TomCruise.com crew tweets. We love \
                      you guys! \nVisit us at Facebook!\nENDBIO\nkatieH\n\
                      NicoleKidman\nEND\n")
        {'following': ['katieH', 'PerezHilton'], 'bio': \
        'Official TomCruise.com crew tweets. We love you guys! \
        \nVisit us at Facebook!', 'location': 'Los Angeles, \
        CA', 'name': 'Tom Cruise', 'web': \
        'http://www.tomcruise.com'}

    >>> get_user_info("PerezHilton\nPerez Hilton\nHollywood, California\n\
                      http://www.PerezH...\nPerez Hilton is the creator and\
                      writer of one of the most famous websites\nin the world.\
                      And he also loves music - a lot!\nENDBIO\ntomCruise\n\
                      katieH\nNicoleKidman\nEND\n")
        {'following': ['tomCruise', 'katieH', 'x'],\
        'bio': 'Perez Hilton is the creator and writer of one\
        of the most famous websites\nin the world. And he\
        also loves music - a lot!', 'location': 'Hollywood, \
        California', 'name': 'Perez Hilton', 'web': \
        'http://www.PerezH...'}

    """

    data_dictionary = {}
    data_keys = ['name', 'location', 'web', 'bio', 'following']
    data_key_index = 0
    i = 0
    end_of_user_data = len(user_data)

    # Iterate through user_data and slice it in order to obtain the appropriate
    # values for the respective keys.
    while i < end_of_user_data:
        if ( data_key_index < 3):
            key_value_end = user_data.index('\n', i, end_of_user_data)
            line_of_data = user_data[i : key_value_end]
            data_dictionary[data_keys[data_key_index]] = line_of_data
            data_key_index = data_key_index + 1
            i = key_value_end + 1
        elif data_key_index == 3:
            key_value_end = user_data.index('ENDBIO', i, end_of_user_data)
            line_of_data = user_data[i : key_value_end - 1]
            data_dictionary[data_keys[data_key_index]] = line_of_data
            data_key_index = data_key_index + 1
            i = key_value_end + 7
        else:
            key_value_end = user_data.index('END', i, end_of_user_data)
            line_of_data = user_data[i : key_value_end - 1]
            user_following = line_of_data.split("\n")
            data_dictionary[data_keys[data_key_index]] = user_following
            i = end_of_user_data
    return data_dictionary


def process_query(query_file):
    """ (file open for reading) -> query dictionary

    Read query_file and return the data in the file in
    the query dictionary format.

    """

    # Stores the entire file as a single string.
    file_as_string = query_file.read()
    query = {}

    # Slice file_as_string to obtain data for search specification dictionary.
    specification_start = file_as_string.index("SEARCH") + 7
    specification_end = file_as_string.index("FILTER") - 1
    specification_data = file_as_string[specification_start : specification_end]
    query["search"] = get_search_specification(specification_data)

    # Slice file_as_string to obtain data for filter specification dictionary.
    specification_start = specification_end + 8
    specification_end = file_as_string.index("PRESENT") - 1
    specification_data = file_as_string[specification_start : specification_end]
    query["filter"] = get_filter_specification(specification_data)

    # Slice file_as_string to obtain data for present specification dictionary.
    specification_start = specification_end + 9
    specification_end = len(file_as_string)
    specification_data = file_as_string[specification_start : specification_end]
    query["present"] = get_present_specification(specification_data)

    return query


def get_search_specification(search_data):
    """ str -> search specification dictionary

    Slice search_data into various substrings in order to obtain appropriate
    values for the given keys and return a search specification dictionary.

    >>> get_search_specification("tomCruise\nfollowing\nfollowers")
        {'username': 'tomCruise', 'operations': ['following', 'followers']}

    >>> get_search_specification("katieH\nfollowers\nfollowing\nfollowing")
        {'username': 'katieH', 'operations': ['followers', 'following', \
        'following']}

    """

    search_specification = {}
    username = search_data[ : search_data.index("\n")]
    operations = search_data[search_data.index("\n") + 1 : len(search_data)]
    search_specification["username"] = username
    search_specification["operations"] = operations.split("\n")

    return search_specification


def get_filter_specification(filter_data):
    """ str -> filter specification dictionary

    Slice filter_data into various substrings in order to obtain appropriate
    values for the keys and return a filter specification dictionary.

    >>> get_filter_specification("following katieH")
        {'following': 'katieH'}
    >>> get_filter_specification("following tomCruise\nlocation-includes US")
        {'location-includes': 'US', 'following': 'tomCruise'}

    """

    filter_specification = {}
    if len(filter_data) == 0:
        filter_data_lines = []
    else:
        filter_data_lines = filter_data.split("\n")
    i = 0
    while i < len(filter_data_lines) and filter_data_lines[i] != "":
        key_value_pair = filter_data_lines[i].split()
        filter_specification[key_value_pair[0]] = key_value_pair[1]
        i = i + 1

    return filter_specification


def get_present_specification(present_data):
    """ str -> present specification dictionary

    Slice present_data into various substrings in order to obtain appropriate
    values for the keys and return a filter specification dictionary.

    >>> get_present_specification("sort-by username\nformat long")
        {'format': 'long', 'sort-by': 'username'}
    >>> get_present_specification("sort-by popularity\nformat short")
        {'format': 'short', 'sort-by': 'popularity'}

    """

    present_specification = {}
    if len(present_data) == 0:
        present_data_lines = []
    else:
        present_data_lines = present_data.split("\n")
    i = 0
    while i < len(present_data_lines) and present_data_lines[i] != "":
        key_value_pair = present_data_lines[i].split()
        present_specification[key_value_pair[0]] = key_value_pair[1]
        i = i + 1

    return present_specification


def all_followers(twitterverse_data, username):
    """ (Twitterverse dictionary, str) -> list of string

    Identify and return a list of all the users in twitter_data following
    username.

    """

    list_of_followers = []
    for key in twitterverse_data:
        if username in twitterverse_data[key]["following"]:
            list_of_followers.append(key)

    return list_of_followers


def get_search_results(twitterverse_data, search_specification):
    """ (Twitterverse dictionary, search specification dictionary) ->
        list of str

    Perform search_specification on twitterverse_data and return a list of
    usernames that match the search criteria.

    """

    usernames_list = [search_specification["username"]]
    usernames_list_draft = []

    if usernames_list[0] in twitterverse_data:
        for item in search_specification["operations"]:
            if item == "followers":
                for username in usernames_list:
                    if username in twitterverse_data:
                        usernames = all_followers(twitterverse_data, username)
                        usernames_list_draft.extend(usernames)
            elif item == "following":
                for username in usernames_list:
                    if username in twitterverse_data:
                        usernames = twitterverse_data[username]["following"]
                        usernames_list_draft.extend(usernames)
            usernames_list = remove_duplicates(usernames_list_draft)
            usernames_list_draft = []
    else:
        usernames_list = []

    return usernames_list


def remove_duplicates(duplicates_list):
    """ (list of str) -> list of str

    Return a list of all usernames present in duplicates_list without any
    reoccurences of a username.

    """

    no_duplicate_list = []

    for item in duplicates_list:
        if item not in no_duplicate_list:
            no_duplicate_list.append(item)

    return no_duplicate_list


def get_filter_results(twitterverse_data, username_list, filter_specification):
    """ (Twitterverse dictionary, list of str,filter specification dictionary)
        -> list of str 

    Aplly filter_specification to username_list and return the resulting list
    of usernames.

    """

    filtered_list = []

    for username in username_list:
        if username in twitterverse_data:
            flag = True
            for key in filter_specification:
                key_value = filter_specification[key]
                if "include" in key:
                    if key == "location-includes":
                        user_location = twitterverse_data[username]["location"]
                        if key_value.lower() not in user_location.lower():
                            flag = False
                    elif key == "name-includes":
                        user_name = twitterverse_data[username]["name"]
                        if key_value.lower() not in user_name.lower():
                            flag = False
                elif key == "following":
                    user_following = twitterverse_data[username]["following"]
                    if key_value not in user_following:
                        flag = False
                elif key == "follower":
                    if key_value in twitterverse_data:
                        user_follower = twitterverse_data[key_value]["following"]
                        if username not in user_follower:
                            flag = False
                    else:
                        flag = False
            if flag:
                filtered_list.append(username)

    return filtered_list


def get_present_string(twitterverse_data, username_list, present_specification):
    """ (Twitterverse dictionary, list of str,
        presentation specification dictionary) -> str

    Return a string formated based on present_specification.

    """

    sort_by = present_specification["sort-by"]
    final_list = username_list[:]

    if sort_by == "username":
        tweet_sort(twitterverse_data, final_list, username_first)
    elif sort_by == "name":
        tweet_sort(twitterverse_data, final_list, name_first)
    elif sort_by == "popularity":
        tweet_sort(twitterverse_data, final_list, more_popular)

    output_string = ""

    if present_specification["format"] == "short":
        output_string = output_string + str(final_list)

    else:
        username_keys = ["name", "location", "web", "bio", "following"]

        for username in username_list:
            output_string = output_string + "----------\n"
            output_string = output_string + username + "\n"

            for key in username_keys:
                key_value = twitterverse_data[username][key]
                if key == "bio":
                    output_string = output_string + key + ":\n" + key_value \
                                    + "\n"
                elif key == "web":
                    output_string = output_string + "website: " + key_value \
                                    + "\n"
                else:
                    output_string = output_string + key + ": " + str(key_value)\
                                    + "\n"

        if len(username_list) == 0:
            output_string = output_string + "----------\n"

        output_string = output_string + "----------\n"

    return output_string


# --- Sorting Helper Functions ---
def tweet_sort(twitter_data, results, cmp):
    """ (Twitterverse dictionary, list of str, function) -> NoneType

    Sort the results list using the comparison function cmp and the data in
    twitter_data.

    >>> twitter_data = {\
    'a':{'name':'Zed', 'location':'', 'web':'', 'bio':'', 'following':[]}, \
    'b':{'name':'Lee', 'location':'', 'web':'', 'bio':'', 'following':[]}, \
    'c':{'name':'anna', 'location':'', 'web':'', 'bio':'', 'following':[]}}
    >>> result_list = ['c', 'a', 'b']
    >>> tweet_sort(twitter_data, result_list, username_first)
    >>> result_list
    ['a', 'b', 'c']
    >>> tweet_sort(twitter_data, result_list, name_first)
    >>> result_list
    ['b', 'a', 'c']

    """

    # Insertion sort
    for i in range(1, len(results)):
        current = results[i]
        position = i
        while position > 0 and cmp(twitter_data, results[position - 1],\
                                   current) > 0:
            results[position] = results[position - 1]
            position = position - 1
        results[position] = current


def more_popular(twitter_data, a, b):
    """ (Twitterverse dictionary, str, str) -> int

    Return -1 if user a has more followers than user b, 1 if fewer followers,
    and the result of sorting by username if they have the same, based on the
    data in twitter_data.

    >>> twitter_data = {\
    'a':{'name':'', 'location':'', 'web':'', 'bio':'', 'following':['b']}, \
    'b':{'name':'', 'location':'', 'web':'', 'bio':'', 'following':[]}, \
    'c':{'name':'', 'location':'', 'web':'', 'bio':'', 'following':[]}}
    >>> more_popular(twitter_data, 'a', 'b')
    1
    >>> more_popular(twitter_data, 'a', 'c')
    -1
    """

    a_popularity = len(all_followers(twitter_data, a))
    b_popularity = len(all_followers(twitter_data, b))
    if a_popularity > b_popularity:
        return -1
    if a_popularity < b_popularity:
        return 1
    return username_first(twitter_data, a, b)


def username_first(twitter_data, a, b):
    """ (Twitterverse dictionary, str, str) -> int

    Return 1 if user a has a username that comes after user b's username
    alphabetically, -1 if user a's username comes before user b's username,
    and 0 if a tie, based on the data in twitter_data.

    >>> twitter_data = {\
    'a':{'name':'', 'location':'', 'web':'', 'bio':'', 'following':['b']}, \
    'b':{'name':'', 'location':'', 'web':'', 'bio':'', 'following':[]}, \
    'c':{'name':'', 'location':'', 'web':'', 'bio':'', 'following':[]}}
    >>> username_first(twitter_data, 'c', 'b')
    1
    >>> username_first(twitter_data, 'a', 'b')
    -1
    """

    if a < b:
        return -1
    if a > b:
        return 1
    return 0


def name_first(twitter_data, a, b):
    """ (Twitterverse dictionary, str, str) -> int

    Return 1 if user a's name comes after user b's name alphabetically,
    -1 if user a's name comes before user b's name, and the ordering of their
    usernames if there is a tie, based on the data in twitter_data.

    >>> twitter_data = {\
    'a':{'name':'Zed', 'location':'', 'web':'', 'bio':'', 'following':[]}, \
    'b':{'name':'Lee', 'location':'', 'web':'', 'bio':'', 'following':[]}, \
    'c':{'name':'anna', 'location':'', 'web':'', 'bio':'', 'following':[]}}
    >>> name_first(twitter_data, 'c', 'b')
    1
    >>> name_first(twitter_data, 'b', 'a')
    -1
    """

    a_name = twitter_data[a]["name"]
    b_name = twitter_data[b]["name"]
    if a_name < b_name:
        return -1
    if a_name > b_name:
        return 1
    return username_first(twitter_data, a, b)


# if __name__ == '__main__':
#    import doctest
#    doctest.testmod()
