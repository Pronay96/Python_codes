def calculate_time(race_details):
    list_dic = []
    for details in race_details:
        id1 = details.split(":")[0]
        name = details.split(":")[1]
        speed = int(details.split(":")[2])

        dis = 200

        time_taken = round((dis/speed), 1)

        racer_dict = {'Id':id1, 'Name':name, 'Time':time_taken}
        list_dic.append(racer_dict)
    return list_dic


def find_qualifiers(race_details,time):
    list_qualify = []
    for dic_racer in race_details:
        if dic_racer['Time'] <= time:
            list_qualify.append(dic_racer['Name'])
    return list_qualify


def main():
    racer_list = []
    num = int(input("Enter the no. of race participants:"))
    for i in range(num):
        details = input()
        racer_list.append(details)
    final = calculate_time(racer_list)
    time_qualify = float(input("Enter the time to qualify for the next level:"))
    final_res = find_qualifiers(final,time_qualify)
    if final_res is not None and len(final_res) == 0:
        print("No one is qualified")
    else:
        print("The qualified participants are:")
        for loop in final_res:
            print(loop)

main()