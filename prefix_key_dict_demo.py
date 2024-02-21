class PrefixDict(dict):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        assert all(isinstance(v,str) for v in self.keys())

    def __getitem__(self, key):
        if isinstance(key, str):
            # Check if key is a prefix of any existing keys
            matched_keys = [k for k in self.keys() if k.startswith(key)]
            if matched_keys:
                # If there are matches, return the values corresponding to those keys
                return {k: super(PrefixDict,self).__getitem__(k) for k in matched_keys}
            else:
                raise KeyError(f"No keys with prefix '{key}' found")
        else:
            # If key is not a string, treat it as a regular dictionary access
            return super().__getitem__(key)

# Example usage:
original_dict = {'apple': 1, 'banana': 2, 'orange': 3, 'app': 4}
prefixed_dict = PrefixDict(original_dict)
print(prefixed_dict['a'])  # Output: {'apple': 1, 'app': 4}
print(prefixed_dict['ban'])  # Output: {'banana': 2}
print(prefixed_dict['kiwi'])  # KeyError: No keys with prefix 'kiwi' found
