from django.db import models


# Create your models here.
class Student(models.Model):
    idNum = models.CharField(max_length=8, primary_key=True)
    lastName = models.CharField(max_length=20)
    firstName = models.CharField(max_length=20)
    email = models.EmailField(max_length=100)
    cpNum = models.CharField(max_length=10)
    college = models.CharField(max_length=3)
    degree = models.CharField(max_length=20)
    level = models.CharField(max_length=1)
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.email


class Payment(models.Model):
    orNum = models.CharField(max_length=20)
    amount = models.FloatField()
    date = models.DateField()
    idNum = models.ForeignKey(Student, on_delete=models.CASCADE)
    isApproved = models.BooleanField(default=False)

    def __str__(self):
        return self.orNum


class Loan(models.Model):
    idNum = models.ForeignKey(Student, on_delete=models.CASCADE)
    amount = models.FloatField()
    date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, default='In Process')
    balance = models.FloatField(default=0)

    def __str__(self):
        return self.amount


class Create:
    @staticmethod
    def createStudent(student):
        student.save()

    @staticmethod
    def createPaymentA(payment):
        payment.save()

    @staticmethod
    def createPaymentB(ornum, amount, date, idnum, isapproved):
        p = Payment(orNum=ornum, amount=amount, date=date, idNum=idnum, isApproved=isapproved)
        p.save()


class Retrieve:
    # returns all students in the db
    @staticmethod
    def retrieve_student_all():
        return Student.objects.all()

    # returns students of a certain college
    @staticmethod
    def retrieve_student_college(college):
        return Student.objects.filter(college=college)

    # returns a specific student object
    @staticmethod
    def retrieve_student_email(email):
        return Student.objects.get(email=email)

    # returns all payments made
    @staticmethod
    def retrieve_payment_all():
        return Payment.objects.all()

    # returns payments made by a certain student
    @staticmethod
    def retrieve_payment_email(email):
        return Payment.objects.filter(email=email)

    # returns payments with a certain status
    @staticmethod
    def retrieve_payment_status(status):
        return Payment.objects.filter(isApproved=status)

    # returns all loan applications
    @staticmethod
    def retrieve_loan_all():
        return Loan.objects.all()

    # returns loan application made by a certain student
    @staticmethod
    def retrieve_loan_email(email):
        return Loan.objects.get(email=email)

    # returns loans with a certain status
    @staticmethod
    def retrieve_loan_status(status):
        return Loan.objects.filter(status=status)


class Edit:
    # approves a payment
    @staticmethod
    def approve_payment(pk):
        Payment.objects.get(pk=pk).isApproved = True

    # approves a loan
    @staticmethod
    def approve_loan(pk):
        Loan.objects.get(pk=pk).status = 'Approved'

    # rejects a payment
    @staticmethod
    def reject_payment(pk):
        Payment.objects.get(pk=pk).isApproved = False

    # rejects a loan
    @staticmethod
    def reject_loan(pk):
        Loan.objects.get(pk=pk).status = 'Rejected'

    # edits a payment
    @staticmethod
    def edit_payment(pk, ornum, idnum, date, amount):
        Payment.objects.get(pk=pk).isApproved = True
        Payment.objects.get(pk=pk).orNum = ornum
        Payment.objects.get(pk=pk).idNum = idnum
        Payment.objects.get(pk=pk).date = date
        Payment.objects.get(pk=pk).amount = amount


class Delete:
    @staticmethod
    def delete_payment(pk):
        Payment.objects.get(pk=pk).delete()

    @staticmethod
    def delete_loan(pk):
        Loan.objects.get(pk=pk).delete()

    @staticmethod
    def delete_student(pk):
        Student.objects.get(pk=pk).delete()
