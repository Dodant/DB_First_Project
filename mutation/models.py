from django.db import models

# 상염색체 관련 테이블
class Autosome(models.Model):
    auto_no = models.IntegerField(primary_key=True)
    auto_desc = models.TextField(default='Fill')

    def __str__(self):
        return str(self.auto_no)

class Auto_Syndrome(models.Model):
    auto_syn_code = models.IntegerField(primary_key=True)
    auto_syn_name = models.CharField(max_length=35)
    auto_syn_desc = models.TextField(default='Fill')
    auto_syn_fre = models.CharField(max_length=30, default='Fill')

    def __str__(self):
        return self.auto_syn_name

class Auto_Mutation(models.Model):
    auto_mut_code = models.IntegerField(primary_key=True)
    auto_pri = models.ForeignKey(Autosome, on_delete=models.CASCADE)
    TYPE = [
        ('Deletion', 'Deletion'),
        ('Duplication', 'Duplication'),
        ('Inversion', 'Inversion'),
        ('Translocation', 'Translocation'),
    ]
    mutation_type = models.CharField(max_length=15, choices=TYPE)
    auto_sec = models.IntegerField(blank=True, null=True)
    auto_syn_id = models.ForeignKey(Auto_Syndrome, on_delete=models.CASCADE)

    def __str__(self):
        return '#' + str(self.auto_pri) + ' ' + self.mutation_type


# 성염색체 관련 테이블
class Allo_Syndrome(models.Model):
    allo_syn_code = models.IntegerField(primary_key=True)
    allo_syn_name = models.CharField(max_length=30)
    allo_syn_desc = models.TextField(default='Fill')
    allo_syn_fre = models.CharField(max_length=30, default='Fill')

    def __str__(self):
        return self.allo_syn_name

class Allo_Mutation(models.Model):
    allo_mut_code = models.IntegerField(primary_key=True)
    linked = models.CharField(max_length=10)
    allo_syn_id = models.ForeignKey(Allo_Syndrome, on_delete=models.CASCADE)

    def __str__(self):
        return self.linked
