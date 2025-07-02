from django.db import models
from . import SUBJECT_CHOICES, SUBJECT_TYPE_CHOICES, CLASS_CHOICES, REPORT_COLUMNS
from .utils import assign_grade

class Student(models.Model):
    """Consists of the parameters and methods performed on a student"""
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    username = models.CharField(max_length=150, blank=True, unique=True)
    full_name = models.CharField(max_length=201, blank=True)
    age = models.PositiveIntegerField()
    class_name = models.CharField(max_length=10, choices=CLASS_CHOICES)
    password = models.CharField(max_length=128)

    def save(self, *args, **kwargs):
        if not self.pk:
            super().save(*args, **kwargs)
        if not self.username:
            self.username = f"{self.id}-{self.first_name.lower()}-{self.last_name.lower()}"
            self.full_name = f"{self.last_name} {self.first_name}"
        super().save(*args, **kwargs)

    def compile_scores(self):
        """Compile student scores"""
        scores = {'data': {}}
        scores['columns'] = []
        for exam_code, exam_type in SUBJECT_TYPE_CHOICES:
            temp_dict = {}
            temp_total = 0
            subject_count = 0
            for subject in self.subject_set.all(): # self.subject_set.all() returns all subjects that are related to this username
                if subject.type != exam_code:
                    continue
                if subject.name in REPORT_COLUMNS:
                    temp_dict[subject.name] = subject.score
                    temp_total += subject.score
                    subject_count += 1
            # GRADE
            if subject_count > 0:
                avg = temp_total / subject_count
            else:
                avg = 0
            grade = assign_grade(avg)

            temp_dict['TOTAL'] = temp_total
            temp_dict['AVG'] = avg
            temp_dict['GRADE'] = grade

            scores['data'][exam_code] = {}
            for k, v in temp_dict.items():
                if k in REPORT_COLUMNS:
                    scores['data'][exam_code][k] = v
                    scores['columns'].append(k)
        # Remove duplicates from columns while maintaining order
        seen = set()
        unique_columns = []
        for col in scores['columns']:
            if col not in seen:
                unique_columns.append(col)
                seen.add(col)
        scores['columns'] = unique_columns
        return scores

    def __str__(self):
        return f"{self.id}-{self.first_name}-{self.last_name}"


class Subject(models.Model):
    name = models.CharField(max_length=10, choices=SUBJECT_CHOICES)
    score = models.PositiveBigIntegerField()
    type = models.CharField(max_length=10, choices=SUBJECT_TYPE_CHOICES)
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE) # Many-to-one relationships

    def __str__(self):
        return f"{self.student_id.id}-{self.name}-{self.score}".replace(" ", "-")
