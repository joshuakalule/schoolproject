def assign_grade(average):
    if average == 0:
        grade = "-"
    elif average >= 95:
        grade = "A+"
    elif average >= 90:
        grade = "A"
    elif average >= 80:
        grade = "B"
    elif average >= 70:
        grade = "C"
    elif average >= 60:
        grade = "D"
    elif average >= 50:
        grade = "E"
    else:
        grade = "PASS"
    return grade


def compile_score_table(scores: dict):
    columns = scores['columns']
    scores_header = [''] + columns
    scores_data = []
    for row_name, row_data in scores.get('data', {}).items():
        temp_row = []
        for column in columns:
            temp_row.append(row_data.get(column))
        scores_data.append([row_name] + temp_row)
    return (scores_header, scores_data)
