# cook your dish here
def allowed_people(queue: str) -> int:
    boys = 0
    girls = 0
    count = 0
    for person in queue:
        if person == 'B':
            boys += 1
        elif person == 'G':
            girls += 1
        count += 1
        
        if boys > 2 * girls:
            return count  
    return count

def process_test_cases():
    T = int(input().strip())
    results = []
    for _ in range(T):
        N = int(input().strip())
        queue = input().strip()
        results.append(allowed_people(queue))
    for result in results:
        print(result)


if __name__ == "__main__":
    process_test_cases()
