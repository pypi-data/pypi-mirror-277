import assetmodelutilities as amu


def validate_relationship_string(relationship_string):
    # The input string can be comma or colon separated.
    # We will return a string of colon separated relationships
    # Labels that do not conform to Neo4j naming rules will be back-ticked (`)
    # For example:
    #    fruit --> fruit
    #    apple,tree --> apple:tree
    #    birds&bees --> `birds&bees`
    #    one,two,!three --> one:two:`!three`

    result = ''
    for a_relationship in relationship_string.replace(",", ":").split(':'):
        result += ':' + amu.validate(a_relationship)

    # Remove the leading ':' from the result because we don't want it
    if result.startswith(':'):
        result = result[1:]

    return result


def validate_relationships(relationships):
    # We either get a string, or a list of strings.
    # Process as appropriate and return a string or list of strings to match input
    if isinstance(relationships, str):
        return validate_relationship_string(relationships)
    else:
        return [validate_relationship_string(i) for i in relationships]

def split_node_key(node):
    split_node = node.split(':')
    if len(split_node) == 1:
        name = node
        type = ''
    else:
        name = split_node[0]
        type = ':' + split_node[1]
    return name, type
