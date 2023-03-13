"""
We have a grouping problem that members of a collection must be put into arbitrary number of groups based on some rules.
Members are given as lines in a file, with a name and its grouping criteria. Each line has special format as below:
name[***]restricted_level[***]optional_level
    - Name: is the name of member to be grouped,
    - [***]: is divider between values,
    - Restricted_level: members with similar values of it must not be put in one group. If this rule is not possible
      grouping process must be stopped,
    - Optional_level: members with similar value of it should not be put into one group. If this rule is not possible
      the grouping process goes on.
    - The number of members in each group must be the same.
"""