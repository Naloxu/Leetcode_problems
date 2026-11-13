class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for current_string in strs:
            encoded_string += f"{len(current_string)}#{current_string}"
        return encoded_string

    def decode(self, encoded_string: str) -> List[str]:
        decoded_list = []
        current_index = 0
        while current_index < len(encoded_string):
            hash_index = current_index
            while encoded_string[hash_index] != '#':
                hash_index += 1

            string_length = int(encoded_string[current_index:hash_index])

            current_index = hash_index + 1
            decoded_list.append(encoded_string[current_index:current_index + string_length])

            current_index += string_length

        return decoded_list   