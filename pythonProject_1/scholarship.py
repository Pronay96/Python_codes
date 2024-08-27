def check_scholarships(string1, string2):
    tot_students = string1.split(',')
    scholar_students = string2.split(',')
    non_scholar_students = []
    if len(tot_students) < len(scholar_students):
        return "Invalid data"
    for id_student in tot_students:
        if id_student in scholar_students and len(tot_students) == len(scholar_students):
            return "All the students have scholarships"
        if id_student not in scholar_students:
            non_scholar_students.append(id_student)
    return non_scholar_students


def main():
    all_students = input()
    scholars = input()
    final_list = check_scholarships(all_students, scholars)
    if isinstance(final_list,list):
        print(f"Students without scholarships: {','.join(final_list)}")
    else:
        print(final_list)


main()
