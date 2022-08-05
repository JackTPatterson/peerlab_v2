from django.db import models

# Create your models here.

#i forgot how to do custom users 
    
# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     birth_date = models.DateField()
#     phone = models.CharField(max_length=255)
#     school = models.CharField(max_length=255)
    
#     def __repr__(self):
#         return f"<Profile object: {self.user} {self.bio} {self.location} {self.birth_date} {self.created_at} {self.updated_at}>"
    
    
class UserSessions(models.Model):
    session_id = models.IntegerField(primary_key=True)
    #user_id = models.ForeignKey(User, related_name="sessions", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    topic = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    tutor = models.CharField(max_length=255)
    isRecurring = models.BooleanField(default=False)
    startDate = models.DateField(null=True)
    time = models.TimeField(null=True)
    branch = models.CharField(max_length=255)
    
    
    
    def __repr__(self):
        return f"<Sessions object: {self.user_id} {self.created_at}>"
    
class GuestSessions(models.Model):
    session_id = models.IntegerField(primary_key=True)
    fullName = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    phoneNumber = models.CharField(max_length=255)
    tutor = models.CharField(max_length=255)
    school = models.CharField(max_length=255)
    grade = models.CharField(max_length=255)
    topic = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    isRecurring = models.BooleanField(default=False)
    startDate = models.DateField(null=True)
    time = models.TimeField(null=True)
    branch = models.CharField(max_length=255)
    
    