
from random import shuffle


class Extractor:
    """Reads lines of file and after some validation, returns list of members (lines) as a dictionary."""
    def __init__(self, path):
        self._path = path
        self.members = []
        print('*' * 100, '\n', 'Extracting provided file to members:')
        self.read_file()

    def read_file(self):
        with open(self._path) as file:
            content_lines = file.readlines()

        # Q: How to remove "\n" from lines?
        added_members = []
        for line in content_lines:
            split_line = dict()
            try:
                split_line['name'], split_line['restricted_level'], split_line['optional_level'] = line.split('[***]')
            except ValueError:
                print('Warning: One line not processed for invalid format')
                continue
            if not (split_line['name'] and split_line['restricted_level'] and split_line['optional_level']):
                print('Warning: A line has some null data. This line cannot be processed.')
                continue

            if split_line['name'] not in added_members:
                self.members.append(split_line)
                added_members.append(split_line['name'])
            else:
                print(f'Warning: {split_line["name"]} is duplicate. Just previous row with similar name will be considered.')


class Grouping:
    """evaluate grouping criteria based on members (lines) and given rules. Then members will be grouped and printed."""

    def __init__(self, number_of_groups):
        try:
            self.number_of_groups = number_of_groups
        except AttributeError:
            print('Grouping cannot be done.')
        else:
            try:
                self.extracted_members = Extractor('members.txt').members
                self.number_of_members = len(self.extracted_members)
                self.number_of_group_members = 0
                self.sorted_members = []

                if self.evaluate_grouping():
                    self.groups = []
                    self.group_members()
                    self.print_groups()

            except FileNotFoundError:
                print('File "members" is not found in the path.')

    @property
    def number_of_groups(self):
        return self._number_of_groups

    @number_of_groups.setter
    def number_of_groups(self, value):
        if not isinstance(value, int):
            print('Integer must be provided for number of groups.', end="")
            raise AttributeError
        elif value <= 1:
            print('Number of groups must be bigger than 1 groups.', end="")
            raise AttributeError
        else:
            self._number_of_groups = value

    def evaluate_grouping(self):
        # First rule
        if self.number_of_members % self.number_of_groups:
            print('Not groupable, because number of groups is not dividable by number of members.')
            return False
        else:
            self.number_of_group_members = int(self.number_of_members / self.number_of_groups)

        # Here we count restricted_level values frequency.
        restricted_levels = dict()
        for member in self.extracted_members:
            if member['restricted_level'] not in restricted_levels.keys():
                restricted_levels[str(member['restricted_level'])] = 1
            else:
                restricted_levels[str(member['restricted_level'])] += 1

        # Second rule: Here we check if the restricted level frequency exceeds number of groups.
        for level_frequency in restricted_levels.values():
            if int(level_frequency) > self.number_of_groups:
                print('Not groupable, because some restricted level values exceed requested number of groups.')
                return False

        # Use restricted_levels frequencies for sorting members in a new list named sorted_members:
        sorted_restricted_levels = sorted(restricted_levels.items(), key=lambda x: x[1], reverse=True)
        for freq in sorted_restricted_levels:
            for member in self.extracted_members:
                if member['restricted_level'] == freq[0]:
                    self.sorted_members.append(member)

        return True

    def group_members(self):
        # Generate groups based on numbers requested:
        for i in range(0, self.number_of_groups):
            self.groups.append(Group(self.number_of_group_members, i))

        # Now check in which group, members can be added into, based on sorted_members:
        for member in self.sorted_members:
            optional_group = []
            result = 0
            shuffle(self.groups)
            for group in self.groups:
                result = group.add_to_group(member)
                if result == 1:
                    break
                elif result == 2:
                    optional_group.append(group)
            if result == 2:
                optional_group[0].force_add_to_group(member)

    def print_groups(self):
        print('\n', '*'*100, '\n', 'Valid members grouped:')
        for member in self.extracted_members:
            print(member)

        print('\n', '*'*100, '\n', 'Generated groups are:')
        for group in self.groups:
            print(group)


# Q: should instead of dictionary keys, we use member objects?
class Member:
    pass


class Group:
    def __init__(self, number_of_group_members, group_number):
        self.group_number = group_number
        self.number_of_group_members = number_of_group_members
        self.existing_restricted_levels = []
        self.existing_optional_levels = []
        self.added_members = []

    def __str__(self):
        printable_members = f"Group number {self.group_number} :\n"
        for member in self.added_members:
            printable_members += str(member)+'\n'
        return printable_members

    def add_to_group(self, member):
        """If a member could be added to a group based on restricted and optional level constraints, it returns 1.
        If based onn restricted level it cannot be added, it returns 0. If restricted level is ok, but optional
        level is not meet, it returns 2 to signal the grouping module to look for a better match, if possible."""
        if member['restricted_level'] not in self.existing_restricted_levels and len(self.added_members) < self.number_of_group_members:
            if member['optional_level'] not in self.existing_optional_levels:
                self.added_members.append(member)
                self.existing_restricted_levels.append(member['restricted_level'])
                self.existing_restricted_levels.append(member['optional_level'])
                return 1
            else:
                return 2
        else:
            return 0

    def force_add_to_group(self, member):
        """If grouping module decides that no better assignment is possible, it adds member by this method."""
        if len(self.added_members) <= self.number_of_group_members:
            self.added_members.append(member)
            self.existing_restricted_levels.append(member['restricted_level'])
            self.existing_restricted_levels.append(member['optional_level'])


gr1 = Grouping(4)

