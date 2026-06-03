"""
# Most Frequent Octet

You've compiled a list of IP addresses of all the clients connected to your service. Assume all IPs are unique and follow the IPv4 format, which consists of four 8-bit numbers (called octets) separated by dots. Return the most common first octet among the connections.

Example 1: ips = ["203.0.113.10", "208.51.100.5", "202.0.2.5", "203.0.113.5"]
Output: "203". 203 appears twice as the first octet.

Example 2: ips = ["10.0.0.1", "10.0.0.2", "192.168.1.1"]
Output: "10". 10 appears twice as the first octet, while 192 appears once.

Example 3: ips = []
Output: None. There are no IP addresses.

Constraints:

- The length of `ips` is at most 10^5
- All IPs are unique and follow the IPv4 format
- Each octet is a number between `0` and `255`

"""

## An octet contains 8 bits, it can represent exactly \(2^{8}\) (or 256) possible values
# TO: O(n), n is total number of ips
# SO: O(1), as array using constant space


def solution(ips):
    if not ips:
        return None

    first_octet = [0] * 256
    for ip in ips:
        first = ip.split(".")
        int_first = int(first[0])
        first_octet[int_first] += 1

    res = 0
    most_frequent = 0
    for i in range(256):
        if first_octet[i] > most_frequent:
            most_frequent = first_octet[i]
            res = i

    return str(res)


### Testing Phase ###
def run_tests():
    tests = [
        # Example 1 from the book
        (["203.0.113.10", "208.51.100.5", "202.0.2.5", "203.0.113.5"], "203"),
        # Example 2 from the book
        (["10.0.0.1", "10.0.0.2", "192.168.1.1"], "10"),
        # Example 3 from the book
        ([], None),
    ]

    for i, (ips, expected) in enumerate(tests):
        result = solution(ips)
        print(f"Test {i+1}: {result} == {expected} -> {result == expected}")
        assert (
            result == expected
        ), f"Test case {i + 1} failed: expected {expected}, got {result}"
    print("All test cases passed!")


if __name__ == "__main__":
    run_tests()
