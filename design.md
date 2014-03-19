## Design

[edited 20140319]

### Idea: Diminishing index of plausible next steps

1. Traverse target once and make "candidate" list of indices bearing elements that match the first element of the search string.

        candidate = []

1. For each item in candidate list, compare `target[item+1]` against the second element of the search string. Prune candidate list accordingly.
1. Continue until search string is exhausted or candidate list is empty.
1. Problem: each optional-content item still creates multiple lists that have to be handled. Should this be done as sublists within `candidate` or should separate `candidate` objects be instantiated and treated in parallel?

[end]
