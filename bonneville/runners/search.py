# -*- coding: utf-8 -*-
'''
Runner frontend to search system
'''

# Import bonneville libs
import bonneville.search
import bonneville.output


def query(term):
    '''
    Query the search system

    CLI Example:

    .. code-block:: bash

        salt-run search.query foo
    '''
    search = bonneville.search.Search(__opts__)
    result = search.query(term)
    bonneville.output.display_output(result, 'pprint', __opts__)
    return result
