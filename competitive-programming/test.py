# Code Challenge
#  - Input: [
# [1,2],
# [2,3],
# [1,3],
# [3,4]
# ]
#    Output: [[1,2],[2,3],[3,4]]


# ip/v1/users/list
# ip/v1/organizaiton/{org_id}/users/list
# design patterns, problem solving 



def process_task(task_times):
    start_counts = {}
    end_counts = {}
    for i in range(len(task_times)):
        start_time = task_times[i][0]
        end_time = task_times[i][1]
        if start_time in start_counts.keys():
            start_counts[start_time].append(i)
        else:
            start_counts[start_time] = [i]
        if end_time in end_counts.keys():
            end_counts[end_time].append(i)
        else:
            end_counts[end_time] = [i]

    print(start_counts, end_counts)
    # ({1: [0, 2], 2: [1], 3: [3]}, {2: [0], 3: [1, 2], 4: [3]})

    start_colliding_task_ids = []
    end_colliding_task_ids = []
    for _, value in start_counts.items():
        if len(value) > 1:
            start_colliding_task_ids.extend(value)
    for _, value in end_counts.items():
        if len(value) > 1:
            end_colliding_task_ids.extend(value)
    print(start_colliding_task_ids, end_colliding_task_ids)
    # ([0, 2], [1, 2])
    task_to_be_deleted = set(start_colliding_task_ids) & set(end_colliding_task_ids)
    print(list(task_to_be_deleted))
    list_task_to_be_deleted = list(task_to_be_deleted)
    # copy_task_times = copy(task_times)
    for task_id in list_task_to_be_deleted:
        print(task_times)
        print('{}-->{}'.format(task_id, task_times[task_id]))
        d
        del task_times[task_id]
    return task_times





input2 =  [[1,2],[2,3],[1,3],[3,4]]
input =  [[1,2],[1,3],[1,3],[3,4]]
print('input is {}'.format(input))
output = process_task(input)
print('output is {}'.format(output))