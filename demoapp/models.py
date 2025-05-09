from djongo import models  # Use Djongo's models for MongoDB
from django.contrib.auth.models import AbstractUser
from bson.objectid import ObjectId  # MongoDB ObjectId

# ✅ Define a named function to replace lambda
def generate_object_id():
    return str(ObjectId())

class CustomUser(AbstractUser):
    _id = models.CharField(max_length=24, default=generate_object_id, primary_key=True)
    groups = models.ManyToManyField(
        "auth.Group",
        related_name="customuser_groups",
        blank=True
    )
    user_permissions = models.ManyToManyField(
        "auth.Permission",
        related_name="customuser_permissions",
        blank=True
    )

class Blog(models.Model):
    _id = models.CharField(max_length=24, default=generate_object_id, primary_key=True)
    name = models.CharField(max_length=400)
    image = models.FileField(upload_to="images/", blank=True, null=True)
    iam = models.CharField(max_length=500)
    resume = models.FileField(upload_to="images/", blank=True, null=True)
    about_you = models.TextField()

    def __str__(self):
        return self.name if self.name else "Unnamed Blog"

class Projects(models.Model):
    _id = models.CharField(max_length=24, default=generate_object_id, primary_key=True)
    image = models.ImageField(upload_to="images/", blank=True, null=True)
    description = models.CharField(max_length=1000)

    def __str__(self):
        return self.description if self.description else "No description"

class Certifications(models.Model):
    _id = models.CharField(max_length=24, default=generate_object_id, primary_key=True)
    image = models.ImageField(upload_to="images/", blank=True, null=True)
    description = models.CharField(max_length=1000)

    def __str__(self):
        return self.description if self.description else "No description"

class Contact(models.Model):
    _id = models.CharField(max_length=24, default=generate_object_id, primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    contact_number = models.CharField(max_length=15, blank=True, null=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
