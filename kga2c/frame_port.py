import re

def f(templates, bindings):
    """
    bindinds are the keys
    takes the grammar straight from jericho
    splits on ;
    looks at all frames for each example, sums them
    places each summed frame slots into a dictionary with the key being the first verb version, just as in jericho's preprocess
    """

    ## problem: the grammar contains words that are cut off after the max_word_length i.e. swallo instead of swallow
    ## Actually seems like this won't be a huge problem, can just account for it in FE search

    templates = templates.split(';')

    frame_dict = {}
    p = re.compile('\S+(/\S+)+')

    for i in range(len(templates)):
        # calculating frames from each template split on '/'
        # match = p.search(template)
        ## Need to somehow convert template into frame

        frame_dict.update({bindings[i]: ???})
