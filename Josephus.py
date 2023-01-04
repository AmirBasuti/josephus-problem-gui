

def josephus(n, k):
    '''
    josephus(n, k)
    Input:  (int) n = Number of people in the circle
            (int) k = kth person will be executed each time from current position.
    Returns: (list) order_of_execution = Order of people executed. [First... to ...last person executed]
            (int) survivor = Position of the person who survives till the end. (who is freed)
    '''

    try:
        order_of_execution = []
        survivor = None
        n, k = int(float(n)), int(float(k))

        # Generate a list numbered from 1 to n (to represent people)
        circle_of_people = [num for num in range(1, n + 1)]

        index = 0
        people_left = len(circle_of_people)
        while (people_left > 1):
            index = (index + (k - 1)) % (people_left)
            order_of_execution.append(circle_of_people.pop(index))
            people_left -= 1

        survivor = circle_of_people.pop()

    except Exception as e:
        print("\nError occurred: ", e)
        print("Please ensure the inputs are integers, or atleast don't contain alphabets,special chars\n")
    return order_of_execution
