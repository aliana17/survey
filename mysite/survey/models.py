from django.db import models

# Create your models here.
class Customers(models.Model):
    cust_id = models.IntegerField()
    survey = models.BooleanField(default=False)

    def __str__(self):
        return self.cust_id


class Question(models.Model):
    text = models.TextField()

    def __str___(self):
        return self.text


class Answers(models.Model):
    ques = models.ForeignKey(Question, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customers, on_delete=models.CASCADE)
    text = models.TextField()

    def __str__(self):
        return f"Customer {self.customer.cust_id}, Question {self.ques.text}, Answer {self.text}"
